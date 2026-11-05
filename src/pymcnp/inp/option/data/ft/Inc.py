import typing

from ..... import abc
from ..Ft import Ft


class Inc(Ft):
    """
    Represents inc ft data options.

    Attributes:
        id: inc group ``r'INC'`` symbol.
    """

    id: typing.Annotated[abc.Terminal, r'INC'] | str = abc.Terminal[r'INC']('INC')
