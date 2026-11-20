import typing

from .... import abc
from ... import literal
from ..Data import Data


class Fcl(Data):
    """
    Represents fcl data cards.

    Attributes:
        keyword: fcl data card ``r'FCL'`` symbol.
        colon: fcl data card ``colon`` parameter.
        particle: fcl data card ``particle`` parameter.
        x: fcl data card ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FCL'] = abc.Terminal[r'FCL']('FCL')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    x: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']
