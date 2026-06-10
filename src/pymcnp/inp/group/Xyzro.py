import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class Xyzro(Group):
    """
    Represents xyzro groups.

    Attributes:
        x: xyzro group `x` parameter.
        y: xyzro group `y` parameter.
        z: xyzro group `z` parameter.
        ro: xyzro group `ro` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
    ro: literal.Real | int | float | decimal.Decimal | str
