import typing


from .... import abc
from ... import literal
from ..Data import Data
from ... import group


class Esplt(Data):
    """
    Represents esplt data cards.

    Attributes:
        keyword: esplt data card ``r'ESPLT'`` symbol.
        colon: esplt data card ``colon`` parameter.
        particle: esplt data card ``particle`` parameter.
        r_e: esplt data card ``r_e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ESPLT'] = abc.Terminal[r'ESPLT']('ESPLT')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    r_e: typing.Annotated[abc.Array, group.EspltEntry, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
