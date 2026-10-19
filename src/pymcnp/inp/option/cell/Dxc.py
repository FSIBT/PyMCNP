import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Dxc(Cell):
    """
    Represents dxc cell options.

    Attributes:
        keyword: dxc cell option `DXC` symbol.
        suffix: dxc cell option `n` parameter.
        colon: dxc cell option `colon` parameter.
        particle: dxc cell option `particle` parameter.
        equals: dxc cell option `=` symbol.
        p: dxc cell option `p` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'DXC'] | str = abc.Terminal[r'DXC']('DXC')
    suffix: literal.Integer | int | str = dataclasses.field(kw_only=True)
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str = dataclasses.field(kw_only=True)
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    p: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
