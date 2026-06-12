import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Pds(Ft):
    """
    Represents pds ft data options.

    Attributes:
        id: pds group `PDS` symbol.
        c: pds group `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'PDS'] | str = abc.Terminal[r'PDS']('PDS')
    c: literal.Integer | int | str
