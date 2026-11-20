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

    n: literal.Integer
    dx: literal.Real
    dy: literal.Real
    dz: literal.Real
