from .. import literal
from ..Group import Group


class MatCell(Group):
    """
    Represents matcell groups.

    Attributes:
        m: matcell group `m` parameter.
        c: matcell group `c` parameter.
    """

    m: literal.Integer | int | str
    c: literal.Integer | int | str
