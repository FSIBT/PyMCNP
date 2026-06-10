import abc
import typing

from .Error import Error


class Symbol(abc.ABC):
    """
    Represents symbols.
    """

    @classmethod
    @abc.abstractmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding symbols.

        Parameters:
            source: Source string to compile.

        Returns:
            Symbol corresponding to `source`.
        """

        raise NotImplementedError

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


def _parse(kinds: tuple[type[Symbol], ...], source: str) -> tuple[Symbol, str]:
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
    assert all(isinstance(kind, type) and issubclass(kind, Symbol) for kind in kinds)
    assert isinstance(source, str)

    # Searching for longest match.
    error: Error | None = None
    longest: tuple[Symbol | None, str] = (None, source)
    for kind in kinds:
        try:
            parse = kind.from_mcnp(source)

            # Updating `longest`.
            if longest[0] is None:
                longest = parse
            elif len(parse[0].to_mcnp()) > len(longest[0].to_mcnp()):
                longest = parse
        except Error as err:
            if error is None:
                error = err

    if longest[0] is None:
        assert error is not None
        raise error
    else:
        return longest
