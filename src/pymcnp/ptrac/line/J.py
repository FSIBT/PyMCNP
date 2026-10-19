import typing
import dataclasses

from ... import abc
from ..Line import Line


class J(Line):
    """
    Represents j lines.
    """


class J_0(J):
    """
    Represents j lines, form #0.

    Attributes:
        type: j line `type` parameter.
        pbl: j line `pbl` parameter.
        nsr: j line `nsr` parameter.
        ncl: j line `ncl` parameter.
        mat: j line `mat` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    blank: typing.Annotated[abc.Terminal, r' '] = dataclasses.field(kw_only=True)
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:[0-2][1-9]|3[1-4])'] = dataclasses.field(kw_only=True)
    pbl: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    nsr: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ncl: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    mat: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)


class J_1(J):
    """
    Represents j lines, form #1.

    Attributes:
        type: j line `type` parameter.
        node: j line `node` parameter.
        nsx_nsf_nter: j line `nsx_nsf_nter` parameter.
        ntyn_mtp_angle_branch: j line `ntyn_mtp_angle_branch` parameter.
        ncl: j line `ncl` parameter.
        mat: j line `mat` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    blank: typing.Annotated[abc.Terminal, r' '] = dataclasses.field(kw_only=True)
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:[0-2][1-9]|3[1-4])'] = dataclasses.field(kw_only=True)
    node: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    nsr__nsx_nsf_nter: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ncl__ipt__ntyn_mtp_angle_branch: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    mat__ncl: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ncp__mat: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)


class J_2(J):
    """
    Represents j lines, form #2.

    Attributes:
        type: j line `type` parameter.
        node: j line `node` parameter.
        nsx_nsf_nter: j line `nsx_nsf_nter` parameter.
        ntyn_mtp_angle_branch: j line `ntyn_mtp_angle_branch` parameter.
        ipt: j line `ipt` parameter.
        ncl: j line `ncl` parameter.
        mat: j line `mat` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    blank: typing.Annotated[abc.Terminal, r' '] = dataclasses.field(kw_only=True)
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:[0-2][1-9]|3[1-4])'] = dataclasses.field(kw_only=True)
    node: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    nsr__nsx_nsf_nter: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ipt__ntyn_mtp_angle_branch: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ncl__ipt: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    mat__ncl: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ncp__mat: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)


class J_3(J):
    """
    Represents j lines, form #3.

    Attributes:
        type: j line `type` parameter.
        node: j line `node` parameter.
        nsx_nsf_nter: j line `nsx_nsf_nter` parameter.
        ntyn_mtp_angle_branch: j line `ntyn_mtp_angle_branch` parameter.
        ipt: j line `ipt` parameter.
        ncl: j line `ncl` parameter.
        mat: j line `mat` parameter.
        ncp: j line `ncp` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    blank: typing.Annotated[abc.Terminal, r' '] = dataclasses.field(kw_only=True)
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:[0-2][1-9]|3[1-4])'] = dataclasses.field(kw_only=True)
    node: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    nsx_nsf_nter: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ntyn_mtp_angle_branch: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ipt: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ncl: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    mat: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    ncp: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
