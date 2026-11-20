import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Bflcl(Cell):
    """
    Represents bflcl cell options.

    Attributes:
        keyword: bflcl cell option ``r'BFLCL'`` symbol.
        equals: bflcl cell option ``r'='`` symbol.
        x: bflcl cell option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BFLCL'] = abc.Terminal[r'BFLCL']('BFLCL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
