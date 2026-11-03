import typing
import decimal
import collections

from .... import abc
from ... import literal
from ..Data import Data


class Vol(Data):
    """
    Represents vol data cards.

    Attributes:
        keyword: vol data card `VOL` symbol.
        no: vol data card `NO` symbol.
        x: vol data card `x` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VOL'] | str = abc.Terminal[r'VOL']('VOL')
    no: typing.Annotated[abc.Terminal, r'NO'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: (
        typing.Annotated[abc.Array, literal.Real | literal.Jump, None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Real | literal.Jump | int | float | decimal.Decimal | str]
        | str
    )
