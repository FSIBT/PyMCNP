import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Bflcl(Cell):
    """
    Represents bflcl cell options.

    Attributes:
        keyword: bflcl cell option `BFLCL` symbol.
        equals: bflcl cell option `=` symbol.
        x: bflcl cell option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BFLCL'] | str = abc.Terminal[r'BFLCL']('BFLCL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
