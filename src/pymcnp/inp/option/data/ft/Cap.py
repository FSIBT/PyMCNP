import typing

from ..... import abc
from ..Ft import Ft


class Cap(Ft):
    """
    Represents cap ft data options.

    Attributes:
        id: cap group `CAP` symbol.
    """

    id: typing.Annotated[abc.Terminal, r'CAP'] | str = abc.Terminal[r'CAP']('CAP')
