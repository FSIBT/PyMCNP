import typing
import dataclasses

from ..... import abc
from ..Ft import Ft


class Cap(Ft):
    """
    Represents cap ft data options.

    Attributes:
        id: cap group `CAP` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'CAP'] | str = abc.Terminal[r'CAP']('CAP')
