import typing
import decimal
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Tmp(Cell):
    """
    Represents tmp cell options.
    """

    pass


class Tmp_0(Tmp):
    """
    Represents tmp cell options, form #0.

    Attributes:
        keyword: tmp cell option `TMP` symbol.
        suffix: tmp cell option `n` parameter.
        equals: tmp cell option `=` symbol.
        t: tmp cell option `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TMP'] | str = abc.Terminal[r'TMP']('TMP')
    suffix: literal.Integer | int | str
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    t: literal.Real | int | float | decimal.Decimal | str


class Tmp_1(Tmp):
    """
    Represents tmp cell options, form #1.

    Attributes:
        keyword: tmp cell option `TMP` symbol.
        equals: tmp cell option `=` symbol.
        t: tmp cell option `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TMP'] | str = abc.Terminal[r'TMP']('TMP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    t: literal.Real | int | float | decimal.Decimal | str
