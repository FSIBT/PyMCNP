import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Vol(Cell):
    """
    Represents vol cell options.

    Attributes:
        keyword: vol cell option `VOL` symbol.
        equals: vol cell option `=` symbol.
        x: vol cell option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'VOL'] | str = abc.Terminal[r'VOL']('VOL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
