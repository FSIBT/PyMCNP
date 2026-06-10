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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    w: literal.Real | int | float | decimal.Decimal | str
    e: literal.Real | int | float | decimal.Decimal | str
