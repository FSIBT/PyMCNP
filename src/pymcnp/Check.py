import pathlib
import warnings
import dataclasses

from . import abc
from .Inp import Inp


@dataclasses.dataclass
class Check(abc.Utility):
    """
    Represents utilities that check input files.
    """

    def check(self, path: pathlib.Path | str) -> tuple[abc.Warning | abc.Error, ...]:
        """
        Checks input file at `path`.

        Parameters:
            path: Input file or its path to check.

        Raises:
            Error: File not found.
        """

        path = pathlib.Path(path)
        if not path.exists():
            raise abc.Error('File not found', f'{path=}')

        try:
            with warnings.catch_warnings(record=True) as caught_warnings:
                Inp.from_file(path)
        except abc.Error as err:
            return (*(caught_warning.message for caught_warning in caught_warnings if isinstance(caught_warning.message, abc.Warning)), err)

        return tuple((caught_warning.message for caught_warning in caught_warnings if isinstance(caught_warning.message, abc.Warning)))
