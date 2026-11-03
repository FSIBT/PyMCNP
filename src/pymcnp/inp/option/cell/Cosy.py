import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Cosy(Cell):
    """
    Represents cosy cell options.

    Attributes:
        keyword: cosy cell option `COSY` symbol.
        equals: cosy cell option `=` symbol.
        m: cosy cell option `m` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'COSY'] | str = abc.Terminal[r'COSY']('COSY')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m: literal.Integer | int | str
