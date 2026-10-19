import typing
import dataclasses

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

    blank: typing.Annotated[abc.Terminal, r' '] = dataclasses.field(kw_only=True)
    x: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    y: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    z: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)


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

    blank: typing.Annotated[abc.Terminal, r' '] = dataclasses.field(kw_only=True)
    x: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    y: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    z: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    u: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    v: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    w: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    erg: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    wgt: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)
    tme: typing.Annotated[abc.Terminal, r'.{13}'] = dataclasses.field(kw_only=True)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)
