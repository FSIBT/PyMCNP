import typing

from ..... import abc
from .... import literal
from ..Ft import Ft


class Tag(Ft):
    """
    Represents tag ft data options.

    Attributes:
        id: tag group ``r'TAG'`` symbol.
        a: tag group ``a`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'TAG'] | str = abc.Terminal[r'TAG']('TAG')
    a: literal.Integer | int | str
