import decimal

from .. import literal
from ..Group import Group


class TspltEntry(Group):
    """
    Represents tsplt entry groups.

    Attributes:
        r: tsplt entry group ``r`` parameter.
        t: tsplt entry group ``t`` parameter.
    """

    r: literal.Real | int | float | decimal.Decimal | str
    t: literal.Real | int | float | decimal.Decimal | str
