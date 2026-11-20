import os
import typing
import shutil
import pathlib
import warnings
import datetime
import subprocess
import dataclasses
import concurrent.futures

from . import abc
from .Inp import Inp


@dataclasses.dataclass(frozen=True, slots=True)
class Result:
    """
    Represents the outcome of one run.

    Attributes:
        index: Run number.
        directory: Directory storing the run.
        inp: Path to Input file.
        outp: Path to Output file if it exists.
        ptrac: Path to PTRAC file if it exists.
        runtpe: Path to Runtpe file if it exists.
        log: Path to log file with STDOUT and STDERR.
        returncode: Exit code of the command.
    """

    index: int
    directory: pathlib.Path
    log: pathlib.Path
    inp: pathlib.Path
    outp: pathlib.Path | None
    ptrac: pathlib.Path | None
    runtpe: pathlib.Path | None
    returncode: int

    @property
    def ok(self) -> bool:
        """
        Whether the run exited with 0, wrote an output file, and reported no fatal errors.
        """

        return self.returncode == 0 and self.outp is not None


@dataclasses.dataclass(frozen=True, slots=True)
class Run(abc.Utility):
    """
    Represents utitlites that run input files.

    Attributes:
        command: Command to run.
        directory: Directory to store run.
    """

    command: str = 'mcnp6'
    directory: pathlib.Path = pathlib.Path.cwd() / f'pymcnp-{datetime.datetime.today().strftime("%Y-%m-%d--%H-%M-%S")}'

    def __post_init__(self):
        """
        Validates utilities that run input files.

        Raises:
            Error: Invalid value.
        """

        if not shutil.which(self.command):
            raise abc.Error('Invalid value.', f'{self.command=}')

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            self.directory.mkdir(parents=True, exist_ok=True)

    def prehook_one(self, inp: Inp, index: int) -> None:
        """
        Runs before a file.

        Parameters:
            inp: Input file to run.
            index: Index of run.
        """

    def posthook_one(self, result: Result, index: int) -> typing.Any:
        """
        Runs after a file.

        Parameters:
            result: Result from running the file.
            index: Index of run.
        """

        return result

    def prehook_batch(self, *inps: Inp) -> None:
        """
        Runs before a batch.

        Parameters:
            inps: Input files to run.
        """

    def posthook_batch(self, results: tuple[typing.Any, ...]) -> typing.Any:
        """
        Runs after a batch.

        Parameters:
            results: Results from running the batch.
        """

        return results

    def _run(self, index: int, inp: Inp) -> typing.Any:
        """
        Runs input files.

        Parameters:
            inp: Input file to run.
            index: Index of run.

        Returns:
            Post-processed results of the run.
        """

        self.prehook_one(inp, index)

        # Preparing input and log files.
        inpt = self.directory / f'run-{index:05}.inp'
        inp.to_file(inpt)
        log = self.directory / f'run-{index:05}.log'

        # Running command.
        command = f'{self.command} inp=run-{index:05}.inp outp=run-{index:05}.outp ptrac=run-{index:05}.ptrac runtpe=run-{index:05}.runtpe'
        with log.open('w') as stream:
            done = subprocess.run(command.split(' '), cwd=self.directory, stdout=stream, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)

        # Buidling result from run.
        result = Result(
            index=index,
            directory=self.directory,
            log=log,
            inp=inpt,
            outp=outp if (outp := self.directory / f'run-{index:05}.outp').exists() else None,
            ptrac=ptrac if (ptrac := self.directory / f'run-{index:05}.ptrac').exists() else None,
            runtpe=runtpe if (runtpe := self.directory / f'run-{index:05}.runtpe').exists() else None,
            returncode=done.returncode,
        )

        if done.returncode != 0:
            warnings.warn(abc.Warning('Run failed.', f'command={command}'))

        return self.posthook_one(result, index)

    def run(self, *inps: Inp) -> typing.Any:
        """
        Runs input files.

        Parameters:
            inps: Input files to run.

        Returns:
            Post-processed results of all runs.
        """

        self.prehook_batch(*inps)

        with concurrent.futures.ThreadPoolExecutor(max_workers=(os.cpu_count() or 1)) as pool:
            results = tuple(pool.map(self._run, range(len(inps)), inps))

        return self.posthook_batch(results)
