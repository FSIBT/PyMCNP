import os
import pathlib
import difflib

from . import _doer
from . import errors
from .Inp import Inp


class Check(_doer.Doer):
    """
    Checks OUTP files.

    Attribute:
        path: File to check.
    """

    def __init__(self, path: str | pathlib.Path):
        """
        Initializes `Check`.

        Attribute:
            path: File to check.

        Raises:
            CLIError: RUNTIME_DOER.
        """

        if path is None:
            raise errors.CliError(errors.CliCode.RUNTIME_PATH, path)

        self.path = pathlib.Path(path)

    def check(self):
        """
        Checks a file.
        """

        try:
            with self.path.open('r') as file:
                current = file.read()
                correct = Inp.from_mcnp(current).to_mcnp()

                return difflib.unified_diff(current.split('\n'), correct.split('\n'))
        except FileNotFoundError:
            raise errors.CliError(errors.CliCode.RUNTIME_PATH, self.path)

    def fix(self):
        """
        Fixes a file.
        """

        inp = Inp.from_file(self.path)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            inp.to_file(self.path)
