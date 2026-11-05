import typing
import decimal
import collections

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Erg(Ksen):
    """
    Represents erg ksen data options.

    Attributes:
        keyword: erg ksen data option ``r'ERG'`` symbol.
        equals: erg ksen data option ``r'='`` symbol.
        e: erg ksen data option ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ERG'] | str = abc.Terminal[r'ERG']('ERG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
