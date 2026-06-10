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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DXC'] | str = abc.Terminal[r'DXC']('DXC')
    suffix: literal.Integer | int | str
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    p: literal.Real | int | float | decimal.Decimal | str
