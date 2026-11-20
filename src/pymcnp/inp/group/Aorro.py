from .. import literal
from ..Group import Group


class Aorro(Group):
    """
    Represents aorro groups.

    Attributes:
        ao: aorro group ``ao`` parameter.
        r: aorro group ``r`` parameter.
        ro: aorro group ``ro`` parameter.
    """

    ao: literal.Real
    r: literal.Real
    ro: literal.Real
