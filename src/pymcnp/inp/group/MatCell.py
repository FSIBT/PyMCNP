import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class MatCell(Group):
    """
    Represents matcell groups.

    Attributes:
        m: matcell group `m` parameter.
        c: matcell group `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    m: literal.Integer | int | str
    c: literal.Integer | int | str
