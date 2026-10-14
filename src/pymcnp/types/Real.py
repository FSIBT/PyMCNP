import re
import decimal

from . import _number
from .Horizontal import Horizontal


class Real(_number.Number):
    """
    Represents MCNP reals or horizontal syntax.

    Attributes:
        value: Real value or horizontal syntax.
    """

    _REGEX = re.compile(r'\A(?:j|log|ilog|\d*m|i|r|(?:[-+0-9.eE][-+0-9.eEdD]*))\Z', re.IGNORECASE)

    def __init__(self, value: decimal.Decimal | Horizontal):
        super().__init__(value)

    @staticmethod
    def _convert(value):
        return value

    @staticmethod
    def _operand(other):
        if isinstance(other, Real):
            return other.value
        if isinstance(other, decimal.Decimal):
            return other
        if isinstance(other, (float, int)):
            return decimal.Decimal(str(other))

        return _number.UNSUPPORTED

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
