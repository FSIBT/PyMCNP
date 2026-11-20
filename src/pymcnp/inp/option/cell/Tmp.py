import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Tmp(Cell):
    """
    Represents tmp cell options.
    """


class Tmp_0(Tmp):
    """
    Represents tmp cell options, form #0.

    Attributes:
        keyword: tmp cell option ``r'TMP'`` symbol.
        suffix: tmp cell option ``n`` parameter.
        equals: tmp cell option ``r'='`` symbol.
        t: tmp cell option ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TMP'] = abc.Terminal[r'TMP']('TMP')
    suffix: literal.Integer
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    t: literal.Real


class Tmp_1(Tmp):
    """
    Represents tmp cell options, form #1.

    Attributes:
        keyword: tmp cell option ``r'TMP'`` symbol.
        equals: tmp cell option ``r'='`` symbol.
        t: tmp cell option ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TMP'] = abc.Terminal[r'TMP']('TMP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    t: literal.Real
