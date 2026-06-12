import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Com(Ft):
    """
    Represents com ft data options.

    Attributes:
        id: com group `COM` symbol.
        t: com group `t` parameter.
        a: com group `a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'COM'] | str = abc.Terminal[r'COM']('COM')
    t: literal.Integer | int | str
    a: literal.Integer | int | str
