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

    x: literal.Real
    y: literal.Real
    z: literal.Real
