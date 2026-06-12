from __future__ import annotations

import re
import typing
import decimal

from ..Literal import Literal


class Real(Literal):
    """
    Represents real literals.
    """

    _pattern = re.compile(r'([-+]?(?:(?:(?:\d*\.\d+|\d+\.?|\d+)(?:[eE][-+]?\d+)?))|(?:[eE][-+]?\d+))([\s\S]*)', re.IGNORECASE)

    def __hash__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__hash__()

    def __neg__(self) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__neg__()))

    def __pos__(self) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__pos__()))

    def __abs__(self) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__abs__()))

    def __bool__(self) -> bool:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__bool__()

    def __int__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__int__()

    def __float__(self) -> float:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__float__()

    def __trunc__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__trunc__()

    def __floor__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__floor__()

    def __ceil__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__ceil__()

    def __round__(self, ndigits: int = 0) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__round__(ndigits)))

    def __lt__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__lt__(decimal.Decimal(other))
        else:
            return str.__lt__(self, other)

    def __le__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__le__(decimal.Decimal(other))
        else:
            return str.__le__(self, other)

    def __eq__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__eq__(decimal.Decimal(other))
        else:
            return str.__eq__(self, other)

    def __ne__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__ne__(decimal.Decimal(other))
        else:
            return str.__ne__(self, other)

    def __gt__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__gt__(decimal.Decimal(other))
        else:
            return str.__gt__(self, other)

    def __ge__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__ge__(decimal.Decimal(other))
        else:
            return str.__ge__(self, other)

    def __add__(self, other: typing.Any, /) -> Real | str:  # ty: ignore[invalid-method-override]
        if isinstance(other, (Real, Integer, int, float, decimal.Decimal)):
            return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__add__(decimal.Decimal(other))))
        else:
            return str.__add__(self, other)

    def __radd__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__radd__(decimal.Decimal(other))))

    def __sub__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__sub__(decimal.Decimal(other))))

    def __rsub__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rsub__(decimal.Decimal(other))))
        ...

    def __mul__(self, other: typing.Any, /) -> Real:  # ty: ignore[invalid-method-override]
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__mul__(decimal.Decimal(other))))

    def __rmul__(self, other: typing.Any, /) -> Real:  # ty: ignore[invalid-method-override]
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rmul__(decimal.Decimal(other))))

    def __mod__(self, other: typing.Any, /) -> Real:  # ty: ignore[invalid-method-override]
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__mod__(decimal.Decimal(other))))

    def __rmod__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rmod__(decimal.Decimal(other))))

    def __divmod__(self, other: typing.Any, /) -> tuple[Real, Real]:
        q, r = decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__divmod__(decimal.Decimal(other))
        return (Real(str(q)), Real(str(r)))

    def __rdivmod__(self, other: typing.Any, /) -> tuple[Real, Real]:
        q, r = decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rdivmod__(decimal.Decimal(other))
        return (Real(str(q)), Real(str(r)))

    def __pow__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__pow__(decimal.Decimal(other))))

    def __rpow__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rpow__(decimal.Decimal(other))))

    def __floordiv__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__floordiv__(decimal.Decimal(other))))

    def __rfloordiv__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rfloordiv__(decimal.Decimal(other))))

    def __truediv__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__truediv__(decimal.Decimal(other))))

    def __rtruediv__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rtruediv__(decimal.Decimal(other))))


class Integer(Real):
    """
    Represents integer literals.
    """

    _pattern = re.compile(r'([-+]?(?:(?:\d+(?:[eE][-+]?\d+)?)|(?:[eE][-+]?\d+)))([\s\S]*)', re.IGNORECASE)

    def __hash__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__hash__()

    def __neg__(self) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__neg__()))

    def __pos__(self) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__pos__()))

    def __abs__(self) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__abs__()))

    def __bool__(self) -> bool:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__bool__()

    def __int__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__int__()

    def __float__(self) -> float:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__float__()

    def __trunc__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__trunc__()

    def __floor__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__floor__()

    def __ceil__(self) -> int:
        return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__ceil__()

    def __round__(self, ndigits: int = 0) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__round__(ndigits)))

    def __lt__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__lt__(decimal.Decimal(other))
        else:
            return str.__lt__(self, other)

    def __le__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__le__(decimal.Decimal(other))
        else:
            return str.__le__(self, other)

    def __eq__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__eq__(decimal.Decimal(other))
        else:
            return str.__eq__(self, other)

    def __ne__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__ne__(decimal.Decimal(other))
        else:
            return str.__ne__(self, other)

    def __gt__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__gt__(decimal.Decimal(other))
        else:
            return str.__gt__(self, other)

    def __ge__(self, other: typing.Any, /) -> bool:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__ge__(decimal.Decimal(other))
        else:
            return str.__ge__(self, other)

    def __add__(self, other: typing.Any, /) -> Integer | str:
        if isinstance(other, (Integer, Real, int, float, decimal.Decimal)):
            return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__add__(decimal.Decimal(other))))
        else:
            return str.__add__(self, other)

    def __radd__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__radd__(decimal.Decimal(other))))

    def __sub__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__sub__(decimal.Decimal(other))))

    def __rsub__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rsub__(decimal.Decimal(other))))

    def __mul__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__mul__(decimal.Decimal(other))))

    def __rmul__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rmul__(decimal.Decimal(other))))

    def __mod__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__mod__(decimal.Decimal(other))))

    def __rmod__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rmod__(decimal.Decimal(other))))

    def __divmod__(self, other: typing.Any, /) -> tuple[Integer, Integer]:
        q, r = decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__divmod__(decimal.Decimal(other))
        return (Integer(str(q)), Integer(str(r)))

    def __rdivmod__(self, other: typing.Any, /) -> tuple[Integer, Integer]:
        q, r = decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rdivmod__(decimal.Decimal(other))
        return (Integer(str(q)), Integer(str(r)))

    def __pow__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__pow__(decimal.Decimal(other))))

    def __rpow__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rpow__(decimal.Decimal(other))))

    def __floordiv__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__floordiv__(decimal.Decimal(other))))

    def __rfloordiv__(self, other: typing.Any, /) -> Integer:
        return Integer(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rfloordiv__(decimal.Decimal(other))))

    def __truediv__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__truediv__(decimal.Decimal(other))))

    def __rtruediv__(self, other: typing.Any, /) -> Real:
        return Real(str(decimal.Decimal(self if self[0] not in {'e', 'E'} else f'1{self}').__rtruediv__(decimal.Decimal(other))))
