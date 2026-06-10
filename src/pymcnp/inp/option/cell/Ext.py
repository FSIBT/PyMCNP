import typing
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Ext(Cell):
    """
    Represents ext cell options.

    Attributes:
        keyword: ext cell option `EXT` symbol.
        colon: ext cell option `colon` parameter.
        particle: ext cell option `particle` parameter.
        equals: ext cell option `=` symbol.
        a: ext cell option `a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EXT'] | str = abc.Terminal[r'EXT']('EXT')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    a: literal.Qvm | str
