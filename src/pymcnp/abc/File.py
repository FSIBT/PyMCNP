import os
import typing
import pathlib

from .Nonterminal import Nonterminal
from .Error import Error


class File(Nonterminal):
    """
    Represents nonterminal start symbols.
    """

    @classmethod
    def from_file(cls, path: pathlib.Path | str) -> tuple[typing.Self, str]:
        """
        Compiles files into their corresponding nonterminal symbols.

        Parameters:
            path: Path to file to compile.

        Returns:
            Nonterminal symbol corresponding to file at `path`.

        Raises:
            Error: File not found.
        """

        path = pathlib.Path(path)

        if not path.is_file():
            raise Error('File not found.', f'{path=}')

        source = path.read_text()

        return cls.from_mcnp(source)

    def to_file(self, path: pathlib.Path | str) -> None:
        """
        Decompiles nonterminal symbols into their corresponding file at `path`.
        """

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            path = pathlib.Path(path)
            path.write_text(self.to_mcnp())
