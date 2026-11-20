from .. import literal
from ..Group import Group


class Dxtran(Group):
    """
    Represents dxtran groups.

    Attributes:
        x: dxtran group ``x`` parameter.
        y: dxtran group ``y`` parameter.
        z: dxtran group ``z`` parameter.
        ri: dxtran group ``ri`` parameter.
        ro: dxtran group ``ro`` parameter.
    """

    x: literal.Real
    y: literal.Real
    z: literal.Real
    ri: literal.Real
    ro: literal.Real
