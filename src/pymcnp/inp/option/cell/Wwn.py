import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Wwn(Cell):
    """
    Represents wwn cell options.
    """


class Wwn_0(Wwn):
    """
    Represents wwn cell options, form #0.

    Attributes:
        keyword: wwn cell option `WWN` symbol.
        suffix: wwn cell option `i` parameter.
        colon: wwn cell option `colon` parameter.
        particle: wwn cell option `particle` parameter.
        equals: wwn cell option `=` symbol.
        w: wwn cell option `w` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'WWN'] | str = abc.Terminal[r'WWN']('WWN')
    suffix: literal.Integer | int | str = dataclasses.field(kw_only=True)
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str = dataclasses.field(kw_only=True)
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    w: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)


class Wwn_1(Wwn):
    """
    Represents wwn cell options, form #1.

    Attributes:
        keyword: wwn cell option `WWN` symbol.
        colon: wwn cell option `colon` parameter.
        particle: wwn cell option `particle` parameter.
        equals: wwn cell option `=` symbol.
        w: wwn cell option `w` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'WWN'] | str = abc.Terminal[r'WWN']('WWN')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str = dataclasses.field(kw_only=True)
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    w: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
