import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Vol(Cell):
    """
    Represents vol cell options.

    Attributes:
        keyword: vol cell option ``r'VOL'`` symbol.
        equals: vol cell option ``r'='`` symbol.
        x: vol cell option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VOL'] = abc.Terminal[r'VOL']('VOL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
