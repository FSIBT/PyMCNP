import typing

from ..... import abc
from .... import literal
from ..Ft import Ft


class Pds(Ft):
    """
    Represents pds ft data options.

    Attributes:
        id: pds group ``r'PDS'`` symbol.
        c: pds group ``c`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'PDS'] | str = abc.Terminal[r'PDS']('PDS')
    c: literal.Integer | int | str
