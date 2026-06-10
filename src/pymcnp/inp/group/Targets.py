import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class Targets(Group):
    """
    Represents targets groups.

    Attributes:
        original: targets group `original` parameter.
        new: targets group `new` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    original: literal.Zaid | str
    new: literal.Zaid | str
