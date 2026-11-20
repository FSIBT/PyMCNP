import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Elpt(Cell):
    """
    Represents elpt cell options.

    Attributes:
        keyword: elpt cell option ``r'ELPT'`` symbol.
        colon: elpt cell option ``colon`` parameter.
        particle: elpt cell option ``particle`` parameter.
        equals: elpt cell option ``r'='`` symbol.
        x: elpt cell option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ELPT'] = abc.Terminal[r'ELPT']('ELPT')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
