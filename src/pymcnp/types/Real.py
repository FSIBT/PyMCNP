import re
import typing
import decimal

from . import _type
from .Horizontal import Horizontal
from .Horizontal import Repeat
from .Horizontal import Insert
from .Horizontal import Multiply
from .Horizontal import Jump
from .Horizontal import Log
from .. import errors


class Real(_type.Type):
    """
    Represents MCNP values or jump.

    Attributes:
        value: Real value or jump.
    """

    _REGEX = re.compile(r'\A(?:j|log|ilog|\d*m|i|r|(?:[-+0-9.eE][-+0-9.eEdD]*))\Z', re.IGNORECASE)

    def __init__(self, value: int | Horizontal):
        """
        Initializes `Real`.

        Parameters:
            value: Real or jump value.

        Returns:
            `Real`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[int] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Real` from MCNP.

        Parameters:
            source: MCNP real or jump.

        Returns:
            `Real`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        try:
            return Real(Repeat.from_mcnp(source))
        except errors.TypesError:
            pass

        try:
            return Real(Insert.from_mcnp(source))
        except errors.TypesError:
            pass

        try:
            return Real(Multiply.from_mcnp(source))
        except errors.TypesError:
            pass

        try:
            return Real(Jump.from_mcnp(source))
        except errors.TypesError:
            pass

        try:
            return Real(Log.from_mcnp(source))
        except errors.TypesError:
            pass

        source = re.sub(r'([-+0-9.]+)([-+])([0-9]+)', r'\1e\2\3', source)
        source = re.sub(r'[dD]', 'e', source)
        if source[0] == 'e':
            source = '1' + source

        try:
            return Real(decimal.Decimal(source))
        except decimal.InvalidOperation:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from `Real`.

        Returns:
            MCNP real.
        """

        return str(self.value)

    def __hash__(self):
        return hash(self.value)

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

    def __trunc__(self):
        return self.value.__trunc__()

    def __floor__(self):
        return self.value.__floor__()

    def __ceil__(self):
        return self.value.__ceil__()

    def __round__(self):
        return self.value.__round__()

    def __format__(self, spec):
        if match := re.match(r'\A(\d+)[.](\d+)a\Z', spec):
            e = self.value.adjusted() + int(match[2])

            s, d, _ = self.value.as_tuple()
            s = '-' if s else ' '
            d = ''.join(map(str, d[: int(match[1]) - int(match[2]) + 1]))

            if d == '0':
                return f'{s}0.{"0" * (int(match[1]))}E+00'
            else:
                d = int(match[2]) * '0' + d

                a = d[:1]
                b = d[1:]

                return f'{s}{a}.{b}E{e:+03}'
        else:
            return self.value.__format__(spec)

    def __lt__(a, b):
        if isinstance(b, Real):
            return a.value < b.value
        elif isinstance(b, decimal.Decimal):
            return a.value < b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value < decimal.Decimal(str(b))

    def __le__(a, b):
        if isinstance(b, Real):
            return a.value <= b.value
        elif isinstance(b, decimal.Decimal):
            return a.value <= b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value <= decimal.Decimal(str(b))

    def __eq__(a, b):
        if isinstance(b, Real):
            return a.value == b.value
        elif isinstance(b, decimal.Decimal):
            return a.value == b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value == decimal.Decimal(str(b))

    def __ne__(a, b):
        if isinstance(b, Real):
            return a.value != b.value
        elif isinstance(b, decimal.Decimal):
            return a.value != b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value != decimal.Decimal(str(b))

    def __gt__(a, b):
        if isinstance(b, Real):
            return a.value > b.value
        elif isinstance(b, decimal.Decimal):
            return a.value > b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value > decimal.Decimal(str(b))

    def __ge__(a, b):
        if isinstance(b, Real):
            return a.value >= b.value
        elif isinstance(b, decimal.Decimal):
            return a.value >= b
        elif isinstance(b, float) or isinstance(b, int):
            return a.value >= decimal.Decimal(str(b))

    def __add__(a, b):
        if isinstance(b, Real):
            return a.value.__add__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__add__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__add__(decimal.Decimal(str(b)))

    def __radd__(a, b):
        if isinstance(b, Real):
            return a.value.__radd__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__radd__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__radd__(decimal.Decimal(str(b)))

    def __sub__(a, b):
        if isinstance(b, Real):
            return a.value.__sub__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__sub__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__sub__(decimal.Decimal(str(b)))

    def __rsub__(a, b):
        if isinstance(b, Real):
            return a.value.__rsub__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__rsub__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__rsub__(decimal.Decimal(str(b)))

    def __mul__(a, b):
        if isinstance(b, Real):
            return a.value.__mul__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__mul__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__mul__(decimal.Decimal(str(b)))

    def __rmul__(a, b):
        if isinstance(b, Real):
            return a.value.__rmul__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__rmul__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__rmul__(decimal.Decimal(str(b)))

    def __mod__(a, b):
        if isinstance(b, Real):
            return a.value.__mod__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__mod__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__mod__(decimal.Decimal(str(b)))

    def __rmod__(a, b):
        if isinstance(b, Real):
            return a.value.__rmod__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__rmod__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__rmod__(decimal.Decimal(str(b)))

    def __divmod__(a, b):
        if isinstance(b, Real):
            return a.value.__divmod__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__divmod__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__divmod__(decimal.Decimal(str(b)))

    def __rdivmod__(a, b):
        if isinstance(b, Real):
            return a.value.__rdivmod__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__rdivmod__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__rdivmod__(decimal.Decimal(str(b)))

    def __pow__(a, b):
        if isinstance(b, Real):
            return a.value.__pow__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__pow__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__pow__(decimal.Decimal(str(b)))

    def __rpow__(a, b):
        if isinstance(b, Real):
            return a.value.__rpow__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__rpow__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__rpow__(decimal.Decimal(str(b)))

    def __floordiv__(a, b):
        if isinstance(b, Real):
            return a.value.__floordiv__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__floordiv__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__floordiv__(decimal.Decimal(str(b)))

    def __rfloordiv__(a, b):
        if isinstance(b, Real):
            return a.value.__rfloordiv__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__rfloordiv__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__rfloordiv__(decimal.Decimal(str(b)))

    def __truediv__(a, b):
        if isinstance(b, Real):
            return a.value.__truediv__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__truediv__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__truediv__(decimal.Decimal(str(b)))

    def __rtruediv__(a, b):
        if isinstance(b, Real):
            return a.value.__rtruediv__(b.value)
        elif isinstance(b, decimal.Decimal):
            return a.value.__rtruediv__(b)
        elif isinstance(b, float) or isinstance(b, int):
            return a.value.__rtruediv__(decimal.Decimal(str(b)))
