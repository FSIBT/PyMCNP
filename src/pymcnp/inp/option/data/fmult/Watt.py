import typing
import decimal

from ..... import abc
from ..Fmult import Fmult
from .... import literal


class Watt(Fmult):
    """
    Represents watt fmult data options.

    Attributes:
        keyword: watt fmult data option ``r'WATT'`` symbol.
        equals: watt fmult data option ``r'='`` symbol.
        a: watt fmult data option ``a`` parameter.
        b: watt fmult data option ``b`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WATT'] | str = abc.Terminal[r'WATT']('WATT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
