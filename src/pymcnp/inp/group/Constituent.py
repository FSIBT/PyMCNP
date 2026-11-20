from .. import literal
from ..Group import Group


class Constituent(Group):
    """
    Represents constituent groups.

    Attributes:
        z: constituent group ``z`` parameter.
        f: constituent group ``f`` parameter.
    """

    z: literal.Zaid
    f: literal.Real
