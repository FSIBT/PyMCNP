import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Pd(Cell):
    """
    Represents pd cell options.

    Attributes:
        keyword: pd cell option `PD` symbol.
        suffix: pd cell option `n` parameter.
        equals: pd cell option `=` symbol.
        p: pd cell option `p` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PD'] | str = abc.Terminal[r'PD']('PD')
    suffix: literal.Integer | int | str
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    p: literal.Real | int | float | decimal.Decimal | str
