import typing
import decimal
import dataclasses

from ... import abc
from ..Group import Group
from .. import literal


class Rotation(Group):
    """
    Represents rotation groups.
    """

    pass


class Rotation_0(Rotation):
    """
    Represents rotation groups, form #0.

    Attributes:
        o1: rotation group `o1` parameter.
        o2: rotation group `o2` parameter.
        o3: rotation group `o3` parameter.
        xx: rotation group `xx` parameter.
        yx: rotation group `yx` parameter.
        zx: rotation group `zx` parameter.
        xy: rotation group `xy` parameter.
        yy: rotation group `yy` parameter.
        zy: rotation group `zy` parameter.
        xz: rotation group `xz` parameter.
        yz: rotation group `yz` parameter.
        zz: rotation group `zz` parameter.
        m: rotation group `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    o1: literal.Real | int | float | decimal.Decimal | str
    o2: literal.Real | int | float | decimal.Decimal | str
    o3: literal.Real | int | float | decimal.Decimal | str
    xx: literal.Real | int | float | decimal.Decimal | str
    yx: literal.Real | int | float | decimal.Decimal | str
    zx: literal.Real | int | float | decimal.Decimal | str
    xy: literal.Real | int | float | decimal.Decimal | str
    yy: literal.Real | int | float | decimal.Decimal | str
    zy: literal.Real | int | float | decimal.Decimal | str
    xz: literal.Real | int | float | decimal.Decimal | str
    yz: literal.Real | int | float | decimal.Decimal | str
    zz: literal.Real | int | float | decimal.Decimal | str
    m: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')


class Rotation_1(Rotation):
    """
    Represents rotation groups, form #1.

    Attributes:
        o1: rotation group `o1` parameter.
        o2: rotation group `o2` parameter.
        o3: rotation group `o3` parameter.
        xx: rotation group `xx` parameter.
        yx: rotation group `yx` parameter.
        zx: rotation group `zx` parameter.
        xy: rotation group `xy` parameter.
        yy: rotation group `yy` parameter.
        zy: rotation group `zy` parameter.
        m: rotation group `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    o1: literal.Real | int | float | decimal.Decimal | str
    o2: literal.Real | int | float | decimal.Decimal | str
    o3: literal.Real | int | float | decimal.Decimal | str
    xx: literal.Real | int | float | decimal.Decimal | str
    yx: literal.Real | int | float | decimal.Decimal | str
    zx: literal.Real | int | float | decimal.Decimal | str
    xy: literal.Real | int | float | decimal.Decimal | str
    yy: literal.Real | int | float | decimal.Decimal | str
    zy: literal.Real | int | float | decimal.Decimal | str
    m: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')


class Rotation_2(Rotation):
    """
    Represents rotation groups, form #2.

    Attributes:
        o1: rotation group `o1` parameter.
        o2: rotation group `o2` parameter.
        o3: rotation group `o3` parameter.
        xx: rotation group `xx` parameter.
        yx: rotation group `yx` parameter.
        zx: rotation group `zx` parameter.
        xy: rotation group `xy` parameter.
        yy: rotation group `yy` parameter.
        m: rotation group `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    o1: literal.Real | int | float | decimal.Decimal | str
    o2: literal.Real | int | float | decimal.Decimal | str
    o3: literal.Real | int | float | decimal.Decimal | str
    xx: literal.Real | int | float | decimal.Decimal | str
    yx: literal.Real | int | float | decimal.Decimal | str
    zx: literal.Real | int | float | decimal.Decimal | str
    xy: literal.Real | int | float | decimal.Decimal | str
    yy: literal.Real | int | float | decimal.Decimal | str
    m: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')


class Rotation_3(Rotation):
    """
    Represents rotation groups, form #3.

    Attributes:
        o1: rotation group `o1` parameter.
        o2: rotation group `o2` parameter.
        o3: rotation group `o3` parameter.
        xx: rotation group `xx` parameter.
        yx: rotation group `yx` parameter.
        zx: rotation group `zx` parameter.
        m: rotation group `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    o1: literal.Real | int | float | decimal.Decimal | str
    o2: literal.Real | int | float | decimal.Decimal | str
    o3: literal.Real | int | float | decimal.Decimal | str
    xx: literal.Real | int | float | decimal.Decimal | str
    yx: literal.Real | int | float | decimal.Decimal | str
    zx: literal.Real | int | float | decimal.Decimal | str
    m: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')


class Rotation_4(Rotation):
    """
    Represents rotation groups, form #4.

    Attributes:
        o1: rotation group `o1` parameter.
        o2: rotation group `o2` parameter.
        o3: rotation group `o3` parameter.
        m: rotation group `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    o1: literal.Real | int | float | decimal.Decimal | str
    o2: literal.Real | int | float | decimal.Decimal | str
    o3: literal.Real | int | float | decimal.Decimal | str
    m: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')
