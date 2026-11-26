import typing
import pathlib

from .. import symbol
from ..Error import Error
from .. import _text
from ..Symbol import Symbol


T = typing.TypeVar('T', bound=Symbol)
U = typing.TypeVar('U', bound=Symbol)


class WithMcnpIter(symbol.WithMcnpIter[T, U], typing.Generic[T, U]):
    """
    Represents nonterminal start symbols with iterative compilers.
    """

    @classmethod
    def from_file_iter(cls, path: pathlib.Path | str, returning: bool = False) -> typing.Generator[typing.Generator[U, None, None] | U, None, tuple[typing.Self, str] | None]:
        """
        Compiles source strings into their corresponding nonterminal start symbols iteratively.

        Parameters:
            path: Path to file to compile.
            returning: Flag to/to not return.

        Yields:
            Parsed subsymbols, or generators yielding parsed subsymbols (each finished before the next is yielded).

        Returns:
            Nonterminal symbol corresponding to file at ``path`` and the remainder if ``returning``.

        Raises:
            Error: File not found.
            UnicodeDecodeError: The file is not text, i.e., it holds a NUL byte, e.g., binary PTRAC, or is UTF-16.
        """

        path = pathlib.Path(path)

        if not path.is_file():
            raise Error('File not found.', f'{path=}')

        source = _text.read_text(path)

        return (yield from cls.from_mcnp_iter(source, returning=returning))

    @classmethod
    def from_file(cls, path: pathlib.Path | str) -> tuple[typing.Self, str]:
        """
        Compiles files into their corresponding nonterminal start symbols.

        Parameters:
            path: Path to file to compile.

        Returns:
            Nonterminal symbol corresponding to file at ``path``.

        Raises:
            UnicodeDecodeError: The file is not text, i.e., it holds a NUL byte, e.g., binary PTRAC, or is UTF-16.
        """

        generator = cls.from_file_iter(path, returning=True)
        try:
            while True:
                next(generator)
        except StopIteration as stop:
            assert stop.value is not None
            return stop.value
