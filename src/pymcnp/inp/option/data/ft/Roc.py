import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Roc(Ft):
    """
    Represents roc ft data options.

    Attributes:
        id: roc group `ROC` symbol.
        nhb: roc group `nhb` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'ROC'] | str = abc.Terminal[r'ROC']('ROC')
    nhb: literal.Real | int | float | decimal.Decimal | str
