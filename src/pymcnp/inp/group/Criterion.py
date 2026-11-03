import decimal

from .. import literal
from ..Group import Group


class Criterion(Group):
    """
    Represents criterion groups.

    Attributes:
        k: criterion group `k` parameter.
        m: criterion group `m` parameter.
    """

    k: literal.Real | int | float | decimal.Decimal | str
    m: literal.Real | int | float | decimal.Decimal | str
