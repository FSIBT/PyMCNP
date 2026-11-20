import typing

from ..... import abc
from .... import literal
from ..Ft import Ft


class Com(Ft):
    """
    Represents com ft data options.

    Attributes:
        id: com group ``r'COM'`` symbol.
        t: com group ``t`` parameter.
        a: com group ``a`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'COM'] = abc.Terminal[r'COM']('COM')
    t: literal.Integer
    a: literal.Integer
