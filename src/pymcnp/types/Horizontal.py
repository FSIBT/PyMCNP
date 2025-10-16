import re
import typing

from . import _type
from .. import errors
from .. import _symbol


class Horizontal(_type.Type):
    """
    Represents MCNP horizontal input sytnax.
    """

    pass


class Repeat(Horizontal):
    """
    Represents MCNP repeats.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'\A(\d+)?r\Z', re.IGNORECASE)

    def __init__(self, n: int = None):
        """
        Initializes `Repeat`.

        Parameters:
            n: Repetition number.

        Returns:
            `Repeat`

        Raises
            TypesError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Repeat` from MCNP.

        Parameters:
            source: MCNP repeats.

        Returns:
            `Repeat`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Repeat._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        n = int(tokens[1]) if tokens[1] else None

        return Repeat(n)

    def to_mcnp(self):
        """
        Genereates MCNP repeats from `Repeat`.

        Returns:
            MCNP repeats.
        """

        return f'{self.n or ""}r'


class Insert(Horizontal):
    """
    Represents MCNP inserts.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'\A(\d+)?i\Z', re.IGNORECASE)

    def __init__(self, n: int = None):
        """
        Initializes `Insert`.

        Parameters:
            n: Repetition number.

        Returns:
            `Insert`

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Insert` from MCNP.

        Parameters:
            source: MCNP inserts.

        Returns:
            `Insert`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Insert._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        n = int(tokens[1]) if tokens[1] else None

        return Insert(n)

    def to_mcnp(self):
        """
        Genereates MCNP inserts from `Insert`.

        Returns:
            MCNP inserts.
        """

        return f'{self.n or ""}i'


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


class Jump(_symbol.Nonterminal):
    """
    Represents MCNP jumps.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'\A(\d+)?j\Z', re.IGNORECASE)

    def __init__(self, n: int = None):
        """
        Initializes `Jump`.

        Parameters:
            n: Repetition number.

        Returns:
            `Jump`

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Jump` from MCNP.

        Parameters:
            source: MCNP jump.

        Returns:
            `Jump`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Jump._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        n = int(tokens[1]) if tokens[1] else None

        return Jump(n)

    def to_mcnp(self):
        """
        Genereates MCNP from `Jump`.

        Returns:
            MCNP jumps.
        """

        return f'{self.n if self.n is not None else ""}j'


class Log(Horizontal):
    """
    Represents MCNP logs.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'\A(\d+)?(log|ilog)\Z', re.IGNORECASE)

    def __init__(self, n: int = None):
        """
        Initializes `Log`.

        Parameters:
            n: Repetition number.

        Returns:
            `Log`

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Log` from MCNP.

        Parameters:
            source: MCNP log.

        Returns:
            `Log`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Log._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        n = int(tokens[1]) if tokens[1] else None

        return Log(n)

    def to_mcnp(self):
        """
        Genereates MCNP logs. from `Logs`.

        Returns:
            MCNP logs.
        """

        return f'{self.n or ""}log'
