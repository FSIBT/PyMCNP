import typing
import decimal

from ..... import abc
from .... import literal
from ..Ft import Ft


class Geb(Ft):
    """
    Represents geb ft data options.

    Attributes:
        id: geb group ``r'GEB'`` symbol.
        a: geb group ``a`` parameter.
        b: geb group ``b`` parameter.
        c: geb group ``c`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'GEB'] | str = abc.Terminal[r'GEB']('GEB')
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
    c: literal.Real | int | float | decimal.Decimal | str
