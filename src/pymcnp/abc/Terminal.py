import re
import typing

from .Error import Error
from .Symbol import Symbol


CACHE: dict[str, type[Symbol]] = {}

# End of ``Terminal._pattern``, matching the rest of the source.
_REST = r'([\s\S]*)'


class Terminal(Symbol, str):
    """
    Represents terminal symbols.
    """

    _pattern: typing.ClassVar[re.Pattern] = re.compile(r'(\S+)([\s\S]*)', re.IGNORECASE)
    _head: typing.ClassVar[re.Pattern] = re.compile(r'(\S+)', re.IGNORECASE)
    _default: typing.ClassVar[str | None] = None

    def __init_subclass__(cls) -> None:
        """
        Validates subclasses.
        """

        # Deriving the pattern matching only the terminal from ``_pattern``, i.e., ``(<terminal>)([\s\S]*)``.
        if '_pattern' in cls.__dict__:
            pattern = cls._pattern.pattern
            if not pattern.endswith(_REST):
                raise Error('``Terminal._pattern`` must end with ``([\\s\\S]*)``.', f'{pattern=}')
            cls._head = re.compile(pattern[: -len(_REST)], cls._pattern.flags)

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

        assert isinstance(value, str)

        self = super().__new__(cls, value)

        match = cls._pattern.match(value)
        if match is None or match[2] != '':
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

        assert isinstance(pattern, str)

        if pattern not in CACHE:
            CACHE[pattern] = type(
                f"Terminal[r'{pattern}']",
                (cls,),
                {'_pattern': re.compile(rf'({pattern})([\s\S]*)', re.IGNORECASE)},
            )

        return typing.cast(type[typing.Self], CACHE[pattern])

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding terminal symbols.

        Parameters:
            source: Source string to compile.

        Returns:
            Terminal symbol corresponding to ``source``.

        Raises:
            Error: Expected terminal.
        """

        assert isinstance(source, str)

        # Matching only the terminal, since matching the rest too costs time proportional to the length of ``source``.
        match = cls._head.match(source)
        if match is None:
            raise Error(f"Expected Terminal[r'{cls._pattern.pattern}']", f'{source[:200]=}')

        # Skipping the validation of ``__new__``, since ``match`` already matched the pattern.
        return str.__new__(cls, match[0]), source[match.end() :]

    def to_mcnp(self) -> str:
        """
        Decompiles symbols into their corresponding terminal source strings.

        Returns:
            Source string corresponding to ``self``.
        """

        return self
