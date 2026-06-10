import os
import shutil
import pathlib
import datetime
import subprocess
import collections
import dataclasses

from . import abc
from .Inp import Inp


@dataclasses.dataclass
class Run(abc.Utility):
    """
    Represents utitlites that run input files.

    Attributes:
        files: Input files to run.
        command: Command to run.
    """

    files: collections.abc.Sequence[Inp]
    command: str = 'mcnp6'

    def __post_init__(self):
        """
        Validates utilities that run input files.

        Raises:
            Error: Invalid value.
        """

        if not shutil.which(self.command):
            raise abc.Error('Invalid value.', f'{self.command=}')

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

    def run(self, path: pathlib.Path | str):
        """
        Runs an input file.

        Parameters:
            path: Directory for run.
        """

        directory = pathlib.Path(path) / f'pymcnp-{datetime.datetime.today().strftime("%Y-%m-%d--%H-%M-%S")}'
        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            directory.mkdir()

        self.prehook_batch(directory)

        processes = []
        for i, file in enumerate(self.files):
            subdirectory = directory / f'run-{i:05}'
            path_input = subdirectory / f'run-{i:05}.inp'
            path_output = subdirectory / f'run-{i:05}.outp'
            path_ptrac = subdirectory / f'run-{i:05}.ptrac'

            if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                subdirectory.mkdir()
                file.to_file(path_input)

            self.prehook_file(subdirectory, i)
            process = subprocess.Popen([f'{self.command}', f'inp={path_input} outp={path_output} ptrac={path_ptrac}'])
            processes.append((process, subdirectory))

        for i, (process, subdirectory) in enumerate(processes):
            process.wait()
            self.posthook_file(subdirectory, i)

        self.posthook_batch(directory)

        return directory
