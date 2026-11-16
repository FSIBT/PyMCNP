import typing
import pathlib

from .. import symbol
from ..Error import Error
from ..Symbol import Symbol


class WithMcnpIter(symbol.WithMcnpIter):
    """
    Represents nonterminal start symbols with iterative compilers.
    """

    @classmethod
    def from_file_iter(cls, path: pathlib.Path | str, returning: bool = False) -> typing.Generator[Symbol, None, tuple[typing.Self, str] | None]:
        """
        Compiles source strings into their corresponding nonterminal start symbols iteratively.

        Parameters:
            source: Source string to compile.
            returning: Flag to/to not return.

        Yields:
            Nonterminal subsymbols.

        Returns:
            Nonterminal symbol corresponding to `source`.
        """

        path = pathlib.Path(path)

        if not path.is_file():
            raise Error('File not found.', f'{path=}')

        source = path.read_text()

        return (yield from cls.from_mcnp_iter(source, returning=returning))

    @classmethod
    def from_file(cls, path: pathlib.Path | str) -> tuple[typing.Self, str]:
        """
        Compiles files into their corresponding nonterminal start symbols.

        Parameters:
            path: Path to file to compile.

        Returns:
            Nonterminal symbol corresponding to file at ``path``.
        """

        generator = cls.from_file_iter(path, returning=True)
        try:
            while True:
                next(generator)
        except StopIteration as stop:
            assert stop.value is not None
            return stop.value
