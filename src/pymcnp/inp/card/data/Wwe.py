import typing

from .... import abc
from ... import literal
from ..Data import Data


class Wwe(Data):
    """
    Represents wwe data cards.

    Attributes:
        keyword: wwe data card ``r'WWE'`` symbol.
        colon: wwe data card ``colon`` parameter.
        particle: wwe data card ``particle`` parameter.
        e: wwe data card ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WWE'] = abc.Terminal[r'WWE']('WWE')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
