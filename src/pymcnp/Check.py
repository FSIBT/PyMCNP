import os
import pathlib
import difflib
import dataclasses

from . import abc
from .Inp import Inp


@dataclasses.dataclass
class Check(abc.Utility):
    """
    Represents utilities that check input files.

    Attribute:
        path: Path to input file to check.
    """

    path: pathlib.Path | str

    def __post_init__(self):
        """
        Validates utitlites that check input files.

        Raises:
            Error.
        """

        self.path = pathlib.Path(self.path)
        if not self.path.exists():
            raise abc.Error('File not found', f'{self.path=}')

    def check(self):
        """
        Checks the input file at `path`.
        """

        assert isinstance(self.path, pathlib.Path)

        current = self.path.read_text()
        correct = Inp.from_mcnp(current)[0].to_mcnp()
        return difflib.unified_diff(current.split('\n'), correct.split('\n'))

    def fix(self):
        """
        Fixes the input file at `path`.
        """

        assert isinstance(self.path, pathlib.Path)

        file = Inp.from_file(self.path)[0]
        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            file.to_file(self.path)
