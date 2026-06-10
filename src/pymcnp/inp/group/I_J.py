import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class I_J(Group):
    """
    Represents i_j groups.

    Attributes:
        i: i_j group `i` parameter.
        j: i_j group `j` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    i: literal.Integer | int | str
    j: literal.Real | int | float | decimal.Decimal | str
