import typing

import pandas

from ... import abc
from ..Block import Block


class Event(Block, abc.symbol.WithDataIter):
    """
    Represents event blocks.
    """

    if typing.TYPE_CHECKING:
        type: typing.Annotated[abc.Terminal, r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for rows.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for rows.

        Returns:
            Pandas dataframe for all rows.
        """

        yield (
            frame := pandas.DataFrame(
                {
                    'type': [type(self).__name__],
                    'PBL%I%NODE': [self.pbl_i_node.strip() if hasattr(self, 'pbl_i_node') and isinstance(self.pbl_i_node, str) else None],
                    'NSR': [self.nsr.strip() if hasattr(self, 'nsr') and isinstance(self.nsr, str) else None],
                    'NXS(2,IEX)': [self.nxs_2_iex.strip() if hasattr(self, 'nxs_2_iex') and isinstance(self.nxs_2_iex, str) else None],
                    'NTYN': [self.ntyn.strip() if hasattr(self, 'ntyn') and isinstance(self.ntyn, str) else None],
                    'PBL%I%MTP': [self.pbl_i_mtp.strip() if hasattr(self, 'pbl_i_mtp') and isinstance(self.pbl_i_mtp, str) else None],
                    'NSF(PBL%I%JSU)': [self.nsf_pbl_i_jsu.strip() if hasattr(self, 'nsf_pbl_i_jsu') and isinstance(self.nsf_pbl_i_jsu, str) else None],
                    'angle': [self.angle.strip() if hasattr(self, 'angle') and isinstance(self.angle, str) else None],
                    'NTER': [self.nter.strip() if hasattr(self, 'nter') and isinstance(self.nter, str) else None],
                    'branch_number': [self.branch_number.strip() if hasattr(self, 'branch_number') and isinstance(self.branch_number, str) else None],
                    'PBL%I%IPT': [self.pbl_i_ipt.strip() if hasattr(self, 'pbl_i_ipt') and isinstance(self.pbl_i_ipt, str) else None],
                    'NCL(PBL%I%ICL)': [self.ncl_pbl_i_icl.strip() if hasattr(self, 'ncl_pbl_i_icl') and isinstance(self.ncl_pbl_i_icl, str) else None],
                    'MAT(PBL%I%ICL)': [self.mat_pbl_i_icl.strip() if hasattr(self, 'mat_pbl_i_icl') and isinstance(self.mat_pbl_i_icl, str) else None],
                    'PBL%I%NCP': [self.pbl_i_ncp.strip() if hasattr(self, 'pbl_i_ncp') and isinstance(self.pbl_i_ncp, str) else None],
                    'PBL%R%X': [self.pbl_r_x.strip() if hasattr(self, 'pbl_r_x') and isinstance(self.pbl_r_x, str) else None],
                    'PBL%R%Y': [self.pbl_r_y.strip() if hasattr(self, 'pbl_r_y') and isinstance(self.pbl_r_y, str) else None],
                    'PBL%R%Z': [self.pbl_r_z.strip() if hasattr(self, 'pbl_r_z') and isinstance(self.pbl_r_z, str) else None],
                    'PBL%R%U': [self.pbl_r_u.strip() if hasattr(self, 'pbl_r_u') and isinstance(self.pbl_r_u, str) else None],
                    'PBL%R%V': [self.pbl_r_v.strip() if hasattr(self, 'pbl_r_v') and isinstance(self.pbl_r_v, str) else None],
                    'PBL%R%W': [self.pbl_r_w.strip() if hasattr(self, 'pbl_r_w') and isinstance(self.pbl_r_w, str) else None],
                    'PBL%R%ERG': [self.pbl_r_erg.strip() if hasattr(self, 'pbl_r_erg') and isinstance(self.pbl_r_erg, str) else None],
                    'PBL%R%WGT': [self.pbl_r_wgt.strip() if hasattr(self, 'pbl_r_wgt') and isinstance(self.pbl_r_wgt, str) else None],
                    'PBL%R%TME': [self.pbl_r_tme.strip() if hasattr(self, 'pbl_r_tme') and isinstance(self.pbl_r_tme, str) else None],
                }
            )
        )

        if returning:
            return frame

    @property
    def particle(self) -> abc.Terminal:
        """
        Event block particle.
        """

        return self.ncl_pbl_i_icl

    @property
    def material(self) -> abc.Terminal:
        """
        Event block material.
        """

        return self.mat_pbl_i_icl

    @property
    def position(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal]:
        """
        Event block position.
        """

        return (self.pbl_r_x, self.pbl_r_y, self.pbl_r_z)

    @property
    def zaid(self) -> abc.Terminal | None:
        """
        Event block target nuclide zaid.
        """

        return None

    @property
    def surface(self) -> abc.Terminal | None:
        """
        Event block surface.
        """

        return None

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Event block direction.
        """

        return None

    @property
    def energy(self) -> abc.Terminal | None:
        """
        Event block energy.
        """

        return None

    @property
    def weight(self) -> abc.Terminal | None:
        """
        Source event block weigth.
        """

        return None

    @property
    def time(self) -> abc.Terminal | None:
        """
        Source event block time.
        """

        return None


class EventSource(Event):
    """
    Represents source event blocks.
    """


class EventSource_1(EventSource):
    """
    Represents type #1 source event blocks.

    Attributes:
        blank_0: event block j line `r' '` symbol.
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme


class EventSource_4(EventSource):
    """
    Represents type #4 source event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #7 parameter.
        pbl_i_node: event block j line `PBL%I%NODE` parameter.
        nsr: event block j line `NSR` parameter.
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
    nsr: typing.Annotated[abc.Terminal, r'.{10}']
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme


class EventBank(Event):
    """
    Represents bank event blocks.
    """

    if typing.TYPE_CHECKING:
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

    @property
    def zaid(self) -> abc.Terminal:
        """
        Source event block target nuclide zaid.
        """

        return self.nxs_2_iex


class EventBank_1(EventBank):
    """
    Represents type #1 bank event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme


class EventBank_4(EventBank):
    """
    Represents type #4 bank event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #7 parameter.
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme


class EventSurface(Event):
    """
    Represents surface event blocks.
    """

    if typing.TYPE_CHECKING:
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

    @property
    def surface(self) -> abc.Terminal:
        """
        Source event block surface.
        """

        return self.nsf_pbl_i_jsu


class EventSurface_1(EventSurface):
    """
    Represents type #1 surface event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme


class EventSurface_4(EventSurface):
    """
    Represents type #4 surface event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #7 parameter.
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme


class EventCollision(Event):
    """
    Represents collision event blocks.
    """

    if typing.TYPE_CHECKING:
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

    @property
    def zaid(self) -> abc.Terminal:
        """
        Source event block target nuclide zaid.
        """

        return self.nxs_2_iex


class EventCollision_1(EventCollision):
    """
    Represents type #1 collision event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme


class EventCollision_4(EventCollision):
    """
    Represents type #4 collision event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #7 parameter.
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme


class EventTermination(Event):
    """
    Represents termination event blocks.
    """


class EventTermination_1(EventTermination):
    """
    Represents type #1 termination event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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
        type: event block j line variable id #7 parameter.
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme


class EventTermination_4(EventTermination):
    """
    Represents type #4 termination event blocks.

    Attributes:
        blank_0: event block `r' '` symbol.
        type: event block j line variable id #7 parameter.
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

    @property
    def direction(self) -> tuple[abc.Terminal, abc.Terminal, abc.Terminal] | None:
        """
        Source event block direction.
        """

        return (
            self.pbl_r_u,
            self.pbl_r_v,
            self.pbl_r_w,
        )

    @property
    def energy(self) -> abc.Terminal:
        """
        Source event block energy.
        """

        return self.pbl_r_erg

    @property
    def weight(self) -> abc.Terminal:
        """
        Source event block weigth.
        """

        return self.pbl_r_wgt

    @property
    def time(self) -> abc.Terminal:
        """
        Source event block time.
        """

        return self.pbl_r_tme
