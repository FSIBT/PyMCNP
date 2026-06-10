import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Rho(Cell):
    """
    Represents rho cell options.

    Attributes:
        keyword: rho cell option `RHO` symbol.
        equals: rho cell option `=` symbol.
        d: rho cell option `d` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RHO'] | str = abc.Terminal[r'RHO']('RHO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    d: literal.Real | int | float | decimal.Decimal | str
