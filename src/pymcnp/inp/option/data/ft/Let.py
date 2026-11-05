import typing

from ..... import abc
from ..Ft import Ft


class Let(Ft):
    """
    Represents let ft data options.

    Attributes:
        id: let group ``r'LET'`` symbol.
    """

    id: typing.Annotated[abc.Terminal, r'LET'] | str = abc.Terminal[r'LET']('LET')
