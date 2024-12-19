"""
Usage:
    pymcnp run <file>... [ options ]

Options:
    -c --command=<command>        Command to run.
    -s --hosts=<host>...          External hosts.
"""

import os
import shutil
import pathlib
import subprocess
from types import ModuleType

from docopt import docopt

from . import _io
from . import _errors
from .. import files
from .hooks import default


EXECUTABLE = """
import importlib
import subprocess


def main():
    prehook = importlib.import_module('prehook')
    posthook = importlib.import_module('posthook')

    path = "{path}"
    command = "{command}"

    prehook.main(path)
    subprocess.run(command, shell=True)
    posthook.main(path)


if __name__ == '__main__':
    main()
"""


class Run:
    """
    Represents collection of MCNP runs.

    Attributes:
        inps: ``Inp`` objects.
        path: Working directory.
        command: Terminal command.
        prehook: Prehook module with ``main`` function.
        posthook: Posthook module with ``main`` function.
        path_directory: Path to batch run directory
        path_subdirectories: List of paths to run directories.
    """

    PREHOOK_PASS = default
    POSTHOOK_PASS = default

    def __init__(
        self,
        inps: list[files.inp.Inp],
        path: pathlib.Path,
        prehook: ModuleType = PREHOOK_PASS,
        posthook: ModuleType = POSTHOOK_PASS,
        command: str = 'mcnp6',
    ):
        """
        Initializes ``Run``.

        Parameters:
            inps: ``Inp`` objects.
            path: Working directory.
            command: Terminal command.
            prehook: Prehook module with ``main`` function.
            posthook: Posthook module with ``main`` function.

        Raises:
            CliError: INVALID_INP.
            CliError: INVALID_PATH.
            CliError: INVALID_PREHOOK.
            CliError: INVALID_POSTHOOK.
            CliError: INVALID_COMMAND.
        """

        if inps is None:
            raise _errors.CliError(_errors.CliCode.INVALID_INP, str(inps))

        for inp in inps:
            if inp is None:
                raise _errors.CliError(_errors.CliCode.INVALID_INP, str(inp))

        if path is None:
            raise _errors.CliError(_errors.CliCode.INVALID_PATH, str(path))

        if prehook is None or not hasattr(prehook, 'main'):
            raise _errors.CliError(_errors.CliCode.INVALID_PREHOOK, str(prehook))

        if posthook is None or not hasattr(posthook, 'main'):
            raise _errors.CliError(_errors.CliCode.INVALID_POSTHOOK, str(posthook))

        if command is None:
            raise _errors.CliError(_errors.CliCode.INVALID_COMMAND, str(command))

        if shutil.which(command) is None:
            raise _errors.CliError(_errors.CliCode.INVALID_COMMAND, str(command))

        if shutil.which('parallel') is None:
            raise _errors.CliError(_errors.CliCode.INVALID_COMMAND, 'parallel')

        # Storing arguments.
        self.command = command
        self.inps = inps
        self.prehook = prehook
        self.posthook = posthook

        # Initializing paths.
        timestamp = _io.get_timestamp()
        self.path_directory = path / f'pymcnp-{timestamp}'
        self.path_subdirectories = []

        for i, inp in enumerate(self.inps):
            self.path_subdirectories.append(self.path_directory / f'run-{i}')

    def run(self, hosts: list[str] = []):
        """
        Runs MCNP INP files.

        Parameters:
            hosts: List of hostnames on which to execute.
        """

        # Creating directories.
        self.path_directory.mkdir()

        for i, (inp, path_subdirectory) in enumerate(zip(self.inps, self.path_subdirectories)):
            path_inp = path_subdirectory / 'inp.i'
            path_script = path_subdirectory / 'script.py'
            path_prehook = path_subdirectory / 'prehook.py'
            path_posthook = path_subdirectory / 'posthook.py'

            command = f'{self.command} {path_inp}'

            path_subdirectory.mkdir()
            inp.to_mcnp_file(path_inp)
            path_script.write_text(EXECUTABLE.format(path=self.path_directory, command=command))
            shutil.copy(pathlib.Path(self.prehook.__file__), path_prehook)
            shutil.copy(pathlib.Path(self.posthook.__file__), path_posthook)

        # Running!
        param_files = ' '.join(
            str(subdirectory).split('/')[-1] for subdirectory in self.path_subdirectories
        )

        if hosts == []:
            command = f'parallel python3 {{}}/script.py ::: {param_files}'
        else:
            param_hosts = ' '.join(hosts)
            command = f'parallel -S {param_hosts} --transferfile {{}} --return {{}} python3 {{}}/{self.command}.py ::: {param_files}'

        subprocess.run(command, cwd=self.path_directory, shell=True)


def main() -> None:
    """
    Executes the ``pymcnp run`` command.

    ``pymcnp run`` runs INP files.
    """

    args = docopt(__doc__)

    inps = args['<file>']
    hosts = args['--hosts'] if args['--hosts'] else []
    command = args['--command'] if args['--command'] else 'mcnp6'

    try:
        inps = [files.inp.Inp.from_mcnp_file(inp) for inp in inps]
    except files.utils.errors.McnpError as err:
        _io.error(err.__str__())

    path = pathlib.Path(os.getcwd())

    try:
        run = Run(inps, path, command=command)
    except _errors.CliError as err:
        _io.error(err.__str__())

    run.run(hosts)
