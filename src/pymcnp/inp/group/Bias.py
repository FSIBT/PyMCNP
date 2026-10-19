import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class Bias(Group):
    """
    Represents bias groups.

    Attributes:
        w: bias group `w` parameter.
        e: bias group `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    w: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    e: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
