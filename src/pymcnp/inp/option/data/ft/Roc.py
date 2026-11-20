import typing

from ..... import abc
from .... import literal
from ..Ft import Ft


class Roc(Ft):
    """
    Represents roc ft data options.

    Attributes:
        id: roc group ``r'ROC'`` symbol.
        nhb: roc group ``nhb`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'ROC'] = abc.Terminal[r'ROC']('ROC')
    nhb: literal.Real
