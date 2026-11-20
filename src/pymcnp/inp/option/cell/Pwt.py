import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Pwt(Cell):
    """
    Represents pwt cell options.

    Attributes:
        keyword: pwt cell option ``r'PWT'`` symbol.
        equals: pwt cell option ``r'='`` symbol.
        w: pwt cell option ``w`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PWT'] = abc.Terminal[r'PWT']('PWT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    w: literal.Real
