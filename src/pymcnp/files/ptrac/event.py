"""
``event`` contains classes representing PTRAC events.

``event`` packages the ``Event`` class, providing an object-oriented,
importable interface for PTRAC event.
"""

from __future__ import annotations
from typing import Final
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

        @staticmethod
        def from_mcnp(source: str):
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
            if int(source) not in [enum.value for enum in Event.EventType]:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_TYPE)

            return Event.EventType(int(source))

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

        @staticmethod
        def from_mcnp(source: int):
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
            if int(source) not in [enum.value for enum in Event.EventNters]:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_EVENT_NTER)

            return Event.EventNters(int(source))

    def __init__(
        self,
        next_type,
        event_type,
        node,
        nsr,
        nxs,
        ntyn_mtp,
        nsf,
        surface_angle,
        nter,
        branch,
        ipt,
        ncl,
        mat,
        ncp,
        xxx,
        yyy,
        zzz,
        uuu,
        vvv,
        www,
        erg,
        wgt,
        tme,
    ):
        """
        ``__init__`` initializes ``Event``.

        Parameters:
            event_type: Event type.
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

        Raises:
            MCNPSemanticError: INVALID_EVENT_TYPE.
            MCNPSemanticError: INVALID_EVENT_NODE.
            MCNPSemanticError: INVALID_EVENT_NSR.
            MCNPSemanticError: INVALID_EVENT_NXS.
            MCNPSemanticError: INVALID_EVENT_NTYNMTP.
            MCNPSemanticError: INVALID_EVENT_NSF.
            MCNPSemanticError: INVALID_EVENT_ANGLE.
            MCNPSemanticError: INVALID_EVENT_NTER.
            MCNPSemanticError: INVALID_EVENT_BRANCH.
            MCNPSemanticError: INVALID_EVENT_IPT.
            MCNPSemanticError: INVALID_EVENT_NCL.
            MCNPSemanticError: INVALID_EVENT_MAT.
            MCNPSemanticError: INVALID_EVENT_NCP.
            MCNPSemanticError: INVALID_EVENT_XXX.
            MCNPSemanticError: INVALID_EVENT_YYY.
            MCNPSemanticError: INVALID_EVENT_ZZZ.
            MCNPSemanticError: INVALID_EVENT_UUU.
            MCNPSemanticError: INVALID_EVENT_VVV.
            MCNPSemanticError: INVALID_EVENT_WWW.
            MCNPSemanticError: INVALID_EVENT_ERG.
            MCNPSemanticError: INVALID_EVENT_WGT.
            MCNPSemanticError: INVALID_EVENT_TME.
        """

        # TODO: Add error checking here!

        self.next_type: Final[self.EventType] = next_type
        self.event_type: Final[self.EventType] = event_type
        self.node: Final[int] = node
        self.nsr: Final[int] = nsr
        self.nxs: Final[float] = nxs
        self.ntyn_mtp: Final[int] = ntyn_mtp
        self.nsf: Final[int] = nsf
        self.surface_angle: Final[int] = surface_angle
        self.nter: Final[self.EventNtrs] = nter
        self.branch: Final[int] = branch
        self.ipt: Final[int] = ipt
        self.ncl: Final[int] = ncl
        self.mat: Final[int] = mat
        self.ncp: Final[int] = ncp
        self.xxx: Final[float] = xxx
        self.yyy: Final[float] = yyy
        self.zzz: Final[float] = zzz
        self.uuu: Final[float] = uuu
        self.vvv: Final[float] = vvv
        self.www: Final[float] = www
        self.erg: Final[float] = erg
        self.wgt: Final[float] = wgt
        self.tme: Final[float] = tme

    @staticmethod
    def from_mcnp(
        source: str, header: Header, event_type: EventType, line: int = None
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

        next_type = None
        event_type = None
        node = None
        nsr = None
        nxs = None
        ntyn_mtp = None
        nsf = None
        surface_angle = None
        nter = None
        branch = None
        ipt = None
        ncl = None
        mat = None
        ncp = None
        xxx = None
        yyy = None
        zzz = None
        uuu = None
        vvv = None
        www = None
        erg = None
        wgt = None
        tme = None

        source = _parser.Preprocessor.process_ptrac(source)
        lines = source.split('\n')
        if len(lines) != 2:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_EVENT)

        # Processing J-Line
        j_line = _parser.Parser(
            lines[0].split(' '), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_EVENT)
        )

        # Processing J2 (Next Event Type: 7)
        next_type = Event.EventType.from_mcnp(j_line.popl())

        # Processing J2 (Node: 8)
        node = types.McnpInteger.from_mcnp(j_line.popl())

        # Processing J3
        match event_type:
            case Event.EventType.SOURCE:
                # (NSR: 9)
                nsr = types.McnpInteger.from_mcnp(j_line.popl())

            case Event.EventType.SURFACE:
                # (NSF: 12)
                nsf = types.McnpReal.from_mcnp(j_line.popl())

            case Event.EventType.COLLISION:
                # (NXS: 10)
                nxs = types.McnpReal.from_mcnp(j_line.popl())

            case Event.EventType.TERMINAL:
                # (NTER: 14)
                nter = Event.EventNter.from_mcnp(j_line.popl())

            case Event.EventType.FLAG:
                assert False

            case _:
                # (NXS: 10)
                nxs = types.McnpReal.from_mcnp(j_line.popl())

        # Processing Type Dependent Entries
        numbers = tuple([number.value for number in header.numbers[1:12]])

        match numbers:
            case (5, 3, 6, 3, 6, 3, 6, 3, 6, 3):
                # Type 1

                # Processing J5/J6 (MAT: 18)
                mat = types.McnpInteger.from_mcnp(j_line.popr())

                # Processing J4/J5 (NCL: 17)
                ncl = types.McnpInteger.from_mcnp(j_line.popr())

            case (6, 3, 7, 3, 7, 3, 7, 3, 7, 3):
                # Type 2

                # Processing J6/J7 (MAT: 18)
                mat = types.McnpInteger.from_mcnp(j_line.popr())

                # Processing J5/J6 (NCL: 17)
                ncl = types.McnpInteger.from_mcnp(j_line.popr())

                # Processing J4/J5 (IPT: 16)
                ipt = types.McnpInteger.from_mcnp(j_line.popr())

            case (6, 9, 7, 9, 7, 9, 7, 9, 7, 9):
                # Type 3

                # Processing J6/J7 (NCP: 19)
                ncp = types.McnpInteger.from_mcnp(j_line.popr())

                # Processing J5/J6 (MAT: 18)
                mat = types.McnpInteger.from_mcnp(j_line.popr())

                # Processing J4/J5 (NCL: 17)
                ncl = types.McnpInteger.from_mcnp(j_line.popr())

            case (7, 9, 8, 9, 8, 9, 8, 9, 8, 9):
                # Type 4

                # Processing J7/J8 (NCP: 19)
                ncp = types.McnpInteger.from_mcnp(j_line.popr())

                # Processing J6/J7 (MAT: 18)
                mat = types.McnpInteger.from_mcnp(j_line.popr())

                # Processing J5/J6 (NCL: 17)
                ncl = types.McnpInteger.from_mcnp(j_line.popr())

                # Processing J4/J5 (IPT: 16)
                ipt = types.McnpInteger.from_mcnp(j_line.popr())

        # Processing J4
        match event_type:
            case Event.EventType.SOURCE:
                pass

            case Event.EventType.SURFACE:
                # (Surface Angle: 13)
                surface_angle = types.McnpInteger.from_mcnp(j_line.popl())

            case Event.EventType.COLLISION:
                # (NTYN/MTP: 11)
                ntyn_mtp = types.McnpInteger.from_mcnp(j_line.popl())

            case Event.EventType.TERMINAL:
                # (Branch Number: 15)
                branch = types.McnpInteger.from_mcnp(j_line.popl())

            case Event.EventType.FLAG:
                assert False

            case _:
                # (NTYN/MTP: 11)
                ntyn_mtp = types.McnpInteger.from_mcnp(j_line.popl())

        # Processing P-Line
        p_line = _parser.Parser(
            lines[1].split(' '), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_EVENT)
        )

        # Processing P1 (xxx: 20)
        xxx = types.McnpReal.from_mcnp(p_line.popl())

        # Processing P2 (yyy: 21)
        yyy = types.McnpReal.from_mcnp(p_line.popl())

        # Processing P3 (zzz: 22)
        zzz = types.McnpReal.from_mcnp(p_line.popl())

        # Processing Type Dependent Entries
        if numbers in {
            (6, 9, 7, 9, 7, 9, 7, 9, 7, 9),
            (7, 9, 8, 9, 8, 9, 8, 9, 8, 9),
        }:
            # Processing P4 (uuu: 23)
            uuu = types.McnpReal.from_mcnp(p_line.popl())

            # Processing P5 (vvv: 24)
            vvv = types.McnpReal.from_mcnp(p_line.popl())

            # Processing P6 (www: 25)
            www = types.McnpReal.from_mcnp(p_line.popl())

            # Processing P7 (erg: 26)
            erg = types.McnpReal.from_mcnp(p_line.popl())

            # Processing P8 (wgt: 27)
            wgt = types.McnpReal.from_mcnp(p_line.popl())

            # Processing P9 (tme: 28)
            tme = types.McnpReal.from_mcnp(p_line.popl())

        return Event(
            next_type,
            event_type,
            node,
            nsr,
            nxs,
            ntyn_mtp,
            nsf,
            surface_angle,
            nter,
            branch,
            ipt,
            ncl,
            mat,
            ncp,
            xxx,
            yyy,
            zzz,
            uuu,
            vvv,
            www,
            erg,
            wgt,
            tme,
        )

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
