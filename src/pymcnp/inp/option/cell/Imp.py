import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Imp(Cell):
    """
    Represents imp cell options.

    Attributes:
        keyword: imp cell option ``r'IMP'`` symbol.
        colon: imp cell option ``colon`` parameter.
        particle: imp cell option ``particle`` parameter.
        equals: imp cell option ``r'='`` symbol.
        x: imp cell option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IMP'] = abc.Terminal[r'IMP']('IMP')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
