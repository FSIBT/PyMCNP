import abc
import typing

from ..Symbol import Symbol


T = typing.TypeVar('T', bound=Symbol)
U = typing.TypeVar('U', bound=Symbol)


class WithMcnpIter(abc.ABC, typing.Generic[T, U]):
    """
    Represents symbols with iterative compilers.
    """

    @classmethod
    @abc.abstractmethod
    def from_mcnp_iter(
        cls, source: str, returning: bool = False
    ) -> typing.Generator[typing.Generator[tuple[U, str], None, tuple[T, str] | None] | tuple[T, str], None, tuple[typing.Self, str] | None]:
        """
        Compiles source strings into their corresponding nonterminal symbols iteratively.

        Parameters:
            source: Source string to compile.
            returning: Flag to/to not return.

        Yields:
            Nonterminal subsymbols.

        Returns:
            Nonterminal symbol corresponding to `source`.
        """

        raise NotImplementedError

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding symbols.

        Parameters:
            source: Source string to compile.

        Returns:
            Symbol corresponding to ``source``.
        """

        generator = cls.from_mcnp_iter(source, returning=True)
        try:
            while True:
                next(generator)
        except StopIteration as stop:
            assert stop.value is not None
            return stop.value
