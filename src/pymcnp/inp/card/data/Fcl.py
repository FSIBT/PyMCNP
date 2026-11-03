import typing
import decimal
import collections

from .... import abc
from ... import literal
from ..Data import Data


class Fcl(Data):
    """
    Represents fcl data cards.

    Attributes:
        keyword: fcl data card `FCL` symbol.
        colon: fcl data card `colon` parameter.
        particle: fcl data card `particle` parameter.
        x: fcl data card `x` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FCL'] | str = abc.Terminal[r'FCL']('FCL')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    x: (
        typing.Annotated[abc.Array, literal.Real | literal.Jump, None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Real | literal.Jump | int | float | decimal.Decimal | str]
        | str
    )
