import typing

from ... import abc
from ..Line import Line


class P(Line):
    """
    Represents p lines.
    """


class P_0(P):
    """
    Represents p lines, form #0.

    Attributes:
        x: p line `x` parameter.
        y: p line `y` parameter.
        z: p line `z` parameter.
    """

    blank: typing.Annotated[abc.Terminal, r' ']
    x: typing.Annotated[abc.Terminal, r'.{13}']
    y: typing.Annotated[abc.Terminal, r'.{13}']
    z: typing.Annotated[abc.Terminal, r'.{13}']


class P_1(P):
    """
    Represents p lines, form #1.

    Attributes:
        x: p line `x` parameter.
        y: p line `y` parameter.
        z: p line `z` parameter.
        u: p line `u` parameter.
        v: p line `v` parameter.
        w: p line `w` parameter.
        erg: p line `erg` parameter.
        wgt: p line `wgt` parameter.
        tme: p line `tme` parameter.
    """

    blank: typing.Annotated[abc.Terminal, r' ']
    x: typing.Annotated[abc.Terminal, r'.{13}']
    y: typing.Annotated[abc.Terminal, r'.{13}']
    z: typing.Annotated[abc.Terminal, r'.{13}']
    u: typing.Annotated[abc.Terminal, r'.{13}']
    v: typing.Annotated[abc.Terminal, r'.{13}']
    w: typing.Annotated[abc.Terminal, r'.{13}']
    erg: typing.Annotated[abc.Terminal, r'.{13}']
    wgt: typing.Annotated[abc.Terminal, r'.{13}']
    tme: typing.Annotated[abc.Terminal, r'.{13}']
