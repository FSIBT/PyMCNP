import decimal

from .. import literal
from ..Group import Group


class Location(Group):
    """
    Represents location groups.

    Attributes:
        x: location group ``x`` parameter.
        y: location group ``y`` parameter.
        z: location group ``z`` parameter.
    """

    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
