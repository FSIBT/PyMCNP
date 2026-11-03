import typing
import decimal

from ..... import abc
from .... import literal
from ..Ft import Ft


class Lcs(Ft):
    """
    Represents lcs ft data options.

    Attributes:
        id: lcs group `LCS` symbol.
        lo: lcs group `lo` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'LCS'] | str = abc.Terminal[r'LCS']('LCS')
    lo: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')
