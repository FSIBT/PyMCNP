import decimal
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class Aorro(Group):
    """
    Represents aorro groups.

    Attributes:
        ao: aorro group `ao` parameter.
        r: aorro group `r` parameter.
        ro: aorro group `ro` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    ao: literal.Real | int | float | decimal.Decimal | str
    r: literal.Real | int | float | decimal.Decimal | str
    ro: literal.Real | int | float | decimal.Decimal | str
