import typing
import dataclasses

from ... import abc
from ..Line import Line


class J(Line):
    """
    Represents j lines.
    """

    pass


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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    blank: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:[0-2][1-9]|3[1-4])']
    pbl: typing.Annotated[abc.Terminal, r'.{10}']
    nsr: typing.Annotated[abc.Terminal, r'.{10}']
    ncl: typing.Annotated[abc.Terminal, r'.{10}']
    mat: typing.Annotated[abc.Terminal, r'.{10}']


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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    blank: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:[0-2][1-9]|3[1-4])']
    node: typing.Annotated[abc.Terminal, r'.{10}']
    nsr__nsx_nsf_nter: typing.Annotated[abc.Terminal, r'.{10}']
    ncl__ipt__ntyn_mtp_angle_branch: typing.Annotated[abc.Terminal, r'.{10}']
    mat__ncl: typing.Annotated[abc.Terminal, r'.{10}']
    ncp__mat: typing.Annotated[abc.Terminal, r'.{10}']


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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    blank: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:[0-2][1-9]|3[1-4])']
    node: typing.Annotated[abc.Terminal, r'.{10}']
    nsr__nsx_nsf_nter: typing.Annotated[abc.Terminal, r'.{10}']
    ipt__ntyn_mtp_angle_branch: typing.Annotated[abc.Terminal, r'.{10}']
    ncl__ipt: typing.Annotated[abc.Terminal, r'.{10}']
    mat__ncl: typing.Annotated[abc.Terminal, r'.{10}']
    ncp__mat: typing.Annotated[abc.Terminal, r'.{10}']


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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    blank: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:[0-2][1-9]|3[1-4])']
    node: typing.Annotated[abc.Terminal, r'.{10}']
    nsx_nsf_nter: typing.Annotated[abc.Terminal, r'.{10}']
    ntyn_mtp_angle_branch: typing.Annotated[abc.Terminal, r'.{10}']
    ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl: typing.Annotated[abc.Terminal, r'.{10}']
    mat: typing.Annotated[abc.Terminal, r'.{10}']
    ncp: typing.Annotated[abc.Terminal, r'.{10}']
