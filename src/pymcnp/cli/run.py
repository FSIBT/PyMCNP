"""
Usage:
    pymcnp run <file> [ --parallel=<threads> ] [ options ]

Options:
    -c --command=<command>        Command to run.
    -P --path=<path>              Path to use.
    -n --dry-run                  Don't run or create directories, just print what would happen
"""

from pathlib import Path
import shutil
import subprocess
import sys

from docopt import docopt
from rich import print

from ..files.inp import Inp
from ..functions.read import read_input
from . import _io


def check_prog(name: str) -> None:
    if shutil.which(name) is None:
        print(f'[red]ERROR[/] Cannot find {name} program.')
        sys.exit(3)


class Run:
    """Encapsulates methods for running a single PyMCNP INP instance.

    Can take either an Inp object or a filename that gets red in.

    Always executes in a custom directory. By default this directory
    doesn't get deleted.

    """

    def __init__(
        self,
        inp: Inp | Path | str,
        path: str | Path = Path('.'),
        command: str = 'mcnp6',
        prefix: str = 'pymcnp',
        run_name: str | None = None,
    ):
        """
        Parameters:
            inp:      The pymcnp input object or filename to run
            path:     Path to directory to store run inputs and outputs.
            command:  Terminal command to execute.
            prefix:   prefix of the run directory
            run_name: name of the run, use a timestamp if not given
        """

        self.command: str = command
        self.path: Path = Path(path)
        self.prefix: str = prefix
        self.run_name: str | None = run_name
        self.run_path: Path | None = None  # will be modified when we run
        self.filename: Path | None = None  # will be modified when we run

        if isinstance(inp, Inp):
            self.inp = inp
        elif isinstance(inp, (str, Path)):
            self.inp = read_input(inp)
        else:
            print('[red]Error[/] cannot parse input')

    def prehook(self):
        pass

    def posthook(self):
        pass

    def create_files(self, dry_run: bool = False):
        """Create directory and input files."""
        if self.run_name is None:
            self.run_name = _io.get_timestamp()

        self.run_path = self.path / f'{self.prefix}-{self.run_name}'
        self.filename = self.run_path / f'input-{self.run_name}.i'

        if dry_run:
            return

        self.run_path.mkdir(exist_ok=True, parents=True)
        self.inp.to_mcnp_file(self.filename)

    def run(self, *, dry_run: bool = False) -> Path:
        """Runs a PyMcnp INP instance.

        Creates a custom directory and a copy of the input file. It
        then calls MCNP. By default no cleanup is done.

        Returns:
            Path to run directory.

        """
        check_prog(self.command)

        self.create_files(dry_run)

        command_to_run = f'{self.command} i={self.filename.name}'

        if dry_run:
            print('[yellow]INFO[/] Dry run:')
            print(f'   creating {self.run_path.absolute()}')
            print('   executing prehook')
            print(f'   {command_to_run}')
            print('   executing posthook')

            # some cleanup
            self.run_path = None
            self.filename = None
            return self.path

        self.prehook()
        subprocess.run(command_to_run, cwd=self.run_path, shell=True)
        self.posthook()

        return self.path

    def cleanup(self):
        """Helper function that can be used in posthooks."""
        if self.run_path:
            for file_or_dir in self.run_path.rglob('*'):
                if file_or_dir.is_file():
                    file_or_dir.unlink()
                else:
                    file_or_dir.rmdir()
            self.run_path.rmdir()


class Parallel:
    """Run  multiple `Run` instancnes.

    At the moment we only create the input directories with the correct files.
    However, in the future we plan to automatically run those using Gnu parallel.

    """

    def __init__(
        self,
        runs,
        prefix: str = 'pymcnp',
        run_name: str | None = None,
    ):
        self.runs = runs
        self.prefix = prefix

        if run_name is None:
            self.run_name = _io.get_timestamp()
        else:
            self.run_name = run_name

        self.path = Path('.') / f'{self.prefix}-{self.run_name}'

    def create_files(self):
        if self.path.is_dir():
            print(f'[red]Error[/] {self.path} already exists. Existing.')
            return

        self.path.mkdir()

        N = len(str(len(self.runs)))  # how many digits do we need?
        for i, run in enumerate(self.runs):
            run.path = self.path
            run.prefix = self.prefix
            run.run_name = f'{i:0{N}d}'
            run.create_files()

    def cleanup(self):
        """Helper function that can be used in posthooks."""
        if self.path:
            for file_or_dir in self.path.rglob('*'):
                if file_or_dir.is_file():
                    file_or_dir.unlink()
                else:
                    file_or_dir.rmdir()
            self.path.rmdir()

    def prehook(self):
        pass

    def posthook(self):
        pass

    def run(self, *, dry_run: bool = False):
        """
        Runs MCNP INP files in parallel.

        Creates a directory with subdirectories for all the different input files

        Returns:
            Path to run directory.
        """

        # some error checking
        self.check_prog('parallel')

        return


class ParallelWithMaxNPS(Parallel):
    """Replace any run with nps > max_nps with multiple runs with a given nps."""

    def __init__(
        self,
        runs,
        prefix: str = 'pymcnp',
        run_name: str | None = None,
        max_nps: float = 1e8,
    ):
        super().__init__(runs, prefix, run_name)
        self.max_nps = int(max_nps)

    def prehook(self):
        out = []
        for run in self.runs:
            nps = run.inp.get_nps()
            if nps > self.max_nps:
                while nps > 0:
                    if nps > self.max_nps:
                        run.inp = run.inp.set_nps(self.max_nps)
                    else:
                        run.inp = run.inp.set_nps(nps)
                    nps -= self.max_nps
                    run.inp = run.inp.set_seed()
                    out.append(run)
        self.runs = out


def main() -> None:
    """
    Executes the ``pymcnp run`` command.

    ``main`` processes the given command line arguments, and it runs either INP
    files single or in parallel.
    """

    args = docopt(__doc__)

    input_file = Path(args['<file>'])

    command = args['--command'] if args['--command'] else 'mcnp6'
    path = args['--path'] if args['--path'] else input_file.parent
    dry_run = args['--dry-run']

    run = Run(
        input_file,
        path=path,
        command=command,
    )

    run.run(dry_run=dry_run)
