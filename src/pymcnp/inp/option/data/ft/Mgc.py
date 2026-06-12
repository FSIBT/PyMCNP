import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Mgc(Ft):
    """
    Represents mgc ft data options.

    Attributes:
        id: mgc group `MGC` symbol.
        fg: mgc group `fg` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'MGC'] | str = abc.Terminal[r'MGC']('MGC')
    fg: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')
