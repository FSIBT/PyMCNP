import typing

from ..... import abc
from .... import literal
from ..Ft import Ft


class Scx(Ft):
    """
    Represents scx ft data options.

    Attributes:
        id: scx group ``r'SCX'`` symbol.
        k: scx group ``k`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'SCX'] | str = abc.Terminal[r'SCX']('SCX')
    k: literal.Integer | int | str
