import typing
import dataclasses

from ..... import abc
from ..Ft import Ft


class Let(Ft):
    """
    Represents let ft data options.

    Attributes:
        id: let group `LET` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'LET'] | str = abc.Terminal[r'LET']('LET')
