import typing
import decimal
import collections

from .... import abc
from ... import literal
from ..Data import Data


class Elpt(Data):
    """
    Represents elpt data cards.

    Attributes:
        keyword: elpt data card `ELPT` symbol.
        colon:  elpt data card `:` symbol.
        particle: elpt data card `particle` parameter.
        x: elpt data card `x` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ELPT'] | str = abc.Terminal[r'ELPT']('ELPT')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    x: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
