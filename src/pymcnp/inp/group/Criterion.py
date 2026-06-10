import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class Criterion(Group):
    """
    Represents criterion groups.

    Attributes:
        k: criterion group `k` parameter.
        m: criterion group `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    k: literal.Real | int | float | decimal.Decimal | str
    m: literal.Real | int | float | decimal.Decimal | str
