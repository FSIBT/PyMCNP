import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class U(Cell):
    """
    Represents u cell options.

    Attributes:
        keyword: u cell option ``r'U'`` symbol.
        equals: u cell option ``r'='`` symbol.
        n: u cell option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'U'] = abc.Terminal[r'U']('U')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    n: literal.Integer
