import abc
import typing

from .Error import Error


class Symbol(abc.ABC):
    """
    Represents symbols.

    Symbols compile by position: ``_from_mcnp_at`` parses ``source`` starting at ``pos`` and returns
    the end position, so compiling never copies the rest of the source. ``from_mcnp`` wraps it.

    Subclasses that override only ``from_mcnp``, e.g., to preprocess, keep being reached through
    ``_from_mcnp_at``, which then compiles a slice with their ``from_mcnp``, and their
    ``super().from_mcnp`` compiles with the nearest ``_from_mcnp_at`` that parses by position.
    """

    # Nearest ``_from_mcnp_at`` in the MRO that parses by position, i.e., not ``_from_mcnp_at_by_slice``.
    _from_mcnp_at_by_position: typing.ClassVar[typing.Callable[..., tuple[typing.Any, int]] | None] = None

    def __init_subclass__(cls, **kwargs: typing.Any) -> None:
        """
        Routes ``_from_mcnp_at`` to overrides of ``from_mcnp``.
        """

        super().__init_subclass__(**kwargs)

        for base in cls.__mro__:
            if base is Symbol:
                break
            if '_from_mcnp_at' in base.__dict__:
                # Position parser (or an inherited routing to an override) comes first.
                break
            if 'from_mcnp' in base.__dict__:
                # Override of ``from_mcnp`` comes first: parse slices with it.
                cls._from_mcnp_at = classmethod(_from_mcnp_at_by_slice)  # ty: ignore[invalid-assignment]
                break

        cls._from_mcnp_at_by_position = None
        for base in cls.__mro__:
            if base is Symbol:
                break
            method = base.__dict__.get('_from_mcnp_at')
            if method is not None and method.__func__ is not _from_mcnp_at_by_slice:
                cls._from_mcnp_at_by_position = method.__func__
                break

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding symbols.

        Parameters:
            source: Source string to compile.

        Returns:
            Symbol corresponding to ``source`` and the remainder of ``source``.
        """

        parse = cls._from_mcnp_at_by_position
        if parse is None:
            raise NotImplementedError

        symbol, end = parse(cls, source, 0)
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

        return _from_mcnp_at_by_slice(cls, source, pos)

    @abc.abstractmethod
    def to_mcnp(self) -> str:
        """
        Decompiles symbols into their corresponding source strings.

        Returns:
            Source string corresponding to ``self``.
        """

        raise NotImplementedError

    def __str__(self) -> str:
        """
        Stringifies symbols.
        """

        return self.to_mcnp()


def _from_mcnp_at_by_slice(cls: type[Symbol], source: str, pos: int) -> tuple[typing.Any, int]:
    """
    Compiles source strings at positions with ``from_mcnp``, for symbols that do not parse by position.

    Parameters:
        cls: Symbol to compile.
        source: Source string to compile.
        pos: Position in ``source`` to compile at.

    Returns:
        Symbol corresponding to ``source`` at ``pos`` and the position where it ends.
    """

    symbol, remainder = cls.from_mcnp(source[pos:] if pos else source)
    return symbol, len(source) - len(remainder)


def _parse_at(kinds: tuple[type[Symbol], ...], source: str, pos: int) -> tuple[Symbol, int]:
    """
    Matches ``source`` at ``pos`` to symbol in ``kinds``.

    This function disambiguated using the longest match rule; ties keep the first kind.

    Parameters:
        kinds: Symbols to match.
        source: Source to match.
        pos: Position in ``source`` to match at.

    Returns:
        Matched symbol and the position where it ends.
    """

    if len(kinds) == 1:
        return kinds[0]._from_mcnp_at(source, pos)

    # Searching for longest match, i.e., the largest end.
    error: Error | None = None
    longest: tuple[Symbol, int] | None = None
    for kind in kinds:
        try:
            parse = kind._from_mcnp_at(source, pos)

            # Updating ``longest``.
            if longest is None or parse[1] > longest[1]:
                longest = parse
        except Error as err:
            if error is None:
                error = err

    if longest is None:
        assert error is not None
        raise error
    else:
        return longest


def _parse(kinds: tuple[type[Symbol], ...], source: str) -> tuple[Symbol, str]:
    """
    Matches ``source`` to symbol in ``kinds``.

    This function disambiguated using the longest match rule.

    Parameters:
        kinds: Symbols to match.
        source: Source to match.

    Returns:
        Matched symbol and the remainder of ``source``.
    """

    symbol, end = _parse_at(kinds, source, 0)
    return symbol, source[end:]
