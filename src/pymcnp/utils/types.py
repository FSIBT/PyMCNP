import re
import typing
import decimal

from . import errors
from . import _parser
from . import _object


class Tuple(tuple, _object.McnpNonterminal):
    """
    Represents generic MCNP collections.

    Attributes:
        value: Tuple value.
    """

    def __init__(self, value: tuple):
        """
        Initializes ``Tuple``.

        Parameters:
            value: Tuple value.

        Returns:
            ``Tuple``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None or not (value != tuple()):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[tuple] = value

    @classmethod
    def from_mcnp(cls, source: str, T: typing.Type):
        """
        Generates ``Tuple`` from MCNP.

        Parameters:
            source: MCNP tuple.
            T: Inner type.

        Returns:
            ``Tuple``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        tokens = re.finditer(T._REGEX.pattern[2:-2], source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        return Tuple([T.from_mcnp(token[0]) for token in tokens])

    def to_mcnp(self):
        """
        Generates MCNP from ``Tuple``.

        Returns:
            MCNP for ``Tuple``.
        """

        return ' '.join(val.to_mcnp() if val is not None else '' for val in self.value)


class Repeat(_object.McnpNonterminal):
    """
    Represents MCNP repeats.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'\A(\d+)?r\Z')

    def __init__(self, n: int = None):
        """
        Initializes ``Repeat``.

        Parameters:
            n: Repetition number.

        Returns:
            ``Repeat``

        Raises
            McnpError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Repeat`` from MCNP.

        Parameters:
            source: MCNP repeats.

        Returns:
            ``Repeat``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Repeat._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        n = int(tokens[1]) if tokens[1] else None

        return Repeat(n)

    def to_mcnp(self):
        """
        Genereates MCNP repeats from ``Repeat``.

        Returns:
            MCNP repeats.
        """

        return f'{self.n or ''}r'


class Insert(_object.McnpNonterminal):
    """
    Represents MCNP inserts.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'\A(\d+)?i\Z')

    def __init__(self, n: int = None):
        """
        Initializes ``Insert``.

        Parameters:
            n: Repetition number.

        Returns:
            ``Insert``

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Insert`` from MCNP.

        Parameters:
            source: MCNP inserts.

        Returns:
            ``Insert``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Insert._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        n = int(tokens[1]) if tokens[1] else None

        return Insert(n)

    def to_mcnp(self):
        """
        Genereates MCNP inserts from ``Insert``.

        Returns:
            MCNP inserts.
        """

        return f'{self.n or ''}i'


class Multiply(_object.McnpNonterminal):
    """
    Represents MCNP multiply.

    Attributes:
        x: Multiply number.
    """

    _REGEX = re.compile(r'\A(\d+)m\Z')

    def __init__(self, x: float):
        """
        Initializes ``Multiply``.

        Parameters:
            x: Multiply number.

        Returns:
            ``Multiply``

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if x is not None and not x:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, x)

        self.x: typing.Final[float] = x

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Multiply`` from MCNP.

        Parameters:
            source: MCNP multiply.

        Returns:
            ``Multiply``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Multiply._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        x = int(tokens[1])

        return Multiply(x)

    def to_mcnp(self):
        """
        Genereates MCNP multiplies. from ``Multiply``.

        Returns:
            MCNP multiply.
        """

        return f'{self.x}m'


class Jump(_object.McnpNonterminal):
    """
    Represents MCNP jumps.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'\A(\d+)?j\Z')

    def __init__(self, n: int = None):
        """
        Initializes ``Jump``.

        Parameters:
            n: Repetition number.

        Returns:
            ``Jump``

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Jump`` from MCNP.

        Parameters:
            source: MCNP jump.

        Returns:
            ``Jump``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Jump._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        n = int(tokens[1]) if tokens[1] else None

        return Jump(n)

    def to_mcnp(self):
        """
        Genereates MCNP from ``Jump``.

        Returns:
            MCNP jumps.
        """

        return f'{self.n or ""}j'


class Log(_object.McnpNonterminal):
    """
    Represents MCNP logs.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'\A(\d+)?(log|ilog)\Z')

    def __init__(self, n: int = None):
        """
        Initializes ``Log``.

        Parameters:
            n: Repetition number.

        Returns:
            ``Log``

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Log`` from MCNP.

        Parameters:
            source: MCNP log.

        Returns:
            ``Log``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Log._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        n = int(tokens[1]) if tokens[1] else None

        return Log(n)

    def to_mcnp(self):
        """
        Genereates MCNP logs. from ``Logs``.

        Returns:
            MCNP logs.
        """

        return f'{self.n or ''}log'


class Integer(_object.McnpNonterminal):
    """
    Represents MCNP values or jump.

    Attributes:
        value: Integer value or jump.
    """

    _REGEX = re.compile(r'\A(?:\d*j|\d*log|\d*ilog|\d*m|\d*i|\d*r|[-+0-9.eEdD]+)\Z')

    def __init__(self, value: int | Repeat | Insert | Multiply | Jump | Log):
        """
        Initializes ``Integer``.

        Parameters:
            value: Integer or jump value.

        Returns:
            ``Integer``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[int] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Integer`` from MCNP.

        Parameters:
            source: MCNP value or jump.

        Returns:
            ``Integer``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Integer(Repeat.from_mcnp(source))
        except Exception:
            pass

        try:
            return Integer(Insert.from_mcnp(source))
        except Exception:
            pass

        try:
            return Integer(Multiply.from_mcnp(source))
        except Exception:
            pass

        try:
            return Integer(Jump.from_mcnp(source))
        except Exception:
            pass

        try:
            return Integer(Log.from_mcnp(source))
        except Exception:
            pass

        source = re.sub(r'd', 'e', source)
        if source[0] == 'e':
            source = '1' + source

        try:
            return Integer(int(float(source)))
        except Exception:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Integer``.

        Returns:
            MCNP value.
        """

        return str(self.value)

    def __lt__(a, b):
        if isinstance(b, Integer):
            return a.value.__lt__(b.value)
        elif isinstance(b, int):
            return a.value.__lt__(b)
        else:
            return a.value.__lt__(b)

    def __le__(a, b):
        if isinstance(b, Integer):
            return a.value.__le__(b.value)
        elif isinstance(b, int):
            return a.value.__le__(b)
        else:
            return a.value.__le__(b)

    def __eq__(a, b):
        if isinstance(b, Integer):
            return a.value.__eq__(b.value)
        elif isinstance(b, int):
            return a.value.__eq__(b)
        else:
            return a.value.__eq__(b)

    def __ne__(a, b):
        if isinstance(b, Integer):
            return a.value.__ne__(b.value)
        elif isinstance(b, int):
            return a.value.__ne__(b)
        else:
            return a.value.__ne__(b)

    def __gt__(a, b):
        if isinstance(b, Integer):
            return a.value.__gt__(b.value)
        elif isinstance(b, int):
            return a.value.__gt__(b)
        else:
            return a.value.__gt__(b)

    def __ge__(a, b):
        if isinstance(b, Integer):
            return a.value.__ge__(b.value)
        elif isinstance(b, int):
            return a.value.__ge__(b)
        else:
            return a.value.__ge__(b)

    def __hash__(self):
        return hash(self.value)

    def __add__(a, b):
        if isinstance(b, Integer):
            return a.value.__add__(b.value)
        elif isinstance(b, int):
            return a.value.__add__(b)
        else:
            return a.value.__add__(b)

    def __radd__(a, b):
        if isinstance(b, Integer):
            return a.value.__radd__(b.value)
        elif isinstance(b, int):
            return a.value.__radd__(b)
        else:
            return a.value.__radd__(b)

    def __sub__(a, b):
        if isinstance(b, Integer):
            return a.value.__sub__(b.value)
        elif isinstance(b, int):
            return a.value.__sub__(b)
        else:
            return a.value.__sub__(b)

    def __rsub__(a, b):
        if isinstance(b, Integer):
            return a.value.__rsub__(b.value)
        elif isinstance(b, int):
            return a.value.__rsub__(b)
        else:
            return a.value.__rsub__(b)

    def __mul__(a, b):
        if isinstance(b, Integer):
            return a.value.__mul__(b.value)
        elif isinstance(b, int):
            return a.value.__mul__(b)
        else:
            return a.value.__mul__(b)

    def __rmul__(a, b):
        if isinstance(b, Integer):
            return a.value.__rmul__(b.value)
        elif isinstance(b, int):
            return a.value.__rmul__(b)
        else:
            return a.value.__rmul__(b)

    def __mod__(a, b):
        if isinstance(b, Integer):
            return a.value.__mod__(b.value)
        elif isinstance(b, int):
            return a.value.__mod__(b)
        else:
            return a.value.__mod__(b)

    def __rmod__(a, b):
        if isinstance(b, Integer):
            return a.value.__rmod__(b.value)
        elif isinstance(b, int):
            return a.value.__rmod__(b)
        else:
            return a.value.__rmod__(b)

    def __divmod__(a, b):
        if isinstance(b, Integer):
            return a.value.__divmod__(b.value)
        elif isinstance(b, int):
            return a.value.__divmod__(b)
        else:
            return a.value.__divmod__(b)

    def __rdivmod__(a, b):
        if isinstance(b, Integer):
            return a.value.__rdivmod__(b.value)
        elif isinstance(b, int):
            return a.value.__rdivmod__(b)
        else:
            return a.value.__rdivmod__(b)

    def __pow__(a, b):
        if isinstance(b, Integer):
            return a.value.__pow__(b.value)
        elif isinstance(b, int):
            return a.value.__pow__(b)
        else:
            return a.value.__pow__(b)

    def __rpow__(a, b):
        if isinstance(b, Integer):
            return a.value.__rpow__(b.value)
        elif isinstance(b, int):
            return a.value.__rpow__(b)
        else:
            return a.value.__rpow__(b)

    def __neg__(self):
        return self.value.__neg__()

    def __pos__(self):
        return self.value.__pos__()

    def __abs__(self):
        return self.value.__abs__()

    def __bool__(self):
        return self.value.__bool__()

    def __int__(self):
        return self.value.__int__()

    def __float__(self):
        return self.value.__float__()

    def __floordiv__(a, b):
        if isinstance(b, Integer):
            return a.value.__floordiv__(b.value)
        elif isinstance(b, int):
            return a.value.__floordiv__(b)
        else:
            return a.value.__floordiv__(b)

    def __rfloordiv__(a, b):
        if isinstance(b, Integer):
            return a.value.__rfloordiv__(b.value)
        elif isinstance(b, int):
            return a.value.__rfloordiv__(b)
        else:
            return a.value.__rfloordiv__(b)

    def __truediv__(a, b):
        if isinstance(b, Integer):
            return a.value.__truediv__(b.value)
        elif isinstance(b, int):
            return a.value.__truediv__(b)
        else:
            return a.value.__truediv__(b)

    def __rtruediv__(a, b):
        if isinstance(b, Integer):
            return a.value.__rtruediv__(b.value)
        elif isinstance(b, int):
            return a.value.__rtruediv__(b)
        else:
            return a.value.__rtruediv__(b)

    def __trunc__(self):
        return self.value.__trunc__()

    def __floor__(self):
        return self.value.__floor__()

    def __ceil__(self):
        return self.value.__ceil__()

    def __round__(self):
        return self.value.__round__()


class Real(_object.McnpNonterminal):
    """
    Represents MCNP values or jump.

    Attributes:
        value: Real value or jump.
    """

    _REGEX = re.compile(r'\A(?:\d*j|\d*log|\d*ilog|\d*m|\d*i|\d*r|[-+0-9.eEdD]+)\Z')

    def __init__(self, value: int | Repeat | Insert | Multiply | Jump | Log):
        """
        Initializes ``Real``.

        Parameters:
            value: Real or jump value.

        Returns:
            ``Real``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[int] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Real`` from MCNP.

        Parameters:
            source: MCNP real or jump.

        Returns:
            ``Real``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Real(Repeat.from_mcnp(source))
        except Exception:
            pass

        try:
            return Real(Insert.from_mcnp(source))
        except Exception:
            pass

        try:
            return Real(Multiply.from_mcnp(source))
        except Exception:
            pass

        try:
            return Real(Jump.from_mcnp(source))
        except Exception:
            pass

        try:
            return Real(Log.from_mcnp(source))
        except Exception:
            pass

        source = re.sub(r'd', 'e', source)
        if source[0] == 'e':
            source = '1' + source

        try:
            return Real(decimal.Decimal(source))
        except Exception:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Real``.

        Returns:
            MCNP real.
        """

        return str(self.value)

    def __lt__(a, b):
        if isinstance(b, Real):
            return a.value < b.value
        elif isinstance(b, decimal.Decimal):
            return a.value < b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value < decimal.Decimal(str(b))
        else:
            return a.value.__lt__(b)

    def __le__(a, b):
        if isinstance(b, Real):
            return a.value <= b.value
        elif isinstance(b, decimal.Decimal):
            return a.value <= b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value <= decimal.Decimal(str(b))
        else:
            return a.value.__le__(b)

    def __eq__(a, b):
        if isinstance(b, Real):
            return a.value == b.value
        elif isinstance(b, decimal.Decimal):
            return a.value == b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value == decimal.Decimal(str(b))
        else:
            return a.value.__eq__(b)

    def __ne__(a, b):
        if isinstance(b, Real):
            return a.value != b.value
        elif isinstance(b, decimal.Decimal):
            return a.value != b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value != decimal.Decimal(str(b))
        else:
            return a.value.__ne__(b)

    def __gt__(a, b):
        if isinstance(b, Real):
            return a.value > b.value
        elif isinstance(b, decimal.Decimal):
            return a.value > b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value > decimal.Decimal(str(b))
        else:
            return a.value.__gt__(b)

    def __ge__(a, b):
        if isinstance(b, Real):
            return a.value >= b.value
        elif isinstance(b, decimal.Decimal):
            return a.value >= b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value >= decimal.Decimal(str(b))
        else:
            return a.value.__ge__(b)

    def __hash__(self):
        return hash(self.value)

    def __add__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__add_(b)

    def __radd__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__radd(b)

    def __sub__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__sub_(b)

    def __rsub__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__rsub(b)

    def __mul__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__mul_(b)

    def __rmul__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__rmul(b)

    def __mod__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__mod_(b)

    def __rmod__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__rmod(b)

    def __divmod__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__divm(b)

    def __rdivmod__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__rdiv(b)

    def __pow__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__pow_(b)

    def __rpow__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__rpow(b)

    def __neg__(self):
        return self.value.__neg__()

    def __pos__(self):
        return self.value.__pos__()

    def __abs__(self):
        return self.value.__abs__()

    def __bool__(self):
        return self.value.__bool__()

    def __int__(self):
        return self.value.__int__()

    def __float__(self):
        return self.value.__float__()

    def __floordiv__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__floo(b)

    def __rfloordiv__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__rflo(b)

    def __truediv__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__true(b)

    def __rtruediv__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))
        else:
            return a.__rtru(b)

    def __trunc__(self):
        return self.value.__trunc__()

    def __floor__(self):
        return self.value.__floor__()

    def __ceil__(self):
        return self.value.__ceil__()

    def __round__(self):
        return self.value.__round__()


class String(str, _object.McnpNonterminal):
    """
    Represents MCNP strings.

    Attributes:
        value: String value.
    """

    _REGEX = re.compile(r'\A\S+\Z')

    def __init__(self, value: str):
        """
        Initializes ``String``.

        Parameters:
            value: String value.

        Returns:
            ``String``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[str] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``String`` from MCNP.

        Praameters:
            source: MCNP string.

        Returns:
            ``String``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        return String(source)

    def to_mcnp(self):
        """
        Generates MCNP from ``String``.

        Returns:
            MCNP string.
        """

        return self


