import decimal

from .. import literal
from ..Group import Group


class Aorro(Group):
    """
    Represents aorro groups.

    Attributes:
        ao: aorro group `ao` parameter.
        r: aorro group `r` parameter.
        ro: aorro group `ro` parameter.
    """

    ao: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str
    ro: literal.Real | int | float | decimal.Decimal | str
