import typing
import dataclasses


from .... import abc
from ... import literal
from ..Data import Data


class Ext(Data):
    """
    Represents ext data cards.

    Attributes:
        keyword: ext data card ``r'EXT'`` symbol.
        colon: ext data card ``colon`` parameter.
        particle: ext data card ``particle`` parameter.
        a: ext data card ``a`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EXT'] = abc.Terminal[r'EXT']('EXT')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    a: typing.Annotated[abc.Array, literal.Qvm | literal.Jump, None] | typing.Annotated[abc.Terminal, r''] = dataclasses.field(kw_only=True)
