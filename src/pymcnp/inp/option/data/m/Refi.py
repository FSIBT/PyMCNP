import typing
import decimal

from ..... import abc
from ..M import M
from .... import literal


class Refi(M):
    """
    Represents refi m data options.

    Attributes:
        keyword: refi m data option ``r'REFI'`` symbol.
        equals: refi m data option ``r'='`` symbol.
        a: refi m data option ``a`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'REFI'] | str = abc.Terminal[r'REFI']('REFI')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    a: literal.Real | int | float | decimal.Decimal | str
