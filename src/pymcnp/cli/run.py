"""
'run' contains functions for interacting with MCNP.

Functions:
    run_inp_file: Runs INP files using MCNP.
    run_inp_object: Runs INP objects using MCNP.
    main: Runs the command line for interacting with MCNP.
"""


import os
import sys


from ..files import inp
from . import _io
from . import _save


class Run:
    def __init__(self, path: str, command: str = "mcnp"):
        """
        '__init__' initalizes 'Run'.

        Parameters:
            path: Path to working directory.
            command: Command to execute.
        """

        self.path: str = path
        self.command: str = command
        self.filename: str = None
        self.inpt: dict = None

    @classmethod
    def from_inp_object(cls, inpt: inp.Inp):
        """
        'from_inp_file' populates run objects from INP objects.

        Parameters:
            inpt (Inp): INP object to load.
        """

        runner = cls(".")

        runner.inpt = inpt
        runner.filename = f"mcnp-save-{_io.get_timestamp()}.i"
        inpt.to_mcnp_file(runner.filename)

        return runner

    @classmethod
    def from_inp_file(cls, filename: str):
        """
        'from_inp_file' populates run objects from files.

        Parameters:
            filename: INP file to load.
        """

        runner = cls(".")

        if not os.path.isfile(filename):
            raise ValueError

        runner.inpt = inp.Inp().from_mcnp_file(filename)
        runner.filename = filename

        return runner

    def run_inp(self) -> str:
        """
        'run_inp' runs INP files using MCNP.
        """

        run_directory = f"{self.path}/pymcnp-run-{_io.get_timestamp()}"
        os.mkdir(run_directory)

        os.system(f"{self.command} I={self.filename}")

        return run_directory

    def run_inp_parallel(self, count: int) -> str:
        """
        'run_inp_parallel' runs INP files in parallel using MCNP.

        Parameters:
            count (int): Number of parallel runs.
        """

        parallel_directory = f"{self.path}/pymcnp-parallel-{_io.get_timestamp()}"

        subrun = Run(parallel_directory)
        for i in range(0, count):
            subrun.run_inp()

        return parallel_directory


def main(argv: list[str] = sys.argv[1:]) -> None:
    """
    'main' runs the command line for interacting with MCNP.

    Parameters:
        argv (list): Arguments list.
    """

    match argv[0] if argv else None:
        case arg if arg is not None and arg[0] != "-":
            print(_io.INFO_RUNNING_MCNP)

            inpts = _save.Save.get_save()
            run = Run(".")
            run.filename = inpts[argv[0]][0]
            run.inpt = inpts[argv[0]][1]

            match argv[1] if argv[1:] else None:
                case "-p" | "--parallel":
                    run.run_inp_parallel(10)
                case None:
                    run.run_inp()
                case _:
                    _io.error(_io.ERROR_UNRECOGNIZED_OPTION)

        case "-f" | "--file":
            if len(argv) < 2:
                _io.error(_io.ERROR_INSUFFICENT_ARGS)

            print(_io.INFO_RUNNING_MCNP)

            run = Run(".").from_inp_file(argv[1])

            match argv[2] if argv[2:] else None:
                case "-p" | "--parallel":
                    run.run_inp_parallel(10)
                case None:
                    run.run_inp()
                case _:
                    _io.error(_io.ERROR_UNRECOGNIZED_OPTION)

        case None:
            _io.error(_io.ERROR_INSUFFICENT_ARGS)

        case _:
            _io.error(_io.ERROR_UNRECOGNIZED_OPTION)
