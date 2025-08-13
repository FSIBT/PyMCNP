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


class Integer(_type.Type):
    """
    Represents MCNP values or jump.

    Attributes:
        value: Integer value or jump.
    """

    _REGEX = re.compile(r'\A(?:j|log|ilog|\d*m|i|r|(?:[-+0-9.eE][-+0-9.eEdD]*))\Z', re.IGNORECASE)

    def __init__(self, value: int | Horizontal):
        """
        Initializes `Integer`.

        Parameters:
            value: Integer or jump value.

        Returns:
            `Integer`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[int] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Integer` from MCNP.

        Parameters:
            source: MCNP value or jump.

        Returns:
            `Integer`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        try:
            return Integer(Repeat.from_mcnp(source))
        except errors.TypesError:
            pass

        try:
            return Integer(Insert.from_mcnp(source))
        except errors.TypesError:
            pass

        try:
            return Integer(Multiply.from_mcnp(source))
        except errors.TypesError:
            pass

        try:
            return Integer(Jump.from_mcnp(source))
        except errors.TypesError:
            pass

        try:
            return Integer(Log.from_mcnp(source))
        except errors.TypesError:
            pass

        source = re.sub(r'([-+0-9.]+)([-+])([0-9]+)', r'\1e\2\3', source)
        source = re.sub(r'[dD]', 'e', source)
        if source[0] == 'e':
            source = '1' + source

        try:
            return Integer(int(decimal.Decimal(source)))
        except decimal.InvalidOperation:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from `Integer`.

        Returns:
            MCNP value.
        """

        return str(self.value)

    def __hash__(self):
        return self.value.__hash__()

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
        return self.value.__format__(spec)

    def __lt__(a, b):
        if isinstance(b, Integer):
            return a.value.__lt__(b.value)
        elif isinstance(b, int):
            return a.value.__lt__(b)

    def __le__(a, b):
        if isinstance(b, Integer):
            return a.value.__le__(b.value)
        elif isinstance(b, int):
            return a.value.__le__(b)

    def __eq__(a, b):
        if isinstance(b, Integer):
            return a.value.__eq__(b.value)
        elif isinstance(b, int):
            return a.value.__eq__(b)

    def __ne__(a, b):
        if isinstance(b, Integer):
            return a.value.__ne__(b.value)
        elif isinstance(b, int):
            return a.value.__ne__(b)

    def __gt__(a, b):
        if isinstance(b, Integer):
            return a.value.__gt__(b.value)
        elif isinstance(b, int):
            return a.value.__gt__(b)

    def __ge__(a, b):
        if isinstance(b, Integer):
            return a.value.__ge__(b.value)
        elif isinstance(b, int):
            return a.value.__ge__(b)

    def __add__(a, b):
        if isinstance(b, Integer):
            return a.value.__add__(b.value)
        elif isinstance(b, int):
            return a.value.__add__(b)

    def __radd__(a, b):
        if isinstance(b, Integer):
            return a.value.__radd__(b.value)
        elif isinstance(b, int):
            return a.value.__radd__(b)

    def __sub__(a, b):
        if isinstance(b, Integer):
            return a.value.__sub__(b.value)
        elif isinstance(b, int):
            return a.value.__sub__(b)

    def __rsub__(a, b):
        if isinstance(b, Integer):
            return a.value.__rsub__(b.value)
        elif isinstance(b, int):
            return a.value.__rsub__(b)

    def __mul__(a, b):
        if isinstance(b, Integer):
            return a.value.__mul__(b.value)
        elif isinstance(b, int):
            return a.value.__mul__(b)

    def __rmul__(a, b):
        if isinstance(b, Integer):
            return a.value.__rmul__(b.value)
        elif isinstance(b, int):
            return a.value.__rmul__(b)

    def __mod__(a, b):
        if isinstance(b, Integer):
            return a.value.__mod__(b.value)
        elif isinstance(b, int):
            return a.value.__mod__(b)

    def __rmod__(a, b):
        if isinstance(b, Integer):
            return a.value.__rmod__(b.value)
        elif isinstance(b, int):
            return a.value.__rmod__(b)

    def __divmod__(a, b):
        if isinstance(b, Integer):
            return a.value.__divmod__(b.value)
        elif isinstance(b, int):
            return a.value.__divmod__(b)

    def __rdivmod__(a, b):
        if isinstance(b, Integer):
            return a.value.__rdivmod__(b.value)
        elif isinstance(b, int):
            return a.value.__rdivmod__(b)

    def __pow__(a, b):
        if isinstance(b, Integer):
            return a.value.__pow__(b.value)
        elif isinstance(b, int):
            return a.value.__pow__(b)

    def __rpow__(a, b):
        if isinstance(b, Integer):
            return a.value.__rpow__(b.value)
        elif isinstance(b, int):
            return a.value.__rpow__(b)

    def __floordiv__(a, b):
        if isinstance(b, Integer):
            return a.value.__floordiv__(b.value)
        elif isinstance(b, int):
            return a.value.__floordiv__(b)

    def __rfloordiv__(a, b):
        if isinstance(b, Integer):
            return a.value.__rfloordiv__(b.value)
        elif isinstance(b, int):
            return a.value.__rfloordiv__(b)

    def __truediv__(a, b):
        if isinstance(b, Integer):
            return a.value.__truediv__(b.value)
        elif isinstance(b, int):
            return a.value.__truediv__(b)

    def __rtruediv__(a, b):
        if isinstance(b, Integer):
            return a.value.__rtruediv__(b.value)
        elif isinstance(b, int):
            return a.value.__rtruediv__(b)
