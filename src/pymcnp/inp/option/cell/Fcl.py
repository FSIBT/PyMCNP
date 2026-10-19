import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Fcl(Cell):
    """
    Represents fcl cell options.

    Attributes:
        keyword: fcl cell option `FCL` symbol.
        colon: fcl cell option `colon` parameter.
        particle: fcl cell option `particle` parameter.
        equals: fcl cell option `=` symbol.
        x: fcl cell option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'FCL'] | str = abc.Terminal[r'FCL']('FCL')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str = dataclasses.field(kw_only=True)
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
