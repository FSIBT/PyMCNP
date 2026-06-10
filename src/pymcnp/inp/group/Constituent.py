import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class Constituent(Group):
    """
    Represents constituent groups.

    Attributes:
        z: constituent group `z` parameter.
        f: constituent group `f` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    z: literal.Zaid | str
    f: literal.Real | int | float | decimal.Decimal | str
