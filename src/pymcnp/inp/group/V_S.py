import decimal

from .. import literal
from ..Group import Group


class V_S(Group):
    """
    Represents v_s groups.

    Attributes:
        v: v_s group ``v`` parameter.
        s: v_s group ``s`` parameter.
    """

    i: literal.Distribution | literal.Real | int | float | decimal.Decimal | str
    j: literal.Distribution | literal.Real | int | float | decimal.Decimal | str
