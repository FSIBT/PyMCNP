import typing

from ..... import abc
from ..Dawwg import Dawwg
from .... import literal


class Points(Dawwg):
    """
    Represents points dawwg data options.

    Attributes:
        keyword: points dawwg data option `POINTS` symbol.
        equals: points dawwg data option `=` symbol.
        n: points dawwg data option `n` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'POINTS'] | str = abc.Terminal[r'POINTS']('POINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
