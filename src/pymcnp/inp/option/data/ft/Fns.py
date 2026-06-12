import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Fns(Ft):
    """
    Represents fns ft data options.

    Attributes:
        id: fns group `FNS` symbol.
        nt: fns group `nt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'FNS'] | str = abc.Terminal[r'FNS']('FNS')
    nt: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
