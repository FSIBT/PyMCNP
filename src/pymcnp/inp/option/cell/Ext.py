import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Ext(Cell):
    """
    Represents ext cell options.

    Attributes:
        keyword: ext cell option ``r'EXT'`` symbol.
        colon: ext cell option ``colon`` parameter.
        particle: ext cell option ``particle`` parameter.
        equals: ext cell option ``r'='`` symbol.
        a: ext cell option ``a`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EXT'] = abc.Terminal[r'EXT']('EXT')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    a: literal.Qvm