class DistributionNumber(_object.McnpNonterminal):
    """
    Represents MCNP distribution numbers.

    Attributes:
        n: Distribution identifier.
    """

    _REGEX = re.compile(r'\A[dD]\d+\Z')

    def __init__(self, n: int):
        """
        Initializes ``DistributionNumber``.

        Parameters:
            n: Distribution identifier.

        Returns:
            ``DistributionNumber``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if n is None or not (1 <= n <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DistributionNumber`` from MCNP.

        Parameters:
            source: MCNP for ``DistributionNumber``.

        Returns:
            ``DistributionNumber``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        match = re.match(r'\A[dD](\d|\d\d|\d\d\d)\Z', source)

        if match is None:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        return DistributionNumber(int(match[1]))

    def to_mcnp(self):
        """
        Generates MCNP from ``DistributionNumber``.

        Returns:
            MCNP for ``DistributionNumber``.
        """

        return f'd{self.n}'


class EmbeddedDistributionNumber(_object.McnpNonterminal):
    """
    Represents MCNP embedded distribution numbers.

    Attributes:
        numbers: Distribution numbers.
    """

    _REGEX = re.compile(r'\A[dD0-1<]+\Z')

    def __init__(self, numbers: tuple[DistributionNumber]):
        """
        Initializes ``EmbeddedDistributionNumber``.

        Parameters:
            numbers: Distribution numbers.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if numbers is None or None in numbers:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, numbers)

        self.numbers: typing.Final[tuple[DistributionNumber]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeddedDistributionNumber`` from MCNP.

        Parameters:
            source: MCNP for ``EmbeddedDistributionNumber``.

        Returns:
            ``EmbeddedDistributionNumber`` object.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return EmbeddedDistributionNumber(Tuple([DistributionNumber.from_mcnp(token) for token in source.split('>')]))
        except Exception:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``EmbeddedDistributionNumber``.

        Returns:
            MCNP for ``EmbeddedDistributionNumber``.
        """

        return '>'.join(number.to_mcnp() for number in self.numbers)


class Zaid(_object.McnpNonterminal):
    """
    Represents MCNP nuclide information numbers.

    Attributes:
        z: Atomic number.
        a: Mass number.
        abx: Cross-section evaluation & class information.
    """

    _REGEX = re.compile(r'\A(\d{1,3})(\d\d\d)(?:[.](\S+))?\Z')

    def __init__(self, z: int, a: int, abx: str = None):
        """
        Initializes ``Zaid``.

        Parameters:
            z: ZAID atomic number.
            a: ZAID mass number.
            abx: ZAID cross-section evaluation & class information.

        Returns:
            ``Zaid``.

        Raises:
            McnpError: SEMANTICS_TYPE.
            McnpError: SEMANTICS_TYPE.
            McnpError: SEMANTICS_TYPE.
        """

        if z is None or not (000 <= z <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, z)

        if a is None or not (000 <= a <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, a)

        self.z: typing.Final[int] = z
        self.a: typing.Final[int] = a
        self.abx: typing.Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Zaid`` from MCNP.

        Parameters:
            source: MCNP for ``Zaid``.

        Returns:
            ``Zaid`` object.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Zaid._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        return Zaid(int(tokens[1]), int(tokens[2]), tokens[3])

    def to_mcnp(self) -> str:
        """
        Generates MCNP from ``Zaid``.

        Returns:
            MCNP Zaid.
        """

        if self.abx:
            return f'{self.z:03}{self.a:03}.{self.abx}'
        else:
            return f'{self.z:03}{self.a:03}'


class Particle(_object.McnpTerminal):
    """
    Represents MCNP particle designators.
    """

    NEUTRON = 'n'
    ANTI_NEUTRON = 'q'
    PHOTON = 'p'
    ELECTRON = 'e'
    POSITRON = 'f'
    NEGATIVE_MUON = '|'
    POSITIVE_MUON = '!'
    ELECTRON_NEUTRINO = 'u'
    ANTI_ELECTRON_NEUTRINO = '<'
    MUON_NEUTRINO = 'v'
    ANTI_MUON_MEUTRINO = '>'
    PROTON = 'h'
    ANTI_PROTON = 'g'
    LAMBDA_BARYON = 'l'
    ANTI_LAMBDA_BARYON = 'b'
    POSITIVE_SIGMA_BARYON = '+'
    ANTI_POSITIVE_SIGMA_BARYON = '_'
    NEGATIVE_SIGMA_BARYON = '-'
    ANTI_NEGATIVE_SIGMA_BARYON = '~'
    CASCADE = 'x'
    ANTI_CASCADE = 'c'
    NEGATIVE_CASCADE = 'y'
    POSITIVE_CASCADE = 'w'
    OMEGA_BARYON = 'o'
    ANTI_OMEGA_BARYON = '@'
    POSITIVE_PION = '/'
    NEGATIVE_PION = '*'
    NEUTRAL_PION = 'z'
    POSITIVE_KAON = 'k'
    NEGATIVE_KAON = '?'
    SHORT_KAON = '%'
    LONG_KAON = '^'
    DEUTERON = 'd'
    TRITON = 't'
    HELION = 's'
    ALPHA = 'a'
    HEAVY_IONS = '#'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Particle`` from MCNP.

        Parameters:
            source: MCNP for ``Particle``.

        Returns:
            ``Particle``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Particle(source)
        except Exception:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Particle``.

        Returns:
            MCNP particle.
        """

        return str(self.value)


class Designator(_object.McnpNonterminal):
    """
    Represents MCNP particle designators.

    Attributes:
        particles: Designator particles.
    """

    _REGEX = re.compile(r'\A[nqpef|!u<v>hglb+_-~xcywo@/*zk?%^dtsa#]((?:,)[nqpef|!u<v>hglb+_-~xcywo@/*zk?%^dtsa#])*\Z')

    def __init__(self, particles: tuple[Particle]):
        """
        Initializes ``Designator``.

        Parameters:
            particles: Tuple of particles.

        Returns:
            ``Designator``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if particles is None or None in particles:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, particles)

        self.particles: typing.Final[tuple[Particle]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Designator`` from MCNP.

        Parameters:
            source: MCNP for ``Designator``.

        Returns:
            ``Designator``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Designator(tuple(Particle.from_mcnp(token) for token in source.split(',')))
        except Exception:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self) -> str:
        """
        Generates MCNP from ``Designator``.

        Returns:
            MCNP designator.
        """

        return ','.join(particle.to_mcnp() for particle in self.particles)


class Geometry(_object.McnpNonterminal):
    """
    Represents MCNP geometries.

    Attributes:
        infix: Geometry infix formula.
    """

    _REGEX = re.compile(r'\A(.+)\Z')

    def __init__(self, infix: String):
        """
        Initializes ``Geometry``.

        Parameters:
            infix: Geometry infix formula.

        Returns:
            ``Geometry``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        temp = re.sub(r' 0+', '', infix)
        temp = re.sub(r' +', ' ', temp)
        temp = re.sub(r'\+', '', temp)
        temp = re.sub(r' ?: ?', '+', temp)
        temp = re.sub(r' ', '*', temp)
        temp = re.sub(r'#', '-', temp)
        temp = re.sub(r'\+-', '-', temp)
        temp = re.sub(r'(\d)\(', r'\1*(', temp)

        for number in re.split(r'[*#:+ ()-]+', temp):
            if number and not re.match(r'\d+(?:[.][1-8])?', number):
                raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, infix)

        try:
            eval(temp)
        except Exception:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, infix)

        self.infix: typing.typing.Final[String] = infix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Geometry`` from INP.

        Parameters:
            INP for ``Geometry``.

        Returns:
            ``Geometry``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Geometry._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        infix = String.from_mcnp(tokens[1])

        return Geometry(infix)

    def to_mcnp(self):
        """
        Generates INP from ``Geometry``.

        Returns:
            INP for ``Geometry``.
        """

        return self.infix

    def __and__(a, b):
        """
        Unites ``Geometry``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``Geometry`` union.
        """

        return Geometry(infix=f'({a.infix}):({b.infix})')

    def __or__(a, b):
        """
        Intersects ``Geometry``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``Geometry`` intersection.
        """

        return Geometry(infix=f'({a.infix}) ({b.infix})')

    def __neg__(self):
        """
        Negatives ``Geometry``.

        Returns:
            ``Geometry`` negative.
        """

        return Geometry(infix=f'-({self.infix})')

    def __pos__(self):
        """
        Positives ``Geometry``.

        Returns:
            ``Geometry`` positive.
        """

        return Geometry(infix=f'+({self.infix})')

    def __invert__(self):
        """
        Inverts ``Geometry``.

        Returns:
            ``Geometry`` complement.
        """

        return Geometry(infix=f'#({self.infix})')


