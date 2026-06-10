import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Imp(Cell):
    """
    Represents imp cell options.

    Attributes:
        keyword: imp cell option `IMP` symbol.
        colon: imp cell option `colon` parameter.
        particle: imp cell option `particle` parameter.
        equals: imp cell option `=` symbol.
        x: imp cell option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IMP'] | str = abc.Terminal[r'IMP']('IMP')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
