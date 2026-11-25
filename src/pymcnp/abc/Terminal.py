import re
import typing

from .Error import Error
from .Symbol import Symbol


CACHE: dict[str, type[Symbol]] = {}


class Terminal(Symbol, str):
    """
    Represents terminal symbols.
    """

    _pattern: typing.ClassVar[re.Pattern] = re.compile(r'(\S+)', re.IGNORECASE)
    _default: typing.ClassVar[str | None] = None

    def __init_subclass__(cls) -> None:
        """
        Validates subclasses.
        """

        super().__init_subclass__()

        if cls._default is not None:
            cls.from_mcnp(cls._default)

    def __new__(cls, value: str) -> typing.Self:
        """
        Constructs terminal symbols.

        Parameters:
            value: String value of terminal symbol.

        Returns:
            Terminal symbol with value ``value``.

        Raises:
            Error: Expected terminal.
        """

        self = super().__new__(cls, value)

        match = cls._pattern.match(value)
        if match is None or value[match.end() :] != '':
            raise Error(f"Expected Terminal[r'{cls._pattern.pattern}']", f'{value=}')

        return self

    @classmethod
    def __class_getitem__(cls, pattern: str) -> type[typing.Self]:
        """
        Gets subclasses of ``Terminal`` representing terminal symbols matching ``pattern``.

        Parameters:
            pattern: Regular expression for terminal symbols ``index``.

        Returns:
            Subclass of ``Terminal`` representing terminal symbols matching ``pattern``.
        """

        if pattern not in CACHE:
            CACHE[pattern] = type(
                f"Terminal[r'{pattern}']",
                (cls,),
                {'_pattern': re.compile(rf'({pattern})', re.IGNORECASE)},
            )

        return typing.cast(type[typing.Self], CACHE[pattern])

    @classmethod
    def _from_mcnp_at(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        """
        Compiles source strings at positions into their corresponding terminal symbols.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.

        Returns:
            Terminal symbol corresponding to ``source`` at ``pos`` and the position where it ends.

        Raises:
            Error: Expected terminal.
        """

        match = cls._pattern.match(source, pos)
        if match is None:
            raise Error(f"Expected Terminal[r'{cls._pattern.pattern}']", f'source[:200]={source[pos : pos + 200]!r}')

        return str.__new__(cls, match[0]), match.end()

    def to_mcnp(self) -> str:
        """
        Decompiles symbols into their corresponding terminal source strings.

        Returns:
            Source string corresponding to ``self``.
        """

        return self
