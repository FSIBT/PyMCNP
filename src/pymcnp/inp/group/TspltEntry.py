import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class TspltEntry(Group):
    """
    Represents tspltentry groups.

    Attributes:
        r: tspltentry group `r` parameter.
        t: tspltentry group `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    r: literal.Real | int | float | decimal.Decimal | str
    t: literal.Real | int | float | decimal.Decimal | str
