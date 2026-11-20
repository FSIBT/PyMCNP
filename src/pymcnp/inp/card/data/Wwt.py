import typing

from .... import abc
from ... import literal
from ..Data import Data


class Wwt(Data):
    """
    Represents wwt data cards.

    Attributes:
        keyword: wwt data card ``r'WWT'`` symbol.
        colon: wwt data card ``colon`` parameter.
        particle: wwt data card ``particle`` parameter.
        t: wwt data card ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WWT'] = abc.Terminal[r'WWT']('WWT')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
