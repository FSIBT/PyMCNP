import typing


from .... import abc
from ... import literal
from ..Data import Data


class Mode(Data):
    """
    Represents mode data cards.

    Attributes:
        keyword: mode data card ``r'MODE'`` symbol.
        p: mode data card ``p`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MODE'] = abc.Terminal[r'MODE']('MODE')
    p: typing.Annotated[abc.Array, literal.Particle, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
