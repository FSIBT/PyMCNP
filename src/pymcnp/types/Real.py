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

    _REGEX = re.compile(r'\A(?:\d*j|\d*log|\d*ilog|\d*m|\d*i|\d*r|[-+0-9.eEdD]+)\Z')

    def __init__(self, value: int | Horizontal):
        """
        Initializes ``Real``.

        Parameters:
            value: Real or jump value.

        Returns:
            ``Real``.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, value)

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

        source = re.sub(r'd', 'e', source)
        if source[0] == 'e':
            source = '1' + source

        try:
            return Real(decimal.Decimal(source))
        except errors.TypesError:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

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
