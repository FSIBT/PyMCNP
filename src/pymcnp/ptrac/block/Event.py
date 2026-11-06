import typing

from ... import abc
from ..Block import Block


class Event(Block):
    """
    Represents event blocks.
    """


class EventSource(Event):
    """
    Represents source event blocks.
    """


class EventSource_1(EventSource):
    """
    Represents type #1 source event blocks.

    Attributes:
        blank_0: event block j line `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nsr: event block j line `NSR` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block p line  `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nsr: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventSource_2(EventSource):
    """
    Represents type #2 source event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nsr: event block j line `NSR` parameter.
        pbl_i_ipt: event block j line `PBL%I%IPT` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nsr: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventSource_3(EventSource):
    """
    Represents type #3 source event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nsr: event block j line `NSR` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nsr: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']


class EventSource_4(EventSource):
    """
    Represents type #4 source event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nsr: event block j line `NSR` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nsr: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']


class EventBank(Event):
    """
    Represents bank event blocks.
    """


class EventBank_1(EventBank):
    """
    Represents type #1 bank event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nxs_2_iex: event block j line `NXS(2,IEX)` parameter.
        ntyn: event block j line `NTYN` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nxs_2_iex: typing.Annotated[abc.Terminal, r'.{10}']
    ntyn: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventBank_2(EventBank):
    """
    Represents type #2 bank event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nxs_2_iex: event block j line `NXS(2,IEX)` parameter.
        ntyn: event block j line `NTYN` parameter.
        pbl_i_ipt: event block j line `PBL%I%IPT` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nxs_2_iex: typing.Annotated[abc.Terminal, r'.{10}']
    ntyn: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventBank_3(EventBank):
    """
    Represents type #3 bank event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nxs_2_iex: event block j line `NXS(2,IEX)` parameter.
        ntyn: event block j line `NTYN` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nxs_2_iex: typing.Annotated[abc.Terminal, r'.{10}']
    ntyn: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']


class EventBank_4(EventBank):
    """
    Represents type #4 bank event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nxs_2_iex: event block j line `NXS(2,IEX)` parameter.
        ntyn: event block j line `NTYN` parameter.
        pbl_i_ipt: event block j line `PBL%I%IPT` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nxs_2_iex: typing.Annotated[abc.Terminal, r'.{10}']
    ntyn: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']


class EventSurface(Event):
    """
    Represents surface event blocks.
    """


class EventSurface_1(EventSurface):
    """
    Represents type #1 surface event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nsf_pbl_i_jsu: event block j line `NSF(PBL%I%JSU)` parameter.
        angle: event block j line variable id #13 parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nsf_pbl_i_jsu: typing.Annotated[abc.Terminal, r'.{10}']
    angle: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventSurface_2(EventSurface):
    """
    Represents type #2 surface event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nsf_pbl_i_jsu: event block j line `NSF(PBL%I%JSU)` parameter.
        angle: event block j line variable id #13 parameter.
        pbl_i_ipt: event block j line `PBL%I%IPT` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nsf_pbl_i_jsu: typing.Annotated[abc.Terminal, r'.{10}']
    angle: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventSurface_3(EventSurface):
    """
    Represents type #3 surface event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nsf_pbl_i_jsu: event block j line `NSF(PBL%I%JSU)` parameter.
        angle: event block j line variable id #13 parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nsf_pbl_i_jsu: typing.Annotated[abc.Terminal, r'.{10}']
    angle: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']


class EventSurface_4(EventSurface):
    """
    Represents type #4 surface event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nsf_pbl_i_jsu: event block j line `NSF(PBL%I%JSU)` parameter.
        angle: event block j line variable id #13 parameter.
        pbl_i_ipt: event block j line `PBL%I%IPT` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nsf_pbl_i_jsu: typing.Annotated[abc.Terminal, r'.{10}']
    angle: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']


class EventCollision(Event):
    """
    Represents collision event blocks.
    """


