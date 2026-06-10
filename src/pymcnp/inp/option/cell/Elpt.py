import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Elpt(Cell):
    """
    Represents elpt cell options.

    Attributes:
        keyword: elpt cell option `ELPT` symbol.
        colon: elpt cell option `colon` parameter.
        particle: elpt cell option `particle` parameter.
        equals: elpt cell option `=` symbol.
        x: elpt cell option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ELPT'] | str = abc.Terminal[r'ELPT']('ELPT')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
