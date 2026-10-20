import os
import shutil
import pathlib
import datetime
import subprocess
import dataclasses
import collections.abc
import concurrent.futures

from . import abc
from .Inp import Inp
from .Outp import _fatal_errors


@dataclasses.dataclass
class Result:
    """
    Represents the outcome of one run.

    Attributes:
        index: Run number.
        directory: Directory the run executed in.
        inp: Input file.
        outp: Output file, `None` if the command did not write one.
        ptrac: PTRAC file, `None` if the command did not write one.
        runtpe: Runtpe file, `None` if the command did not write one.
        log: File with the command's standard output and error.
        returncode: Exit code of the command.
        fatal_errors: Fatal errors reported in the output file.
    """

    index: int
    directory: pathlib.Path
    inp: pathlib.Path
    outp: pathlib.Path | None
    ptrac: pathlib.Path | None
    runtpe: pathlib.Path | None
    log: pathlib.Path
    returncode: int
    fatal_errors: list[str] = dataclasses.field(default_factory=list)

    @property
    def ok(self) -> bool:
        """
        Whether the run exited with 0 and reported no fatal errors.
        """

        return self.returncode == 0 and not self.fatal_errors


@dataclasses.dataclass
class Run(abc.Utility):
    """
    Represents utitlites that run input files.

    Every input runs in its own directory (`<batch>/<name>/<name>.inp`, `.outp`, `.ptrac`, `.runtpe`, `.log`),
    since MCNP refuses to reuse output files and parallel runs would share one `runtpe`.

    Attributes:
        files: Input files to run.
        command: Command to run.
        max_workers: Maximum number of simultaneous runs, defaults to the number of CPUs.
        names: Names of the runs: a sequence with one name per file, or a template with `{index}`, e.g., `'case-{index}'`. Defaults to `run-{index:05}`.
        check: Whether `run` raises if a run failed.
        batch: Whether `run` puts the runs in a new `pymcnp-<timestamp>` directory inside the given path. If not, the run directories `<path>/<name>` are created directly in the given path, which must not contain them yet.
        directory: Directory holding the run directories, set by `run`.
    """

    files: collections.abc.Sequence[Inp]
    command: str = 'mcnp6'
    max_workers: int | None = None
    names: collections.abc.Sequence[str] | str | None = None
    check: bool = True
    batch: bool = True
    directory: pathlib.Path | None = dataclasses.field(default=None, init=False)

    def __post_init__(self):
        """
        Validates utilities that run input files.

        Raises:
            Error: Invalid value.
        """

        if not shutil.which(self.command):
            raise abc.Error('Invalid value.', f'{self.command=}')

        if self.max_workers is not None and self.max_workers < 1:
            raise abc.Error('Invalid value.', f'{self.max_workers=}')

        names = self._names()
        if len(names) != len(self.files) or len(set(names)) != len(names) or any(not name or name != pathlib.Path(name).name or name.startswith('.') for name in names):
            raise abc.Error('Invalid value.', f'{self.names=}')

    def _names(self) -> list[str]:
        if self.names is None:
            return [f'run-{i:05}' for i in range(len(self.files))]
        if isinstance(self.names, str):
            return [self.names.format(index=i) for i in range(len(self.files))]
        return list(self.names)

    def prehook_file(self, path: pathlib.Path, index: int):
        """
        Runs before a file, in the thread that starts the run.

        Parameters:
            path: Path to run directory.
            index: Run number.
        """

    def posthook_file(self, result: Result):
        """
        Runs after a file, in the thread that ran it, while other runs may still be going.
        Skipped for failed runs if `check` is set.

        Parameters:
            result: Result of the run.
        """

    def prehook_batch(self, path: pathlib.Path):
        """
        Runs before the batch.

        Parameters:
            path: Path to batch directory.
        """

    def posthook_batch(self, path: pathlib.Path):
        """
        Runs after the batch, if no run failed or `check` is not set.

        Parameters:
            path: Path to batch directory.
        """

    def _run_one(self, directory: pathlib.Path, name: str, index: int, file: Inp) -> Result:
        directory.mkdir()
        inp = directory / f'{name}.inp'
        inp.write_text(file.to_mcnp())

        self.prehook_file(directory, index)

        keywords = {key: f'{name}.{key}' for key in ('inp', 'outp', 'ptrac', 'runtpe')}
        log = directory / f'{name}.log'
        with log.open('w') as stream:
            done = subprocess.run(
                [self.command, *(f'{key}={value}' for key, value in keywords.items())],
                cwd=directory,
                stdin=subprocess.DEVNULL,
                stdout=stream,
                stderr=subprocess.STDOUT,
            )

        def found(key: str) -> pathlib.Path | None:
            path = directory / keywords[key]
            return path if path.exists() else None

        outp = found('outp')
        result = Result(
            index=index,
            directory=directory,
            inp=inp,
            outp=outp,
            ptrac=found('ptrac'),
            runtpe=found('runtpe'),
            log=log,
            returncode=done.returncode,
            fatal_errors=_fatal_errors(outp.read_text(errors='replace')) if outp else [],
        )

        if result.ok or not self.check:
            self.posthook_file(result)

        return result

    def run(self, path: pathlib.Path | str) -> list[Result]:
        """
        Runs the input files, at most `max_workers` at a time.

        Parameters:
            path: Directory for run, or, with `batch` unset, the directory that gets the run directories.

        Returns:
            Results of the runs, in the order of the input files.

        Raises:
            Error: A run failed and `check` is set, raised after all runs finished.
        """

        path = pathlib.Path(path)
        names = self._names()

        if self.batch:
            stamp = datetime.datetime.today().strftime('%Y-%m-%d--%H-%M-%S')
            directory = path / f'pymcnp-{stamp}'
            suffix = 0
            while True:
                try:
                    directory.mkdir(parents=True)
                    break
                except FileExistsError:
                    suffix += 1
                    directory = path / f'pymcnp-{stamp}-{suffix}'
        else:
            directory = path
            directory.mkdir(parents=True, exist_ok=True)
            existing = [name for name in names if (directory / name).exists()]
            if existing:
                raise abc.Error('Run directory exists.', f'{directory=} {existing[:3]=}')

        self.directory = directory
        self.prehook_batch(directory)

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers or os.cpu_count() or 1) as pool:
            futures = [pool.submit(self._run_one, directory / name, name, i, file) for i, (name, file) in enumerate(zip(names, self.files))]
            results = [future.result() for future in futures]

        failed = [result for result in results if not result.ok]
        if failed and self.check:
            raise abc.Error(
                'Run failed.',
                '\n'.join(f'{result.directory.name}: exit code {result.returncode}' + ''.join(f'\n    {error}' for error in result.fatal_errors[:3]) + f'\n    see {result.log}' for result in failed),
            )

        self.posthook_batch(directory)

        return results
