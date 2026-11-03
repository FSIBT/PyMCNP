import decimal

from .. import literal
from ..Group import Group


class Constituent(Group):
    """
    Represents constituent groups.

    Attributes:
        z: constituent group `z` parameter.
        f: constituent group `f` parameter.
    """

    z: literal.Zaid | str
    f: literal.Real | int | float | decimal.Decimal | str
