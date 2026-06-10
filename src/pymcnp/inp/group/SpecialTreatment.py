import typing
import decimal
import dataclasses

from ... import abc
from ..Group import Group
from .. import literal


class SpecialTreatment(Group):
    """
    Represents specialtreatment groups.
    """

    pass


class SpecialTreatment_0(SpecialTreatment):
    """
    Represents specialtreatment groups, form #0.

    Attributes:
        id: specialtreatment group `FRV` symbol.
        v1: specialtreatment group `v1` parameter.
        v2: specialtreatment group `v2` parameter.
        v3: specialtreatment group `v3` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'FRV'] | str = abc.Terminal[r'FRV']('FRV')
    v1: literal.Real | int | float | decimal.Decimal | str
    v2: literal.Real | int | float | decimal.Decimal | str
    v3: literal.Real | int | float | decimal.Decimal | str


class SpecialTreatment_1(SpecialTreatment):
    """
    Represents specialtreatment groups, form #1.

    Attributes:
        id: specialtreatment group `GEB` symbol.
        a: specialtreatment group `a` parameter.
        b: specialtreatment group `b` parameter.
        c: specialtreatment group `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'GEB'] | str = abc.Terminal[r'GEB']('GEB')
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
    c: literal.Real | int | float | decimal.Decimal | str


class SpecialTreatment_2(SpecialTreatment):
    """
    Represents specialtreatment groups, form #2.

    Attributes:
        id: specialtreatment group `TMC` symbol.
        a: specialtreatment group `a` parameter.
        b: specialtreatment group `b` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'TMC'] | str = abc.Terminal[r'TMC']('TMC')
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str


class SpecialTreatment_3(SpecialTreatment):
    """
    Represents specialtreatment groups, form #3.

    Attributes:
        id: specialtreatment group `INC` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'INC'] | str = abc.Terminal[r'INC']('INC')


class SpecialTreatment_4(SpecialTreatment):
    """
    Represents specialtreatment groups, form #4.

    Attributes:
        id: specialtreatment group `ICD` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'ICD'] | str = abc.Terminal[r'ICD']('ICD')


class SpecialTreatment_5(SpecialTreatment):
    """
    Represents specialtreatment groups, form #5.

    Attributes:
        id: specialtreatment group `SCX` symbol.
        k: specialtreatment group `k` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'SCX'] | str = abc.Terminal[r'SCX']('SCX')
    k: literal.Integer | int | str


class SpecialTreatment_6(SpecialTreatment):
    """
    Represents specialtreatment groups, form #6.

    Attributes:
        id: specialtreatment group `SCD` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'SCD'] | str = abc.Terminal[r'SCD']('SCD')


class SpecialTreatment_7(SpecialTreatment):
    """
    Represents specialtreatment groups, form #7.

    Attributes:
        id: specialtreatment group `ELC` symbol.
        c: specialtreatment group `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'ELC'] | str = abc.Terminal[r'ELC']('ELC')
    c: literal.Integer | int | str


class SpecialTreatment_8(SpecialTreatment):
    """
    Represents specialtreatment groups, form #8.

    Attributes:
        id: specialtreatment group `CAP` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'CAP'] | str = abc.Terminal[r'CAP']('CAP')


class SpecialTreatment_9(SpecialTreatment):
    """
    Represents specialtreatment groups, form #9.

    Attributes:
        id: specialtreatment group `TAG` symbol.
        a: specialtreatment group `a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'TAG'] | str = abc.Terminal[r'TAG']('TAG')
    a: literal.Integer | int | str


class SpecialTreatment_10(SpecialTreatment):
    """
    Represents specialtreatment groups, form #10.

    Attributes:
        id: specialtreatment group `LET` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'LET'] | str = abc.Terminal[r'LET']('LET')


class SpecialTreatment_11(SpecialTreatment):
    """
    Represents specialtreatment groups, form #11.

    Attributes:
        id: specialtreatment group `ROC` symbol.
        nhb: specialtreatment group `nhb` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'ROC'] | str = abc.Terminal[r'ROC']('ROC')
    nhb: literal.Real | int | float | decimal.Decimal | str


class SpecialTreatment_12(SpecialTreatment):
    """
    Represents specialtreatment groups, form #12.

    Attributes:
        id: specialtreatment group `PDS` symbol.
        c: specialtreatment group `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'PDS'] | str = abc.Terminal[r'PDS']('PDS')
    c: literal.Integer | int | str


class SpecialTreatment_13(SpecialTreatment):
    """
    Represents specialtreatment groups, form #13.

    Attributes:
        id: specialtreatment group `FFT` symbol.
        lkji: specialtreatment group `lkji` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'FFT'] | str = abc.Terminal[r'FFT']('FFT')
    lkji: typing.Annotated[abc.Terminal, r'[01]{4}'] | str


class SpecialTreatment_14(SpecialTreatment):
    """
    Represents specialtreatment groups, form #14.

    Attributes:
        id: specialtreatment group `COM` symbol.
        t: specialtreatment group `t` parameter.
        a: specialtreatment group `a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'COM'] | str = abc.Terminal[r'COM']('COM')
    t: literal.Integer | int | str
    a: literal.Integer | int | str


class SpecialTreatment_15(SpecialTreatment):
    """
    Represents specialtreatment groups, form #15.

    Attributes:
        id: specialtreatment group `MGC` symbol.
        fg: specialtreatment group `fg` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'MGC'] | str = abc.Terminal[r'MGC']('MGC')
    fg: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')


class SpecialTreatment_16(SpecialTreatment):
    """
    Represents specialtreatment groups, form #16.

    Attributes:
        id: specialtreatment group `FNS` symbol.
        nt: specialtreatment group `nt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'FNS'] | str = abc.Terminal[r'FNS']('FNS')
    nt: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')


class SpecialTreatment_17(SpecialTreatment):
    """
    Represents specialtreatment groups, form #17.

    Attributes:
        id: specialtreatment group `LCS` symbol.
        lo: specialtreatment group `lo` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'LCS'] | str = abc.Terminal[r'LCS']('LCS')
    lo: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')
