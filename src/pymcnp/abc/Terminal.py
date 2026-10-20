import re
import typing

from .Error import Error
from .Symbol import Symbol
from .Symbol import _excerpt


CACHE: dict[str, type[Symbol]] = {}


class Terminal(Symbol, str):
    """
    Represents terminal symbols.
    """

    _pattern: typing.ClassVar[re.Pattern] = re.compile(r'(\S+)([\s\S]*)', re.IGNORECASE)
    _token: typing.ClassVar[re.Pattern] = re.compile(r'(\S+)', re.IGNORECASE)
    _default: typing.ClassVar[str | None] = None

    def __init_subclass__(cls) -> None:
        """
        Validates subclasses.
        """

        # Matching `_pattern` without its trailing `([\s\S]*)`, which would
        # scan and copy the rest of the source on every match.
        cls._token = re.compile(cls._pattern.pattern.removesuffix(r'([\s\S]*)'), cls._pattern.flags)

        if cls._default is not None:
            cls._from(cls._default, 0)

    def __new__(cls, value: str) -> typing.Self:
        """
        Constructs terminal symbols.

        Parameters:
            value: String value of terminal symbol.

        Returns:
            Terminal symbol with value `value`.

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
        Gets subclasses of `Terminal` representing terminal symbols matching `pattern`.

        Parameters:
            pattern: Regular expression for terminal symbols `index`.

        Returns:
            Subclass of `Terminal` representing terminal symbols matching `pattern`.
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
    def _from(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        match = cls._token.match(source, pos)
        if match is None:
            raise Error(f"Expected Terminal[r'{cls._pattern.pattern}']", _excerpt(source, pos))

        return str.__new__(cls, match[1]), match.end()

    def to_mcnp(self) -> str:
        """
        Decompiles symbols into their corresponding terminal source strings.

        Returns:
            Source string corresponding to `self`.
        """

        return self
