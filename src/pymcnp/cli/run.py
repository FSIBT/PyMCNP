"""
Usage:
    pymcnp run <inp>... [ options ]

Options:
    -c --command=<command>        Command to run.
    -p --path=<path>              Working directory.
"""

import os
import shutil
import pathlib
import subprocess

from docopt import docopt

from . import _io
from ..Inp import Inp
from ..utils import errors


class Run:
    """
    Runs MCNP files.

    Attributes:
        inps: Files to run.
        command: Command to run.
    """

    def __init__(self, *inps: Inp, command='mcnp6'):
        """
        Initializes ``Run``.

        Parameters:
            inps: Files to run.
            command: Command to run.
        """

        if inps is None or None in inps:
            raise errors.CliError(errors.CliCode.SEMANTICS_INP, inps)

        if command is None or not (shutil.which(command)):
            raise errors.CliError(errors.CliCode.SEMANTICS_COMMAND, command)

        self.inps = inps
        self.command = command

    def prehook_file(self, path: pathlib.Path):
        """
        Runs before a file.

        Parameters:
            path: Path to run directory.
        """

        pass

    def posthook_file(self, path: pathlib.Path):
        """
        Runs after a file.

        Parameters:
            path: Path to run directory.
        """

        pass

    def prehook_batch(self, path: pathlib.Path):
        """
        Runs before the batch.

        Parameters:
            path: Path to batch directory.
        """

        pass

    def posthook_batch(self, path: pathlib.Path):
        """
        Runs after the batch.

        Parameters:
            path: Path to batch directory.
        """

        pass

    def run(self, path: str | pathlib.Path):
        """
        Runs a file.

        Parameters:
            path: Directory for run.
        """

        directory = pathlib.Path(path) / f'pymcnp-{_io.get_timestamp()}'
        directory.mkdir()

        self.prehook_batch(directory)

        processes = []
        for i, inp in enumerate(self.inps):
            subdirectory = directory / f'run-{i}'
            path_input = subdirectory / f'run-{i}.inp'
            path_output = subdirectory / f'run-{i}.outp'
            path_ptrac = subdirectory / f'run-{i}.ptrac'

            subdirectory.mkdir()
            with path_input.open('w') as file:
                file.write(inp.to_mcnp())

            self.prehook_file(subdirectory)
            process = subprocess.Popen([f'{self.command}', f'inp={path_input} outp={path_output} ptrac={path_ptrac}'])
            processes.append((process, subdirectory))

        for process, subdirectory in processes:
            process.wait()
            self.posthook_file(subdirectory)

        self.posthook_batch(directory)


def main() -> None:
    """
    Executes the ``pymcnp run`` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    path = args['--path'] if args['--path'] else os.getcwd()
    command = args['--command'] if args['--command'] else 'mcnp6'

    # Reading INP file(s).
    try:
        inps = map(Inp.from_file, map(pathlib.Path, args['<inp>']))
    except errors.InpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)

    # Running!
    try:
        Run(*inps, command=command).run(pathlib.Path(path))
    except errors.CliError as err:
        _io.error(err.__str__())

    _io.done()
