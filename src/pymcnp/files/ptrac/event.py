"""
``event`` contains classes representing PTRAC events.

``event`` packages the ``Event`` class, providing an object-oriented,
importable interface for PTRAC event.
"""

from __future__ import annotations
from enum import Enum
import re

from ..utils import _parser
from ..utils import types
from ..utils import errors
from .header import Header


class Event:
    """
    ``Event`` represents PTRAC events.

    ``Event`` implements PTRAC events as a Python class. Its attributes store
    PTRAC event line parameters, and its methods provide entry points and
    endpoints for working with PTRAC. It represents the PTRAC event, i.e. the
    PTRAC J and P lines, syntax element.

    Attributes:
        next_type: Event type of the next event.
        type: Event type.
        node: Number of nodes in track from source.
        nsr: Source type.
        nxs: Blocks of descriptors of cross section tables.
        ntyn_mtp: Reaction type.
        nsf: Surface number.
        surface_angle: Angle with surface normal in degrees.
        nter: Termination type.
        branch: Event branch number.
        ipt: Particle type.
        ncl: Problem number of the cells.
        mat: Material numbers of the cells.
        ncp: Count of collisions per track.
        xxx: X coordinate of the particle position.
        yyy: Y coordinate of the particle position.
        zzz: Z coordinate of the particle position.
        uuu: Particle direction cosine with x axis.
        vvv: Particle direction cosine with y axis.
        www: Particle direction cosine with z axis.
        erg: Particle energy.
        wgt: Particle weight.
        tme: Time at the particles position.
    """

    class EventType(Enum):
        """
        ``EventType`` represents PTRAC event event-types.

        ``EventType`` implements PTRAC event event-types as a Python inner
        class. It enumerates event-type descriptoins and provides methods for
        casting strings to ``EventType`` instances. It represents the PTRAC
        event event-types syntax element, so ``Event`` depends on ``EventType``
        as an enum.
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
        def from_mcnp(cls, source: str):
            """
            ``from_mcnp`` generates ``EventType`` objects from PTRAC.

            ``from_mcnp`` constructs instances of ``EventType`` from PTRAC
            source strings, so it operates as a class constructor method
            and PTRAC parser helper function.

            Parameters:
                source: PTRAC for event event-type.

            Returns:
                ``EventType`` object.

            Raises:
                MCNPSemanticError: INVALID_EVENT_TYPE.
            """

            source = _parser.Preprocessor.process_ptrac(source)

            # Checking the source is numeric.
            if not re.match(r'-?\d+', source):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_TYPE)

            # Processing Type
            if int(source) not in [enum.value for enum in cls]:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_TYPE)

            return cls(int(source))

    class EventNters(Enum):
        """
        ``EventNters`` represents PTRAC event NTER variables.

        ``EventNters`` implements PTRAC event NTER variable as a Python inner
        class. It enumerates event-type descriptoins and provides methods for
        casting strings to ``EventNters`` instances. It represents the PTRAC
        event NTER variable syntax element, so ``Event`` depends on
        ``EventNters`` as an enum.
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
        def from_mcnp(cls, source: int):
            """
            ``from_mcnp`` generates ``EventNters`` objects from PTRAC.

            ``from_mcnp`` constructs instances of ``EventNters`` from PTRAC
            source strings, so it operates as a class constructor method
            and PTRAC parser helper function.

            Parameters:
                source: PTRAC for event NTER variable.

            Returns:
                ``EventNters`` object.

            Raises:
                MCNPSemanticError: INVALID_EVENT_NTER.
            """

            source = _parser.Preprocessor.process_ptrac(source)

            # Checking the source is numeric.
            if not re.match(r'\d+', source):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NTER)

            # Processing Type
            if int(source) not in [enum.value for enum in cls]:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NTER)

            return cls(int(source))

    def __init__(self):
        """
        ``__init__`` initializes ``Event``.
        """

        self.next_type: self.EventType = None
        self.type: self.EventType = None
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

    def set_type(self, event_type: EventType) -> None:
        """
        ``set_type`` stores PTRAC event type variables.

        ``set_type`` checks given arguments before assigning the given value
        to ``Event.type``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            type: Event type.

        Raises:
            MCNPSemanticError: INVALID_EVENT_TYPE.
        """

        if event_type is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_TYPE)

        self.type = event_type

    def set_node(self, node: int) -> None:
        """
        ``set_node`` stores PTRAC event node variables.

        ``set_node`` checks given arguments before assigning the given value
        to ``Event.node``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            node: Number of nodes in track from source.

        Raises:
            MCNPSemanticError: INVALID_EVENT_NODE.
        """

        if node is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NODE)

        self.node = node

    def set_nsr(self, nsr: int) -> None:
        """
        ``set_nsr`` stores PTRAC event source nsr variables.

        ``set_nsr`` checks given arguments before assigning the given value
        to ``Event.nsr``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            nsr: Source type.

        Raises:
            MCNPSemanticError: INVALID_EVENT_NSR.
        """

        if nsr is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NSR)

        self.nsr = nsr

    def set_nxs(self, nxs: float) -> None:
        """
        ``set_nxs`` stores PTRAC event source nxs variables.

        ``set_nxs`` checks given arguments before assigning the given value
        to ``Event.nxs``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            nxs: Blocks of descriptors of cross section tables.

        Raises:
            MCNPSemanticError: INVALID_EVENT_NXS.
        """

        if nxs is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NXS)

        self.nxs = nxs

    def set_ntyn_mtp(self, ntyn_mtp: int) -> None:
        """
        ``set_ntyn_mtp`` stores PTRAC event source ntyn_mtp variables.

        ``set_ntyn_mtp`` checks given arguments before assigning the given value
        to ``Event.ntyn_mtp``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            ntyn_mtp: Reaction type.

        Raises:
            MCNPSemanticError: INVALID_EVENT_NTYNMTP.
        """

        if ntyn_mtp is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NTYNMTP)

        self.ntyn_mtp = ntyn_mtp

    def set_nsf(self, nsf: int) -> None:
        """
        ``set_nsf`` stores PTRAC event source nsf variables.

        ``set_nsf`` checks given arguments before assigning the given value
        to ``Event.nsf``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            nsf: Surface number.

        Raises:
            MCNPSemanticError: INVALID_EVENT_NSF.
        """

        if nsf is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NSF)

        self.nsf = nsf

    def set_surface_angle(self, surface_angle: int) -> None:
        """
        ``set_surface_angle`` stores PTRAC event source surface_angle variables.

        ``set_surface_angle`` checks given arguments before assigning the given value
        to ``Event.surface_angle``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            surface_angle: Angle with surface normal in degrees.

        Raises:
            MCNPSemanticError: INVALID_EVENT_ANGLE.
        """

        if surface_angle is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_ANGLE)

        self.surface_angle = surface_angle

    def set_nter(self, nter: EventNters) -> None:
        """
        ``set_nter`` stores PTRAC event source nter variables.

        ``set_nter`` checks given arguments before assigning the given value
        to ``Event.nter``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            nter: Termination type.

        Raises:
            MCNPSemanticError: INVALID_EVENT_NTER.
        """

        if nter is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NTER)

        self.nter = nter

    def set_branch(self, branch: int) -> None:
        """
        ``set_branch`` stores PTRAC event source branch variables.

        ``set_branch`` checks given arguments before assigning the given value
        to ``Event.branch``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            branch: Event branch number.

        Raises:
            MCNPSemanticError: INVALID_EVENT_BRANCH.
        """

        if branch is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_BRANCH)

        self.branch = branch

    def set_ipt(self, ipt: int) -> None:
        """
        ``set_ipt`` stores PTRAC event source ipt variables.

        ``set_ipt`` checks given arguments before assigning the given value
        to ``Event.ipt``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            ipt: Particle type.

        Raises:
            MCNPSemanticError: INVALID_EVENT_IPT.
        """

        if ipt is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_IPT)

        self.ipt = ipt

    def set_ncl(self, ncl: int) -> None:
        """
        ``set_ncl`` stores PTRAC event source ncl variables.

        ``set_ncl`` checks given arguments before assigning the given value
        to ``Event.ncl``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            ncl: Problem number of the cells.

        Raises:
            MCNPSemanticError: INVALID_EVENT_NCL.
        """

        if ncl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NCL)

        self.ncl = ncl

    def set_mat(self, mat: int) -> None:
        """
        ``set_mat`` stores PTRAC event source mat variables.

        ``set_mat`` checks given arguments before assigning the given value
        to ``Event.mat``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            mat: Material numbers of the cells.

        Raises:
            MCNPSemanticError: INVALID_EVENT_MAT.
        """

        if mat is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_MAT)

        self.mat = mat

    def set_ncp(self, ncp: int) -> None:
        """
        ``set_ncp`` stores PTRAC event source ncp variables.

        ``set_ncp`` checks given arguments before assigning the given value
        to ``Event.ncp``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            ncp: Count of collisions per track.

        Raises:
            MCNPSemanticError: INVALID_EVENT_NCP.
        """

        if ncp is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NCP)

        self.ncp = ncp

    def set_xxx(self, xxx: float) -> None:
        """
        ``set_xxx`` stores PTRAC event source xxx variables.

        ``set_xxx`` checks given arguments before assigning the given value
        to ``Event.xxx``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            xxx: X coordinate of the particle position.

        Raises:
            MCNPSemanticError: INVALID_EVENT_XXX.
        """

        if xxx is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_XXX)

        self.xxx = xxx

    def set_yyy(self, yyy: float) -> None:
        """
        ``set_yyy`` stores PTRAC event source yyy variables.

        ``set_yyy`` checks given arguments before assigning the given value
        to ``Event.yyy``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            yyy: Y coordinate of the particle position.

        Raises:
            MCNPSemanticError: INVALID_EVENT_YYY.
        """

        if yyy is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_YYY)

        self.yyy = yyy

    def set_zzz(self, zzz: float) -> None:
        """
        ``set_zzz`` stores PTRAC event source zzz variables.

        ``set_zzz`` checks given arguments before assigning the given value
        to ``Event.zzz``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            zzz: Z coordinate of the particle position.

        Raises:
            MCNPSemanticError: INVALID_EVENT_ZZZ.
        """

        if zzz is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_ZZZ)

        self.zzz = zzz

    def set_uuu(self, uuu: float) -> None:
        """
        ``set_uuu`` stores PTRAC event source uuu variables.

        ``set_uuu`` checks given arguments before assigning the given value
        to ``Event.uuu``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            uuu: Particle direction cosine with x axis.

        Raises:
            MCNPSemanticError: INVALID_EVENT_UUU.
        """

        if uuu is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_UUU)

        self.uuu = uuu

    def set_vvv(self, vvv: float) -> None:
        """
        ``set_vvv`` stores PTRAC event source vvv variables.

        ``set_vvv`` checks given arguments before assigning the given value
        to ``Event.vvv``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            vvv: Particle direction cosine with y axis.

        Raises:
            MCNPSemanticError: INVALID_EVENT_VVV.
        """

        if vvv is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_VVV)

        self.vvv = vvv

    def set_www(self, www: float) -> None:
        """
        ``set_www`` stores PTRAC event source www variables.

        ``set_www`` checks given arguments before assigning the given value
        to ``Event.www``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            www: Particle direction cosine with z axis.

        Raises:
            MCNPSemanticError: INVALID_EVENT_WWW.
        """

        if www is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_WWW)

        self.www = www

    def set_erg(self, erg: float) -> None:
        """
        ``set_erg`` stores PTRAC event source erg variables.

        ``set_erg`` checks given arguments before assigning the given value
        to ``Event.erg``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            erg: Particle energy.

        Raises:
            MCNPSemanticError: INVALID_EVENT_ERG.
        """

        if erg is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_ERG)

        self.erg = erg

    def set_wgt(self, wgt: float) -> None:
        """
        ``set_wgt`` stores PTRAC event source wgt variables.

        ``set_wgt`` checks given arguments before assigning the given value
        to ``Event.wgt``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            wgt: Particle weight.

        Raises:
            MCNPSemanticError: INVALID_EVENT_WGT.
        """

        if wgt is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_WGT)

        self.wgt = wgt

    def set_tme(self, tme: float) -> None:
        """
        ``set_tme`` stores PTRAC event source tme variables.

        ``set_tme`` checks given arguments before assigning the given value to
        ``Event.tme``. If given an unrecognized argument, it raises semantic
        errors.

        Parameters:
            tme: Time at the particles position.

        Raises:
            MCNPSemanticError: INVALID_EVENT_TME.
        """

        if tme is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_TME)

        self.tme = tme

    @classmethod
    def from_mcnp(
        cls, source: str, header: Header, event_type: EventType, line: int = None
    ) -> tuple[Event, str]:
        """
        ``from_mcnp`` generates ``Event`` objects from PTRAC.

        ``from_mcnp`` constructs instances of ``Event`` from PTRAC source
        strings, so it operates as a class constructor method and PTRAC parser
        helper function.

        Parameters:
            source: PTRAC for event.
            header: PTRAC header.
            event_type: Event type.
            line: Line number.

        Returns:
            ``Event`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_EVENT, TOOLONG_EVENT.
        """

        event = cls()
        event.set_type(event_type)

        # Processing Line Number
        event.line = line

        source = _parser.Preprocessor.process_ptrac(source)
        lines = source.split('\n')
        if len(lines) != 2:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_EVENT)

        # Processing J-Line
        j_line = _parser.Parser(
            lines[0].split(' '), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_EVENT)
        )

        # Processing J2 (Next Event Type: 7)
        value = cls.EventType.from_mcnp(j_line.popl())
        if value is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NSR)
        event.next_type = value

        # Processing J2 (Node: 8)
        value = types.cast_fortran_integer(j_line.popl())
        event.set_node(value)

        # Processing J3
        match event_type:
            case cls.EventType.SOURCE:
                # (NSR: 9)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_nsr(value)

            case cls.EventType.SURFACE:
                # (NSF: 12)
                value = types.cast_fortran_real(j_line.popl())
                event.set_nsf(value)

            case cls.EventType.COLLISION:
                # (NXS: 10)
                value = types.cast_fortran_real(j_line.popl())
                event.set_nxs(value)

            case cls.EventType.TERMINAL:
                # (NTER: 14)
                value = cls.EventNter.cast_mcnp_nter(j_line.popl())
                event.set_nter(value)

            case cls.EventType.FLAG:
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
            case cls.EventType.SOURCE:
                pass

            case cls.EventType.SURFACE:
                # (Surface Angle: 13)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_surface_angle(value)

            case cls.EventType.COLLISION:
                # (NTYN/MTP: 11)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_ntyn_mtp(value)

            case cls.EventType.TERMINAL:
                # (Branch Number: 15)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_branch_number(value)

            case cls.EventType.FLAG:
                assert False

            case _:
                # (NTYN/MTP: 11)
                value = types.cast_fortran_integer(j_line.popl())
                event.set_ntyn_mtp(value)

        # Processing P-Line
        p_line = _parser.Parser(
            lines[1].split(' '), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_EVENT)
        )

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
        ``to_arguments`` makes dictionaries from ``Event`` objects.

        ``to_arguments`` creates Python dictionaries from ``Event`` objects, so
        it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual.

        Returns:
            Dictionary for ``Event`` object.
        """

        return {
            'type': self.type,
            'node': self.node,
            'nsr': self.nsr,
            'nxs': self.nxs,
            'ntyn_mtp': self.ntyn_mtp,
            'nsf': self.nsf,
            'surface_angle': self.surface_angle,
            'nter': self.nter,
            'branch': self.branch,
            'ipt': self.ipt,
            'ncl': self.ncl,
            'mat': self.mat,
            'ncp': self.ncp,
            'xxx': self.xxx,
            'yyy': self.yyy,
            'zzz': self.zzz,
            'uuu': self.uuu,
            'vvv': self.vvv,
            'www': self.www,
            'erg': self.erg,
            'wgt': self.wgt,
            'tme': self.tme,
        }