class EventCollision_1(EventCollision):
    """
    Represents type #1 collision event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nxs_2_iex: event block j line `NXS(2,IEX)` parameter.
        pbl_i_mtp: event block j line `PBL%I%MTP` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nxs_2_iex: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_mtp: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventCollision_2(EventCollision):
    """
    Represents type #2 collision event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nxs_2_iex: event block j line `NXS(2,IEX)` parameter.
        pbl_i_mtp: event block j line `PBL%I%MTP` parameter.
        pbl_i_ipt: event block j line `PBL%I%IPT` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nxs_2_iex: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_mtp: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventCollision_3(EventCollision):
    """
    Represents type #3 collision event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nxs_2_iex: event block j line `NXS(2,IEX)` parameter.
        pbl_i_mtp: event block j line `PBL%I%MTP` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nxs_2_iex: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_mtp: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']


class EventCollision_4(EventCollision):
    """
    Represents type #4 collision event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nxs_2_iex: event block j line `NXS(2,IEX)` parameter.
        pbl_i_mtp: event block j line `PBL%I%MTP` parameter.
        pbl_i_ipt: event block j line `PBL%I%IPT` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nxs_2_iex: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_mtp: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']


class EventTermination(Event):
    """
    Represents termination event blocks.
    """


class EventTermination_1(EventTermination):
    """
    Represents type #1 termination event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nter: event block j line `NTER` parameter.
        branch_number: event block j line variable id #15 parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nter: typing.Annotated[abc.Terminal, r'.{10}']
    branch_number: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventTermination_2(EventTermination):
    """
    Represents type #2 termination event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nter: event block j line `NTER` parameter.
        branch_number: event block j line variable id #15 parameter.
        pbl_i_ipt: event block j line `PBL%I%IPT` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nter: typing.Annotated[abc.Terminal, r'.{10}']
    branch_number: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']


class EventTermination_3(EventTermination):
    """
    Represents type #3 termination event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nter: event block j line `NTER` parameter.
        branch_number: event block j line variable id #15 parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nter: typing.Annotated[abc.Terminal, r'.{10}']
    branch_number: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']


class EventTermination_4(EventTermination):
    """
    Represents type #4 termination event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #1 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nter: event block j line `NTER` parameter.
        branch_number: event block j line variable id #15 parameter.
        pbl_i_ipt: event block j line `PBL%I%IPT` parameter.
        ncl_pbl_i_icl: event block j line `NCL(PBL%I%ICL)` parameter.
        mat_pbl_i_icl: event block j line `MAT(PBL%I%ICL)` parameter.
        pbl_i_ncp: event block j line `PBL%I%NCP` parameter.
        newline: event block `r'\\n'` symbol.
        blank_1: event block `r' '` symbol.
        pbl_r_x: event block p line `PBL%R%X` parameter.
        pbl_r_y: event block p line `PBL%R%Y` parameter.
        pbl_r_z: event block p line `PBL%R%Z` parameter.
        pbl_r_u: event block p line `PBL%R%U` parameter.
        pbl_r_v: event block p line `PBL%R%V` parameter.
        pbl_r_w: event block p line `PBL%R%W` parameter.
        pbl_r_erg: event block p line `PBL%R%ERG` parameter.
        pbl_r_wgt: event block p line `PBL%R%WGT` parameter.
        pbl_r_tme: event block p line `PBL%R%TME` parameter.
    """

    blank_0: typing.Annotated[abc.Terminal, r' ']
    type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
    pbl_i_node: typing.Annotated[abc.Terminal, r'.{10}']
    nter: typing.Annotated[abc.Terminal, r'.{10}']
    branch_number: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ipt: typing.Annotated[abc.Terminal, r'.{10}']
    ncl_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    mat_pbl_i_icl: typing.Annotated[abc.Terminal, r'.{10}']
    pbl_i_ncp: typing.Annotated[abc.Terminal, r'.{10}']
    newline: typing.Annotated[abc.Terminal, r'\n']
    blank_1: typing.Annotated[abc.Terminal, r' ']
    pbl_r_x: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_y: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_z: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_u: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_v: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_w: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_erg: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_wgt: typing.Annotated[abc.Terminal, r'.{13}']
    pbl_r_tme: typing.Annotated[abc.Terminal, r'.{13}']
