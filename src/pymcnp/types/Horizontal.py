import re
import typing

from . import _type
from .. import errors
from .. import _symbol


class Horizontal(_type.Type):
    """
    Represents MCNP horizontal input sytnax.
    """


class _Counted:
    """
    Represents horizontal syntax with an optional count and a keyword suffix.

    Attributes:
        n: Count.
    """

    _SUFFIX: str
    _ZERO = False

    def __init__(self, n: int | None = None):
        """
        Initializes the horizontal syntax.

        Parameters:
            n: Count.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @classmethod
    def from_mcnp(cls, source: str):
        """
        Generates the horizontal syntax from MCNP.

        Parameters:
            source: MCNP horizontal syntax.

        Returns:
            Horizontal syntax.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = cls._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        return cls(int(tokens[1]) if tokens[1] else None)

    def to_mcnp(self):
        """
        Generates MCNP from the horizontal syntax.

        Returns:
            MCNP horizontal syntax.
        """

        n = '' if self.n is None or (not self.n and not self._ZERO) else self.n

        return f'{n}{self._SUFFIX}'


class Repeat(_Counted, Horizontal):
    """
    Represents MCNP repeats.

    Attributes:
        n: Count.
    """

    _REGEX = re.compile('\\A(\\d+)?r\\Z', re.IGNORECASE)
    _SUFFIX = 'r'


class Insert(_Counted, Horizontal):
    """
    Represents MCNP inserts.

    Attributes:
        n: Count.
    """

    _REGEX = re.compile('\\A(\\d+)?i\\Z', re.IGNORECASE)
    _SUFFIX = 'i'


class Multiply(Horizontal):
    """
    Represents MCNP multiply.

    Attributes:
        x: Multiply number.
    """

    _REGEX = re.compile(r'\A(\d+)m\Z', re.IGNORECASE)

    def __init__(self, x: float):
        """
        Initializes `Multiply`.

        Parameters:
            x: Multiply number.

        Returns:
            `Multiply`

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if x is not None and not x:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, x)

        self.x: typing.Final[float] = x

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Multiply` from MCNP.

        Parameters:
            source: MCNP multiply.

        Returns:
            `Multiply`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Multiply._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        x = int(tokens[1])

        return Multiply(x)

    def to_mcnp(self):
        """
        Genereates MCNP multiplies. from `Multiply`.

        Returns:
            MCNP multiply.
        """

        return f'{self.x}m'


class Jump(_Counted, _symbol.Nonterminal):
    """
    Represents MCNP jumps.

    Attributes:
        n: Count.
    """

    _REGEX = re.compile('\\A(\\d+)?j\\Z', re.IGNORECASE)
    _SUFFIX = 'j'
    _ZERO = True


class Log(_Counted, Horizontal):
    """
    Represents MCNP logs.

    Attributes:
        n: Count.
    """

    _REGEX = re.compile('\\A(\\d+)?(log|ilog)\\Z', re.IGNORECASE)
    _SUFFIX = 'log'
