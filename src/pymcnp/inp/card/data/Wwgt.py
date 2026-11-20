import typing

from .... import abc
from ... import literal
from ..Data import Data


class Wwgt(Data):
    """
    Represents wwgt data cards.

    Attributes:
        keyword: wwgt data card ``r'WWGT'`` symbol.
        colon: wwgt data card ``colon`` parameter.
        particle: wwgt data card ``particle`` parameter.
        t: wwgt data card ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WWGT'] = abc.Terminal[r'WWGT']('WWGT')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
