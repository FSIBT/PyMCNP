import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class Dxtran(Group):
    """
    Represents dxtran groups.

    Attributes:
        x: dxtran group `x` parameter.
        y: dxtran group `y` parameter.
        z: dxtran group `z` parameter.
        ri: dxtran group `ri` parameter.
        ro: dxtran group `ro` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    x: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    y: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    z: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ri: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ro: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
