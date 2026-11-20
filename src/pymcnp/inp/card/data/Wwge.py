import typing

from .... import abc
from ... import literal
from ..Data import Data


class Wwge(Data):
    """
    Represents wwge data cards.

    Attributes:
        keyword: wwge data card ``r'WWGE'`` symbol.
        colon: wwge data card ``colon`` parameter.
        particle: wwge data card ``particle`` parameter.
        e: wwge data card ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WWGE'] = abc.Terminal[r'WWGE']('WWGE')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
