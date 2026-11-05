import decimal

from .. import literal
from ..Group import Group


class Stochastic(Group):
    """
    Represents stochastic groups.

    Attributes:
        n: stochastic group ``n`` parameter.
        dx: stochastic group ``dx`` parameter.
        dy: stochastic group ``dy`` parameter.
        dz: stochastic group ``dz`` parameter.
    """

    n: literal.Integer | int | str
    dx: literal.Real | int | float | decimal.Decimal | str
    dy: literal.Real | int | float | decimal.Decimal | str
    dz: literal.Real | int | float | decimal.Decimal | str
