"""
'event'
"""


from typing import Self
from enum import Enum

from .._utils import parser
from .._utils import types
from .header import Header


class Event:
    """
    'Event'
    """

    class EventTypes(Enum):
        """
        'EventTypes'
        """

        SOURCE = 1000
        BANK_DXTRAN_TRACK = 2001
        REJECTED_DXTRAN_TRACK = -2001
        BANK_ENERGY_SPLIT = 2002
        REJECTED_ENERGY_SPLIT = -2002
        BANK_WEIGHT_WINDOW_SURFACE_SPLIT = 2003
        REJECTED_WEIGHT_WINDOW_SURFACE_SPLIT = -2003
        BANK_WEIGHT_WINDOW_COLLISION_SPLIT = 2004
        REJECTED_WEIGHT_WINDOW_COLLISION_SPLIT = -2004
        BANK_FORCED_COLLISION_UNCOLLIDED_PART = 2005
        REJECTED_FORCED_COLLISION_UNCOLLIDED_PART = -2005
        BANK_IMPORTANCE_SPLIT = 2006
        REJECTED_IMPORTANCE_SPLIT = -2006
        BANK_NEUTRON_FROM_LIBRARY_PROTONS = 2007
        REJECTED_NEUTRON_FROM_LIBRARY_PROTONS = -2007
        BANK_PHOTON_FROM_NEUTRON = 2008
        REJECTED_PHOTON_FROM_NEUTRON = -2008
        BANK_PHOTON_FROM_DOUBLE_FLUORENSCENE = 2009
        REJECTED_PHOTON_FROM_DOUBLE_FLUORENSCENE = -2009
        BANK_PHOTON_FROM_ANNIHILATION = 2010
        REJECTED_PHOTON_FROM_ANNIHILATION = -2010
        BANK_ELECTRON_FROM_PHOTOELECTRIC = 2011
        REJECTED_ELECTRON_FROM_PHOTOELECTRIC = -2011
        BANK_ELECTRON_FROM_COMPTON = 2012
        REJECTED_ELECTRON_FROM_COMPTON = -2012
        BANK_ELECTRON_FROM_PAIR_PRODUCTION = 2013
        REJECTED_ELECTRON_FROM_PAIR_PRODUCTION = -2013
        BANK_AUGER_ELECTRON_FROM_PHOTON = 2014
        REJECTED_AUGER_ELECTRON_FROM_PHOTON = -2014
        BANK_POSITRON_FROM_PAIR_PRODUCTION = 2015
        REJECTED_POSITRON_FROM_PAIR_PRODUCTION = -2015
        BANK_BREMSSTRAHLUNG_FROM_ELECTRON = 2016
        REJECTED_BREMSSTRAHLUNG_FROM_ELECTRON = -2016
        BANK_KNOCK_ON_ELECTRON = 2017
        REJECTED_KNOCK_ON_ELECTRON = -2017
        BANK_PHOTON_FROM_ELECTRON = 2018
        REJECTED_PHOTON_FROM_ELECTRON = -2018
        BANK_PHOTON_FROM_NEUTRON_MULTIGROUP = 2019
        REJECTED_PHOTON_FROM_NEUTRON_MULTIGROUP = -2019
        BANK_NEUTRON_MULTIGROUP = 2020
        REJECTED_NEUTRON_MULTIGROUP = -2020
        BANK_NEUTRON_K_MULTIGROUP = 2021
        REJECTED_NEUTRON_K_MULTIGROUP = -2021
        BANK_PHOTO_FROM_PHOTON_MULTIGROUP = 2022
        REJECTED_PHOTO_FROM_PHOTON_MULTIGROUP = -2022
        BANK_ADJOINT_WEIGHT_SPLIT_MULTIGROUP = 2023
        REJECTED_ADJOINT_WEIGHT_SPLIT_MULTIGROUP = -2023
        BANK_WEIGHT_WINDOW_PSEUDO_COLLISION_SPLIT = 2024
        REJECTED_WEIGHT_WINDOW_PSEUDO_COLLISION_SPLIT = -2024
        BANK_SECONDARIES_FROM_PHOTONUCLEAR = 2025
        REJECTED_SECONDARIES_FROM_PHOTONUCLEAR = -2025
        BANK_DXTRAN_ANNIHILATION_PHOTON = 2026
        REJECTED_DXTRAN_ANNIHILATION_PHOTON = -2026
        BANK_LIGHT_IONS_FROM_NEUTRONS = 2030
        REJECTED_LIGHT_IONS_FROM_NEUTRONS = -2030
        BANK_LIGHT_IONS_FROM_PROTONS = 2031
        REJECTED_LIGHT_IONS_FROM_PROTONS = -2031
        BANK_LIBRARY_NEUTRONS_FROM_MODEL_NETURONS = 2032
        REJECTED_LIBRARY_NEUTRONS_FROM_MODEL_NETURONS = -2032
        BANK_SECONDARIES_FROM_INELASTIC_INTERACTIONS = 2033
        REJECTED_SECONDARIES_FROM_INELASTIC_INTERACTIONS = -2033
        BANK_SECONARIES_FORM_ELASTIC_INTERACTIONS = 2034
        REJECTED_SECONARIES_FORM_ELASTIC_INTERACTIONS = -2034
        SURFACE = 3000
        COLLISION = 4000
        TERMINAL = 5000
        FLAG = 9000

        @classmethod
        def cast_mcnp_event_types(cls, string: str):
            """
            'cast_mcnp_event_types'
            """

            try:
                return cls(int(string))
            except ValueError:
                return None

    class EventNters(Enum):
        """
        'EventNters'
        """

        ESCAPE = 1
        ENERGY_CUTOFF = 2
        TIME_CUTOFF = 3
        WEIGHT_WINDOW = 4
        CELL_IMPORTANCE = 5
        WEIGHT_CUTOFF = 6
        ENERGY_IMPORTANCE = 7
        DXTRAN = 8
        FORCED_COLLISION = 9
        EXPONENTIAL_TRANSFROM = 10
        NTER_11 = 11
        NTER_12 = 12
        NTER_13 = 13
        NTER_14 = 14
        NTER_15 = 15
        NTER_16 = 16
        NTER_17 = 17

        @classmethod
        def cast_mcnp_nter(cls, string: int) -> Self:
            """
            'cast_mcnp_nter'
            """

            try:
                return cls(string)
            except ValueError:
                return None

    def __init__(self) -> Self:
        """
        '__init__'
        """

        self.next_type: self.EventTypes = None

        self.type: self.EventTypes = None
        self.node: int = None
        self.nsr: int = None
        self.nxs: float = None
        self.ntyn_mtp: int = None
        self.nsf: int = None
        self.surface_angle: int = None
        self.nter: self.EventNtrs = None
        self.branch: int = None
        self.ipt: int = None
        self.ncl: int = None
        self.mat: int = None
        self.ncp: int = None
        self.xxx: float = None
        self.yyy: float = None
        self.zzz: float = None
        self.uuu: float = None
        self.vvv: float = None
        self.www: float = None
        self.erg: float = None
        self.wgt: float = None
        self.tme: float = None

    def set_type(self, event_type: EventTypes) -> None:
        """
        'set_type'
        """

        if event_type is None:
            raise ValueError

        self.type = event_type

    def set_node(self, node: int) -> None:
        """
        'set_node'
        """

        if node is None:
            raise ValueError

        self.node = node

    def set_nsr(self, nsr: int) -> None:
        """
        'set_nsr'
        """

        if nsr is None:
            raise ValueError

        self.nsr = nsr

    def set_nxs(self, nxs: float) -> None:
        """
        'set_nxs'
        """

        if nxs is None:
            raise ValueError

        self.nxs = nxs

    def set_ntyn_mtp(self, ntyn_mtp: int) -> None:
        """
        'set_ntyn_mtp'
        """

        if ntyn_mtp is None:
            raise ValueError

        self.ntyn_mtp = ntyn_mtp

    def set_nsf(self, nsf: int) -> None:
        """
        'set_nsf'
        """

        if nsf is None:
            raise ValueError

        self.nsf = nsf

    def set_surface_angle(self, surface_angle: int) -> None:
        """
        'set_surface_angle'
        """

        if surface_angle is None:
            raise ValueError

        self.surface_angle = surface_angle

    def set_nter(self, nter: EventNters) -> None:
        """
        'set_nter'
        """

        if nter is None:
            raise ValueError

        self.nter = nter

    def set_branch(self, branch: int) -> None:
        """
        'set_branch'
        """

        if branch is None:
            raise ValueError

        self.branch = branch

    def set_ipt(self, ipt: int) -> None:
        """
        'set_ipt'
        """

        if ipt is None:
            raise ValueError

        self.ipt = ipt

    def set_ncl(self, ncl: int) -> None:
        """
        'set_ncl'
        """

        if ncl is None:
            raise ValueError

        self.ncl = ncl

    def set_mat(self, mat: int) -> None:
        """
        'set_mat'
        """

        if mat is None:
            raise ValueError

        self.mat = mat

    def set_ncp(self, ncp: int) -> None:
        """
        'set_ncp'
        """

        if ncp is None:
            raise ValueError

        self.ncp = ncp

    def set_xxx(self, xxx: float) -> None:
        """
        'set_xxx'
        """

        if xxx is None:
            raise ValueError

        self.xxx = xxx

    def set_yyy(self, yyy: float) -> None:
        """
        'set_yyy'
        """

        if yyy is None:
            raise ValueError

        self.yyy = yyy

    def set_zzz(self, zzz: float) -> None:
        """
        'set_zzz'
        """

        if zzz is None:
            raise ValueError

        self.zzz = zzz

    def set_uuu(self, uuu: float) -> None:
        """
        'set_uuu'
        """

        if uuu is None:
            raise ValueError

        self.uuu = uuu

    def set_vvv(self, vvv: float) -> None:
        """
        'set_vvv'
        """

        if vvv is None:
            raise ValueError

        self.vvv = vvv

    def set_www(self, www: float) -> None:
        """
        'set_www'
        """

        if www is None:
            raise ValueError

        self.www = www

    def set_erg(self, erg: float) -> None:
        """
        'set_erg'
        """

        if erg is None:
            raise ValueError

        self.erg = erg

    def set_wgt(self, wgt: float) -> None:
        """
        'set_wgt'
        """

        if wgt is None:
            raise ValueError

        self.wgt = wgt

    def set_tme(self, tme: float) -> None:
        """
        'set_tme'
        """

        if tme is None:
            raise ValueError

        self.tme = tme

    @classmethod
    def from_mcnp(
        cls, source: str, header: Header, event_type: EventTypes
    ) -> tuple[Self, str]:
        """
        'from_mcnp'
        """

        event = cls()
        event.set_type(event_type)

        lines = source.split("\n")
        if len(lines) != 2:
            raise SyntaxError

        # Processing J-Line
        j_line = parser.Parser(SyntaxError).from_string(lines[0], " ")

        # Processing J2 (Next Event Type: 7)
        value = cls.EventTypes.cast_mcnp_event_types(j_line.popl())
        if value is None:
            raise ValueError
        event.next_type = value

        # Processing J2 (Node: 8)
        value = types.cast_fortran_integer(j_line.popl())
        event.set_node(value)

        # Processing J3
        match event_type:
            case cls.EventTypes.SOURCE:
                # (NSR: 9)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_nsr(value)

            case cls.EventTypes.SURFACE:
                # (NSF: 12)
                value = types.cast_fortran_real(j_line.popl())
                event.set_nsf(value)

            case cls.EventTypes.COLLISION:
                # (NXS: 10)
                value = types.cast_fortran_real(j_line.popl())
                event.set_nxs(value)

            case cls.EventTypes.TERMINAL:
                # (NTER: 14)
                value = cls.EventNter.cast_mcnp_nter(j_line.popl())
                event.set_nter(value)

            case cls.EventTypes.FLAG:
                assert False

            case _:
                # (NXS: 10)
                value = types.cast_fortran_real(j_line.popl())
                event.set_nxs(value)

        # Processing Type Dependent Entries
        match header.numbers[1:12]:
            case [5, 3, 6, 3, 6, 3, 6, 3, 6, 3]:
                # Type 1

                # Processing J5/J6 (MAT: 18)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_mat(value)

                # Processing J4/J5 (NCL: 17)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_ncl(value)

            case [6, 3, 7, 3, 7, 3, 7, 3, 7, 3]:
                # Type 2

                # Processing J6/J7 (MAT: 18)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_mat(value)

                # Processing J5/J6 (NCL: 17)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_ncl(value)

                # Processing J4/J5 (IPT: 16)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_ipt(value)

            case [6, 9, 7, 9, 7, 9, 7, 9, 7, 9]:
                # Type 3

                # Processing J6/J7 (NCP: 19)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_ncp(value)

                # Processing J5/J6 (MAT: 18)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_mat(value)

                # Processing J4/J5 (NCL: 17)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_ncl(value)

            case [7, 9, 8, 9, 8, 9, 8, 9, 8, 9]:
                # Type 4

                # Processing J7/J8 (NCP: 19)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_ncp(value)

                # Processing J6/J7 (MAT: 18)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_mat(value)

                # Processing J5/J6 (NCL: 17)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_ncl(value)

                # Processing J4/J5 (IPT: 16)
                value = types.cast_fortran_integer(j_line.popr())
                event.set_ipt(value)

        # Processing J4
        match event_type:
            case cls.EventTypes.SOURCE:
                pass

            case cls.EventTypes.SURFACE:
                # (Surface Angle: 13)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_surface_angle(value)

            case cls.EventTypes.COLLISION:
                # (NTYN/MTP: 11)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_ntyn_mtp(value)

            case cls.EventTypes.TERMINAL:
                # (Branch Number: 15)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_branch_number(value)

            case cls.EventTypes.FLAG:
                assert False

            case _:
                # (NTYN/MTP: 11)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_ntyn_mtp(value)

        # Processing P-Line
        p_line = parser.Parser(SyntaxError).from_string(lines[1], " ")

        # Processing P1 (xxx: 20)
        value = types.cast_fortran_real(p_line.popl())
        event.set_xxx(value)

        # Processing P2 (yyy: 21)
        value = types.cast_fortran_real(p_line.popl())
        event.set_yyy(value)

        # Processing P3 (zzz: 22)
        value = types.cast_fortran_real(p_line.popl())
        event.set_zzz(value)

        # Processing Type Dependent Entries
        if header.numbers[1:12] in {
            (6, 9, 7, 9, 7, 9, 7, 9, 7, 9),
            (7, 9, 8, 9, 8, 9, 8, 9, 8, 9),
        }:
            # Processing P4 (uuu: 23)
            value = types.cast_fortran_real(p_line.popl())
            event.set_uuu(value)

            # Processing P5 (vvv: 24)
            value = types.cast_fortran_real(p_line.popl())
            event.set_vvv(value)

            # Processing P6 (www: 25)
            value = types.cast_fortran_real(p_line.popl())
            event.set_www(value)

            # Processing P7 (erg: 26)
            value = types.cast_fortran_real(p_line.popl())
            event.set_erg(value)

            # Processing P8 (wgt: 27)
            value = types.cast_fortran_real(p_line.popl())
            event.set_wgt(value)

            # Processing P9 (tme: 28)
            value = types.cast_fortran_real(p_line.popl())
            event.set_tme(value)

        return event

    def to_arguments(self) -> dict:
        """
        'to_arguments'
        """

        return {
            "type": self.type,
            "node": self.node,
            "nsr": self.nsr,
            "nxs": self.nxs,
            "ntyn_mtp": self.ntyn_mtp,
            "nsf": self.nsf,
            "surface_angle": self.surface_angle,
            "nter": self.nter,
            "branch": self.branch,
            "ipt": self.ipt,
            "ncl": self.ncl,
            "mat": self.mat,
            "ncp": self.ncp,
            "xxx": self.xxx,
            "yyy": self.yyy,
            "zzz": self.zzz,
            "uuu": self.uuu,
            "vvv": self.vvv,
            "www": self.www,
            "erg": self.erg,
            "wgt": self.wgt,
            "tme": self.tme,
        }
