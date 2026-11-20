from .. import literal
from ..Group import Group


class EspltEntry(Group):
    """
    Represents espltentry groups.

    Attributes:
        r: espltentry group ``r`` parameter.
        e: espltentry group ``e`` parameter.
    """

    r: literal.Real
    e: literal.Real
