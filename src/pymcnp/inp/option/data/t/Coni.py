import typing
import decimal

from ..... import abc
from .... import literal
from ..T import T


class Coni(T):
    """
    Represents coni t data options.

    Attributes:
        keyword: coni t data option `CONI` symbol.
        equals: coni t data option `=` symbol.
        value: coni t data option `value` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CONI'] | str = abc.Terminal[r'CONI']('CONI')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
