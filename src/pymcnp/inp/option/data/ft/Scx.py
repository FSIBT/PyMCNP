import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Scx(Ft):
    """
    Represents scx ft data options.

    Attributes:
        id: scx group `SCX` symbol.
        k: scx group `k` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'SCX'] | str = abc.Terminal[r'SCX']('SCX')
    k: literal.Integer | int | str
