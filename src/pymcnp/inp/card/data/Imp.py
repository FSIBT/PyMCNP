import typing

from .... import abc
from ... import literal
from ..Data import Data


class Imp(Data):
    """
    Represents imp data cards.

    Attributes:
        keyword: imp data card ``r'IMP'`` symbol.
        colon: imp data card ``colon`` parameter.
        particle: imp data card ``particle`` parameter.
        x: imp data card ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IMP'] = abc.Terminal[r'IMP']('IMP')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    x: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']
