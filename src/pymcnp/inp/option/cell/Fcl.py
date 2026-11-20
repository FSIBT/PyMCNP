import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Fcl(Cell):
    """
    Represents fcl cell options.

    Attributes:
        keyword: fcl cell option ``r'FCL'`` symbol.
        colon: fcl cell option ``colon`` parameter.
        particle: fcl cell option ``particle`` parameter.
        equals: fcl cell option ``r'='`` symbol.
        x: fcl cell option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FCL'] = abc.Terminal[r'FCL']('FCL')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
