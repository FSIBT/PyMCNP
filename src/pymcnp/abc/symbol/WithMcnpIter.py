import abc
import typing

from ..Symbol import Symbol


T = typing.TypeVar('T', bound=Symbol)
U = typing.TypeVar('U', bound=Symbol)


class WithMcnpIter(abc.ABC, typing.Generic[T, U]):
    """
    Represents symbols with iterative compilers.

    Subclasses implement ``_from_mcnp_iter_at``, which compiles by position; ``from_mcnp_iter``,
    ``from_mcnp`` and ``_from_mcnp_at`` wrap it.
    """

    @classmethod
    @abc.abstractmethod
    def _from_mcnp_iter_at(cls, source: str, pos: int, returning: bool = False) -> typing.Generator[typing.Generator[U, None, None] | U, None, tuple[typing.Self | None, int]]:
        """
        Compiles source strings at positions into their corresponding symbols iteratively.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.
            returning: Flag to/to not build the symbol.

        Yields:
            Parsed subsymbols, or generators yielding parsed subsymbols.

        Returns:
            Symbol corresponding to ``source`` at ``pos`` if ``returning`` (else ``None``), and the position where it ends.
        """

        raise NotImplementedError

    @classmethod
    def from_mcnp_iter(cls, source: str, returning: bool = False) -> typing.Generator[typing.Generator[U, None, None] | U, None, tuple[typing.Self, str] | None]:
        """
        Compiles source strings into their corresponding symbols iteratively.

        Parameters:
            source: Source string to compile.
            returning: Flag to/to not return.

        Yields:
            Parsed subsymbols, or generators yielding parsed subsymbols (each finished before the next is yielded).

        Returns:
            Symbol corresponding to ``source`` and the remainder of ``source`` if ``returning``.
        """

        symbol, end = yield from cls._from_mcnp_iter_at(source, 0, returning=returning)

        if returning:
            return symbol, source[end:]

    @classmethod
    def _from_mcnp_at(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        """
        Compiles source strings at positions into their corresponding symbols.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.

        Returns:
            Symbol corresponding to ``source`` at ``pos`` and the position where it ends.
        """

        generator = cls._from_mcnp_iter_at(source, pos, returning=True)
        try:
            while True:
                next(generator)
        except StopIteration as stop:
            return stop.value
