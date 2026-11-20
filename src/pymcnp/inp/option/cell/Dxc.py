import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Dxc(Cell):
    """
    Represents dxc cell options.

    Attributes:
        keyword: dxc cell option ``r'DXC'`` symbol.
        suffix: dxc cell option ``n`` parameter.
        colon: dxc cell option ``colon`` parameter.
        particle: dxc cell option ``particle`` parameter.
        equals: dxc cell option ``r'='`` symbol.
        p: dxc cell option ``p`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DXC'] = abc.Terminal[r'DXC']('DXC')
    suffix: literal.Integer
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    p: literal.Real
