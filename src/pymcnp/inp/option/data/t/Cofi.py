import typing
import decimal

from ..... import abc
from .... import literal
from ..T import T


class Cofi(T):
    """
    Represents cofi t data options.

    Attributes:
        keyword: cofi t data option ``r'COFI'`` symbol.
        equals: cofi t data option ``r'='`` symbol.
        value: cofi t data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'COFI'] | str = abc.Terminal[r'COFI']('COFI')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
