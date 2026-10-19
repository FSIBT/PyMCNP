import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Elc(Ft):
    """
    Represents elc ft data options.

    Attributes:
        id: elc group `ELC` symbol.
        c: elc group `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    id: typing.Annotated[abc.Terminal, r'ELC'] | str = abc.Terminal[r'ELC']('ELC')
    c: literal.Integer | int | str = dataclasses.field(kw_only=True)