class Substance(_object.McnpNonterminal):
    """
    Represents MCNP substances.

    Attributes:
        zaid: Zaid alias for nuclide.
        weight_ratio: Atomic weight ratios.
    """

    _REGEX = re.compile(r'\A(\S+) (\S+)\Z')

    def __init__(self, zaid: Zaid, weight_ratio: Real):
        """
        Initializes ``Substance``.

        Parameters:
            zaid: Zaid alias for nuclide.
            weight_ratio: Atomic weight ratios.

        Returns:
            ``Substance``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if zaid is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, zaid)
        if weight_ratio is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, weight_ratio)

        self.zaid: typing.Final[Zaid] = zaid
        self.weight_ratio: typing.Final[Real] = weight_ratio

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Substance`` from MCNP.

        Parameters:
            MCNP for ``Substance``.

        Returns:
            ``Substance``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Substance._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, tokens)

        zaid = Zaid.from_mcnp(tokens[1])
        weight_ratio = Real.from_mcnp(tokens[2])

        return Substance(zaid, weight_ratio)

    def to_mcnp(self):
        """
        Generates INP from ``Substance``.

        Returns:
            INP for ``Substance``.
        """

        return f'{self.zaid} {self.weight_ratio}'


class Transformation_0(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        yx: Transformation rotation matrix yx-entry.
        yy: Transformation rotation matrix yy-entry.
        yz: Transformation rotation matrix yz-entry.
        zx: Transformation rotation matrix zx-entry.
        zy: Transformation rotation matrix zy-entry.
        zz: Transformation rotation matrix zz-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(
        r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z'
    )

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        yx: Real,
        yy: Real,
        yz: Real,
        zx: Real,
        zy: Real,
        zz: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_0``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            yx: Transformation rotation matrix yx-entry.
            yy: Transformation rotation matrix yy-entry.
            yz: Transformation rotation matrix yz-entry.
            zx: Transformation rotation matrix zx-entry.
            zy: Transformation rotation matrix zy-entry.
            zz: Transformation rotation matrix zz-entry.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_0``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xz)
        if yx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yx)
        if yy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yy)
        if yz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yz)
        if zx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, zx)
        if zy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, zy)
        if zz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, zz)
        if m is not None and m.value not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.yx: typing.Final[Real] = yx
        self.yy: typing.Final[Real] = yy
        self.yz: typing.Final[Real] = yz
        self.zx: typing.Final[Real] = zx
        self.zy: typing.Final[Real] = zy
        self.zz: typing.Final[Real] = zz
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_0`` from INP.

        Parameters:
            INP for ``Transformation_0``.

        Returns:
            ``Transformation_0``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_0._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        yx = Real.from_mcnp(tokens[7])
        yy = Real.from_mcnp(tokens[8])
        yz = Real.from_mcnp(tokens[9])
        zx = Real.from_mcnp(tokens[10])
        zy = Real.from_mcnp(tokens[11])
        zz = Real.from_mcnp(tokens[12])
        m = Real.from_mcnp(tokens[13]) if tokens[13] else None

        return Transformation_0(o1, o2, o3, xx, xy, xz, yx, yy, yz, zx, zy, zz, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_0``.

        Returns:
            INP for ``Transformation_0``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.yz} {self.zx} {self.zy} {self.zz} {self.m or ""}'


class Transformation_1(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        yx: Transformation rotation matrix yx-entry.
        yy: Transformation rotation matrix yy-entry.
        yz: Transformation rotation matrix yz-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z')

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        yx: Real,
        yy: Real,
        yz: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_1``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            yx: Transformation rotation matrix yx-entry.
            yy: Transformation rotation matrix yy-entry.
            yz: Transformation rotation matrix yz-entry.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_1``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xz)
        if yx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yx)
        if yy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yy)
        if yz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yz)
        if m is not None and m.value not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.yx: typing.Final[Real] = yx
        self.yy: typing.Final[Real] = yy
        self.yz: typing.Final[Real] = yz
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_1`` from INP.

        Parameters:
            INP for ``Transformation_1``.

        Returns:
            ``Transformation_1``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_1._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        yx = Real.from_mcnp(tokens[7])
        yy = Real.from_mcnp(tokens[8])
        yz = Real.from_mcnp(tokens[9])
        m = Real.from_mcnp(tokens[10]) if tokens[10] else None

        return Transformation_1(o1, o2, o3, xx, xy, xz, yx, yy, yz, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_1``.

        Returns:
            INP for ``Transformation_1``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.yz} {self.m or ""}'


class Transformation_2(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        yx: Transformation rotation matrix yx-entry.
        yy: Transformation rotation matrix yy-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z')

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        yx: Real,
        yy: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_2``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            yx: Transformation rotation matrix yx-entry.
            yy: Transformation rotation matrix yy-entry.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_2``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xz)
        if yx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yx)
        if yy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yy)
        if m is not None and m.value not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.yx: typing.Final[Real] = yx
        self.yy: typing.Final[Real] = yy
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_2`` from INP.

        Parameters:
            INP for ``Transformation_2``.

        Returns:
            ``Transformation_2``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_2._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        yx = Real.from_mcnp(tokens[7])
        yy = Real.from_mcnp(tokens[8])
        m = Real.from_mcnp(tokens[9]) if tokens[9] else None

        return Transformation_2(o1, o2, o3, xx, xy, xz, yx, yy, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_2``.

        Returns:
            INP for ``Transformation_2``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.m or ""}'


class Transformation_3(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z')

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_3``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_3``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xz)
        if m is not None and m.value not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_3`` from INP.

        Parameters:
            INP for ``Transformation_3``.

        Returns:
            ``Transformation_3``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_3._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        m = Real.from_mcnp(tokens[7]) if tokens[7] else None

        return Transformation_3(o1, o2, o3, xx, xy, xz, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_3``.

        Returns:
            INP for ``Transformation_3``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.m or ""}'


class Transformation_4(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z')

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_4``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_4``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if m is not None and m.value not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_4`` from INP.

        Parameters:
            INP for ``Transformation_4``.

        Returns:
            ``Transformation_4``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_4._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        m = Real.from_mcnp(tokens[4]) if tokens[4] else None

        return Transformation_4(o1, o2, o3, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_4``.

        Returns:
            INP for ``Transformation_4``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.m or ""}'


class Index(_object.McnpNonterminal):
    """
    Represents INP lattice index entries.

    Attributes:
        lower: Lower index.
        upper: Upper index.
    """

    _REGEX = re.compile(r'\A(\S+):(\S+)\Z')

    def __init__(self, lower: Integer, upper: Integer):
        """
        Initializes ``Index``.

        Parameters:
            lower: Lower index.
            upper: Upper index.

        Returns:
            ``Index``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if lower is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, lower)
        if upper is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, upper)

        self.lower: typing.Final[Integer] = lower
        self.upper: typing.Final[Integer] = upper

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Index`` from INP.

        Parameters:
            INP for ``Index``.

        Returns:
            ``Index``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Index._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        lower = Integer.from_mcnp(tokens[1])
        upper = Integer.from_mcnp(tokens[2])

        return Index(lower, upper)

    def to_mcnp(self):
        """
        Generates INP from ``Index``.

        Returns:
            INP for ``Index``.
        """

        return f'{self.lower}:{self.upper}'
