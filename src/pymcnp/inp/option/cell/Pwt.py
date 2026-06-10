import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Pwt(Cell):
    """
    Represents pwt cell options.

    Attributes:
        keyword: pwt cell option `PWT` symbol.
        equals: pwt cell option `=` symbol.
        w: pwt cell option `w` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PWT'] | str = abc.Terminal[r'PWT']('PWT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    w: literal.Real | int | float | decimal.Decimal | str
