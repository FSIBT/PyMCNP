import typing


from .... import abc
from ... import literal
from ..Data import Data
from ... import group


class Tsplt(Data):
    """
    Represents tsplt data cards.

    Attributes:
        keyword: tsplt data card ``r'TSPLT'`` symbol.
        colon: tsplt data card ``colon`` parameter.
        particle: tsplt data card ``particle`` parameter.
        r_t: tsplt data card ``r_t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TSPLT'] = abc.Terminal[r'TSPLT']('TSPLT')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    r_t: typing.Annotated[abc.Array, group.TspltEntry, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
