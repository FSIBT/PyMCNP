from .. import literal
from ..Group import Group


class Bias(Group):
    """
    Represents bias groups.

    Attributes:
        w: bias group ``w`` parameter.
        e: bias group ``e`` parameter.
    """

    w: literal.Real
    e: literal.Real
