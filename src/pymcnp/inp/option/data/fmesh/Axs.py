import typing
import decimal
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Axs(Fmesh):
    """
    Represents axs fmesh data options.

    Attributes:
        keyword: axs fmesh data option `AXS` symbol.
        equals: axs fmesh data option `=` symbol.
        x: axs fmesh data option `x` parameter.
        y: axs fmesh data option `y` parameter.
        z: axs fmesh data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'AXS'] | str = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
