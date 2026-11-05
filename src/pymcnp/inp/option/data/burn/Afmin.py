import typing
import decimal

from ..... import abc
from .... import literal
from ..Burn import Burn


class Afmin(Burn):
    """
    Represents afmin burn data options.

    Attributes:
        keyword: afmin burn data option ``r'AFMIN'`` symbol.
        equals: afmin burn data option ``r'='`` symbol.
        af1: afmin burn data option ``af1`` parameter.
        af2: afmin burn data option ``af2`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AFMIN'] | str = abc.Terminal[r'AFMIN']('AFMIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    af1: literal.Real | int | float | decimal.Decimal | str
    af2: literal.Real | int | float | decimal.Decimal | str
