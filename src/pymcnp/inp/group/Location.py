import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class Location(Group):
    """
    Represents location groups.

    Attributes:
        x: location group `x` parameter.
        y: location group `y` parameter.
        z: location group `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    x: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    y: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    z: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
