import typing
import decimal

from ..... import abc
from ..Act import Act
from .... import literal


class Pecut(Act):
    """
    Represents pecut act data options.

    Attributes:
        keyword: pecut act data option ``r'PECUT'`` symbol.
        equals: pecut act data option ``r'='`` symbol.
        e: pecut act data option ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PECUT'] | str = abc.Terminal[r'PECUT']('PECUT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    e: literal.Real | int | float | decimal.Decimal | str
