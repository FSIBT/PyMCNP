import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Rdum(Data):
    """
    Represents rdum data cards.

    Attributes:
        keyword: rdum data card `RDUM` symbol.
        r: rdum data card `r` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RDUM'] | str = abc.Terminal[r'RDUM']('RDUM')
    r: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
