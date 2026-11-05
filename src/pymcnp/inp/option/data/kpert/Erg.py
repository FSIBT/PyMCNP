import typing
import decimal
import collections

from ..... import abc
from ..Kpert import Kpert
from .... import literal


class Erg(Kpert):
    """
    Represents erg kpert data options.

    Attributes:
        keyword: erg kpert data option ``r'ERG'`` symbol.
        equals: erg kpert data option ``r'='`` symbol.
        e: erg kpert data option ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ERG'] | str = abc.Terminal[r'ERG']('ERG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
