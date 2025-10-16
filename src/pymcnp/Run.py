import shutil
import pathlib
import datetime
import subprocess

from . import _doer
from . import errors
from .Inp import Inp


class Run(_doer.Doer):
    """
    Runs INP files.

    Attributes:
        inps: Files to run.
        command: Command to run.
    """

    def __init__(self, inps: Inp, command='mcnp6'):
        """
        Initializes `Run`.

        Parameters:
            inps: Files to run.
            command: Command to run.

        Raises:
            CliCode: RUNTIME_DOER.
        """

        if inps is None or None in inps:
            raise errors.CliError(errors.CliCode.RUNTIME_DOER, inps)

        if command is None or not (shutil.which(command)):
            raise errors.CliError(errors.CliCode.RUNTIME_DOER, command)

        self.inps = inps
        self.command = command

    def prehook_file(self, path: pathlib.Path, index: int):
        """
        Runs before a file.

        Parameters:
            path: Path to run directory.
            index: Run number.
        """

        pass

    def posthook_file(self, path: pathlib.Path, index: int):
        """
        Runs after a file.

        Parameters:
            path: Path to run directory.
            index: Run number.
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

        directory = pathlib.Path(path) / f'pymcnp-{datetime.datetime.today().strftime("%Y-%m-%d--%H-%M-%S")}'
        directory.mkdir()

        self.prehook_batch(directory)

        processes = []
        for i, inp in enumerate(self.inps):
            subdirectory = directory / f'run-{i:05}'
            path_input = subdirectory / f'run-{i:05}.inp'
            path_output = subdirectory / f'run-{i:05}.outp'
            path_ptrac = subdirectory / f'run-{i:05}.ptrac'

            subdirectory.mkdir()
            inp.to_file(path_input)

            self.prehook_file(subdirectory, i)
            process = subprocess.Popen([f'{self.command}', f'inp={path_input} outp={path_output} ptrac={path_ptrac}'])
            processes.append((process, subdirectory))

        for i, (process, subdirectory) in enumerate(processes):
            process.wait()
            self.posthook_file(subdirectory, i)

        self.posthook_batch(directory)

        return directory
