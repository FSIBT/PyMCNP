import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Axs(Mesh):
    """
    Represents axs mesh data options.

    Attributes:
        keyword: axs mesh data option `AXS` symbol.
        equals: axs mesh data option `=` symbol.
        x: axs mesh data option `x` parameter.
        y: axs mesh data option `y` parameter.
        z: axs mesh data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'AXS'] | str = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    y: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    z: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
