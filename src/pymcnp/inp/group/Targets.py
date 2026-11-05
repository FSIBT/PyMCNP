from .. import literal
from ..Group import Group


class Targets(Group):
    """
    Represents targets groups.

    Attributes:
        original: targets group ``original`` parameter.
        new: targets group ``new`` parameter.
    """

    original: literal.Zaid | str
    new: literal.Zaid | str
