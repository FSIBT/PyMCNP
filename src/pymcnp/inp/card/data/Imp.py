import typing
import decimal
import collections

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

    keyword: typing.Annotated[abc.Terminal, r'IMP'] | str = abc.Terminal[r'IMP']('IMP')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    x: (
        typing.Annotated[abc.Array, literal.Real | literal.Jump, None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Real | literal.Jump | int | float | decimal.Decimal | str]
        | str
    )
