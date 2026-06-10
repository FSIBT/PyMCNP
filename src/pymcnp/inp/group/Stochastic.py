import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class Stochastic(Group):
    """
    Represents stochastic groups.

    Attributes:
        n: stochastic group `n` parameter.
        dx: stochastic group `dx` parameter.
        dy: stochastic group `dy` parameter.
        dz: stochastic group `dz` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    n: literal.Integer | int | str
    dx: literal.Real | int | float | decimal.Decimal | str
    dy: literal.Real | int | float | decimal.Decimal | str
    dz: literal.Real | int | float | decimal.Decimal | str
