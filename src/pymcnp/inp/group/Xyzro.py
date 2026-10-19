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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    x: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    y: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    z: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ro: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
