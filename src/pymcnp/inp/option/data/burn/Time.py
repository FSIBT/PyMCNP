import typing
import decimal
import collections

from ..... import abc
from .... import literal
from ..Burn import Burn


class Time(Burn):
    """
    Represents time burn data options.

    Attributes:
        keyword: time burn data option ``r'TIME'`` symbol.
        equals: time burn data option ``r'='`` symbol.
        t: time burn data option ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TIME'] | str = abc.Terminal[r'TIME']('TIME')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
