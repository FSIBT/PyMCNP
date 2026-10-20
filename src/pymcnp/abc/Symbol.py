import abc
import typing

from .Error import Error


class Symbol(abc.ABC):
    """
    Represents symbols.
    """

    @classmethod
    @abc.abstractmethod
    def _from(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        """
        Compiles `source` starting at `pos` into the corresponding symbol.

        Returns:
            Symbol and the position in `source` after it.
        """

        raise NotImplementedError

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding symbols.

        Parameters:
            source: Source string to compile.

        Returns:
            Symbol corresponding to `source` and the unparsed remainder.
        """

        assert isinstance(source, str)

        symbol, pos = cls._from(source, 0)
        return symbol, source[pos:]

    @abc.abstractmethod
    def to_mcnp(self) -> str:
        """
        Decompiles symbols into their corresponding source strings.

        Returns:
            Source string corresponding to `self`.
        """

        raise NotImplementedError

    def __str__(self) -> str:
        """
        Stringifies symbols.
        """

        return self.to_mcnp()


def _excerpt(source: str, pos: int) -> str:
    """
    Shortens `source` from `pos` for error messages.
    """

    return f'source={source[pos : pos + 80]!r}'


def _parse(kinds: tuple[type[Symbol], ...], source: str, pos: int) -> tuple[Symbol, int]:
    """
    Matches `source` to symbol in `kinds`.

    This function disambiguated using the longest match rule.

    Parameters:
        kinds: Symbols to match.
        source: Source to match.

    Returns:
        Matched symbol.
    """

    assert isinstance(kinds, tuple)
    assert isinstance(source, str)

    if len(kinds) == 1:
        return kinds[0]._from(source, pos)

    # Searching for longest match.
    error: Error | None = None
    longest: tuple[Symbol | None, int] = (None, pos)
    for kind in kinds:
        try:
            parse = kind._from(source, pos)

            # Updating `longest`.
            if longest[0] is None or parse[1] > longest[1]:
                longest = parse
        except Error as err:
            if error is None:
                error = err

    if longest[0] is None:
        assert error is not None
        raise error
    else:
        return longest
