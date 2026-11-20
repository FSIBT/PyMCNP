from .. import literal
from ..Group import Group


class Xyzro(Group):
    """
    Represents xyzro groups.

    Attributes:
        x: xyzro group ``x`` parameter.
        y: xyzro group ``y`` parameter.
        z: xyzro group ``z`` parameter.
        ro: xyzro group ``ro`` parameter.
    """

    x: literal.Real
    y: literal.Real
    z: literal.Real
    ro: literal.Real
