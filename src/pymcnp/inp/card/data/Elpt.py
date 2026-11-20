import typing

from .... import abc
from ... import literal
from ..Data import Data


class Elpt(Data):
    """
    Represents elpt data cards.

    Attributes:
        keyword: elpt data card ``r'ELPT'`` symbol.
        colon:  elpt data card ``r':'`` symbol.
        particle: elpt data card ``particle`` parameter.
        x: elpt data card ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ELPT'] = abc.Terminal[r'ELPT']('ELPT')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    x: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
