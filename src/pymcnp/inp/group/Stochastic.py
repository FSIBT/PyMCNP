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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    n: literal.Integer | int | str = dataclasses.field(kw_only=True)
    dx: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    dy: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    dz: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
