"""
``datum`` contains the class representing INP data cards.

``datum`` packages the ``Datum`` class, providing an object-oriented,
importable interface for INP datum cards.
"""


import re
from typing import Callable, Union, override
from enum import StrEnum

from .card import Card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Datum(Card):
    """
    ``Datum`` represents INP data cards.

    ``Datum`` implements INP data cards as a Python class. Its attributes store
    INP data card input parameters, and its methods provide entry points and
    endpoints for working with MCNP cells. It represents the INP data card
    syntax element, and it inherits from the ``Card`` super class.

    Attributes:
        mnemonic: Data card mnemonics.
        parameters: Data card parameters.
    """

    class DatumMnemonic(StrEnum):
        """
        ``DatumMnemonic`` represents INP data card mnemonics

        ``DatumMnemonic`` implements INP data card mnemonics as a Python inner
        class. It enumerates MCNP mnemonics and provides methods for casting
        strings to ``DatumMnemonic`` instances. It represents the INP data card
        mnemonics syntax element, so ``Datum`` depends on ``DatumMnemonic`` as
        an enum.
        """

        VOLUME = "vol"
        AREA = "area"
        TRANSFORMATION = "tr"
        TRANSFORMATION_ANGLE = "*tr"
        UNIVERSE = "u"
        LATTICE = "lat"
        FILL = "fill"
        FILL_ANGLE = "*fill"
        STOCHASTIC_GEOMETRY = "uran"
        DETERMINISTIC_MATERIALS = "dm"
        DETERMINISTIC_WEIGHT_WINDOW = "dawwg"
        EMBEDDED_GEOMETRY = "embed"
        EMBEDDED_CONTROL = "embee"
        EMBEDDED_ENERGY_BOUNDARIES = "embeb"
        EMBEDDED_ENERGY_MULTIPLIERS = "embem"
        EMBEDDED_TIME_BOUNDARIES = "embtb"
        EMBEDDED_TIME_MULTIPLIERS = "embtm"
        EMBEDDED_DOSE_BOUNDARIES = "embde"
        EMBEDDED_DOSE_MULTIPLIERS = "embdf"
        MATERIAL = "m"
        MATERIAL_NEUTRON_SCATTERING = "mt"
        MATERIAL_NUCLIDE_SUBSTITUTION = "mx"
        ON_THE_FLY_BROADENING = "otfdb"
        TOTAL_FISSION = "totnu"
        FISSION_TURNOFF = "nonu"
        ATOMIC_WEIGHT = "awtab"
        CROSS_SECTION_FILE = "xs"
        VOID = "void"
        MULTIGROUP_ADJOINT_TRANSPORT = "mgopt"
        DISCRETE_REACTION_CROSS_SECTION = "drxs"
        PROBLEM_TYPE = "mode"
        PARTICLE_PHYSICS_OPTIONS = "phys"
        ACTIVATION_CONTROL = "act"
        TIME_ENERGY_WEIGHT_CUTOFFS = "cut"
        CELL_ENERGY_CUTOFFS = "elpt"
        FREE_GAS_THERMAL_TEMPERATURE = "tmp"
        THERMAL_TIMES = "thtme"
        MODEL_PHYSICS_CONTROL = "mphys"
        LCA = "lca"
        LCB = "lcb"
        LCC = "lcc"
        LEA = "lea"
        LEB = "leb"
        MULTIPLICITY_CONSTANTS = "fmult"
        TRANSPORT_OPTIONS = "tropt"
        UNCOLLIDED_SECONDARIES = "unc"
        COSYP = "cosyp"
        COSY = "cosy"
        BFLD = "bfld"
        BFLCL = "bflcl"
        GRAVITATIONAL_FIELD = "field"
        GENERAL_SOURCE_DEFINITION = "sdef"
        SOURCE_INFORMATION = "si"
        SOURCE_PROBABILITY = "sp"
        SOURCE_BIAS = "sb"
        DEPENDENT_SOURCE_DISTRIBUTION = "ds"
        SOURCE_COMMENT = "sc"
        SURFACE_SOURCE_WRITE = "ssw"
        SURFACE_SOURCE_READ = "ssr"
        CRITICALITY_SOURCE = "kcode"
        CRITICALITY_SOURCE_POINTS = "ksrc"
        CRITICALITY_CALCULIATION_OPTIONS = "kopts"
        ENTROPY_SOURCE_DISTRIBUTION = "hsrc"
        DEPLETION_BURNUP = "burn"
        SOURCE = "source"
        SRCDX = "srdx"
        STANDARD_TALLIES = "f"
        STANDARD_TALLIES_ANGLE = "*f"
        FIP = "fip"
        FIR = "fir"
        FIC = "fic"
        TALLY_COMMENT = "fc"
        TALLY_ENERGY = "e"
        TALLY_TIME = "t"
        TALLY_COSINE = "c"
        TALLY_COSINE_ANGLE = "*c"
        PRINT_HIERARCHY = "fq"
        TALLY_MULTIPLIER = "em"
        DOSE_ENERGY = "de"
        DOSE_FUNCTION = "df"
        ENERGY_MULTIPLIER = "em"
        TIME_MULTIPLIER = "tm"
        COSINE_MULTIPLIER = "cm"
        CELL_FLAGGING = "cf"
        SURFACE_FLAGGING = "sf"
        TALLY_SEGMENT = "fs"
        SEGMENT_DIVISOR = "sd"
        SPECIAL_TALLY = "fu"
        TALLYX_SUBROUTINE = "tallyx"
        SPECIAL_TREATMENTS_TALLIES = "ft"
        TALLY_FLUCTUATION = "tf"
        DIRECT_ONLY_CONTRIBUTIONS = "notrn"
        TALLY_PERTUBATION = "pert"
        REACTIVITY_PERTUBATIONS = "kpert"
        SENSITIVITY_COEFFICENTS = "ksen"
        SUPERIMPOSED_MESH_TALLY_A = "tmesh"
        SUPERIMPOSED_MESH_TALLY_B = "fmesh"
        LATTICE_SPEED_TALLY_ENHANCEMENT = "spdtl"
        IMPORTANCE = "imp"
        VARIANCE_REDUCATION_CONTROL = "var"
        WEIGHT_WINDOW_ENERGIES = "wwe"
        WEIGHT_WINDOW_TIMES = "wwt"
        WEIGHT_WINDOW_BOUNDS = "wwn"
        WEIGHT_WINDOW_PARAMETER = "wwp"
        WEIGHT_WINDOW_GENERATION = "wwg"
        WEIGHT_WINDOW_GENERATION_ENERGIES = "wwge"
        WEIGHT_WINDOW_GENERATION_TIMES = "wwgt"
        SUPERIMPOSED_IMPORTANCE_MESH = "mesh"
        ENERGY_SPLITTING = "esplt"
        TIME_SPLITTING = "tsplt"
        EXPONENTIAL_TRANSFORM = "ext"
        VECTOR_INPUT = "vect"
        FORCED_COLLISION = "fcl"
        DXTRAN_SPHERE = "dxt"
        DETECTOR_DIAGNOSTICS = "dd"
        DETECTOR_CONTRIBUTION = "pd"
        DXTRAN_CONTRIBUTION = "dxc"
        BREMSSTRAHLUNG_BIASING = "bbrem"
        PHOTON_PRODUDCTION_BIASING = "pikmt"
        SECONDARY_PARTICLE_BIASING = "spabi"
        PHOTON_WEIGHT = "pwt"
        HISTORY_CUTOFF = "nps"
        COMPUTER_TIME_CUTOFF = "ctme"
        PERCISION_CUTOFF = "stop"
        OUPUT_PRINT_TABLES = "print"
        NEGATE_PRINTING_TALLIES = "talnp"
        PRINT_DUMP_CYCLES = "prdmp"
        PARTICLE_TRACK_OUTPUT = "ptrac"
        PLOT_TALLIES_WHITE_RUNNING = "mplot"
        CREATE_LAHET = "histp"
        RANDOM = "rand"
        DEBUG_INFORMATION = "dbcn"
        LOST_PARTICLE_CONTROL = "lost"
        INTEGER_ARRAY = "idum"
        FLOATINGPOINT_ARRAY = "rdum"
        ZA = "za"
        ZB = "zb"
        ZC = "zc"
        ZD = "zd"
        FILE = "files"

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``DatumMnemonic`` objects from INP.

            ``from_mcnp`` constructs instances of ``DatumMnemonic`` from INP
            source strings, so it operates as a class constructor method
            and INP parser helper function.

            Parameters:
                source: INP for data card mnemonic.

            Returns:
                ``DatumMnemonic`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MNEMONIC.
            """

            source = _parser.Preprocessor.process_inp(source)

            # Processing Keyword
            if source not in [enum.value for enum in Datum.DatumMnemonic]:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC)

            return Datum.DatumMnemonic(source)

    def __init__(
        self, mnemonic: DatumMnemonic, parameters: tuple[any], suffix: int = None, designator: types.Designator = None
    ):
        """
        ``__init__`` initializes ``Datum``.

        Parameters:
            number: Data card mnemonic.

        Raises:
            MCNPSemanticError: INVALID_DATUM_MNEMONIC.
        """

        super().__init__(mnemonic + str(suffix) if suffix is not None else mnemonic)

        if mnemonic is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC)

        match mnemonic:
            case Datum.DatumMnemonic.VOLUME:
                obj = Volume(*parameters)
            case Datum.DatumMnemonic.AREA:
                obj = Area(*parameters)
            case Datum.DatumMnemonic.TRANSFORMATION:
                obj = Transformation(*parameters, suffix, is_angle=False)
            case Datum.DatumMnemonic.TRANSFORMATION_ANGLE:
                obj = Transformation(*parameters, suffix, is_angle=True)
            case Datum.DatumMnemonic.UNIVERSE:
                obj = Universe(*parameters)
            case Datum.DatumMnemonic.LATTICE:
                obj = Lattice(*parameters)
            case Datum.DatumMnemonic.FILL:
                obj = Fill(*parameters, is_angle=False)
            case Datum.DatumMnemonic.FILL_ANGLE:
                obj = Fill(*parameters, is_angle=True)
            case Datum.DatumMnemonic.STOCHASTIC_GEOMETRY:
                obj = StochasticGeometry(*parameters)
            case Datum.DatumMnemonic.DETERMINISTIC_MATERIALS:
                obj = DeterministicMaterials(*parameters, suffix)
            case Datum.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW:
                obj = DeterministicWeightWindow(*parameters)
            case Datum.DatumMnemonic.EMBEDDED_GEOMETRY:
                obj = EmbeddedGeometry(*parameters, suffix)
            case Datum.DatumMnemonic.EMBEDDED_CONTROL:
                obj = EmbeddedControl(*parameters, suffix, designator)
            case Datum.DatumMnemonic.EMBEDDED_ENERGY_BOUNDARIES:
                obj = EmbeddedEnergyBoundaries(*parameters, suffix)
            case Datum.DatumMnemonic.EMBEDDED_ENERGY_MULTIPLIERS:
                obj = EmbeddedEnergyMultipliers(*parameters, suffix)
            case Datum.DatumMnemonic.EMBEDDED_TIME_BOUNDARIES:
                obj = EmbeddedTimeBoundaries(*parameters, suffix)
            case Datum.DatumMnemonic.EMBEDDED_TIME_MULTIPLIERS:
                obj = EmbeddedTimeMultipliers(*parameters, suffix)
            case Datum.DatumMnemonic.EMBEDDED_DOSE_BOUNDARIES:
                obj = EmbeddedDoseBoundaries(*parameters, suffix)
            case Datum.DatumMnemonic.EMBEDDED_DOSE_MULTIPLIERS:
                obj = EmbeddedDoseMultipliers(*parameters, suffix)
            case Datum.DatumMnemonic.MATERIAL:
                obj = Material(*parameters)
            case Datum.DatumMnemonic.MATERIAL_NEUTRON_SCATTERING:
                obj = MaterialNeutronScattering(*parameters)
            case Datum.DatumMnemonic.MATERIAL_NUCLIDE_SUBSTITUTION:
                obj = MaterialNuclideSubstitution(*parametres)
            case Datum.DatumMnemonic.ON_THE_FLY_BROADENING:
                obj = OnTheFlyBroadening(*parameters)
            case Datum.DatumMnemonic.TOTAL_FISSION:
                obj = TotalFission(*parameters)
            case Datum.DatumMnemonic.FISSION_TURNOFF:
                obj = FissionTurnOff(*parameters)
            case Datum.DatumMnemonic.ATOMIC_WEIGHT:
                obj = AtomicWeight(*parameters)
            case Datum.DatumMnemonic.CROSS_SECTION_FILE:
                obj = CrossSectionFile(*parameters)
            case Datum.DatumMnemonic.VOID:
                obj = Void(*parameters)
            case Datum.DatumMnemonic.MULTIGROUP_ADJOINT_TRANSPORT:
                obj = MultigroupAdjointTransport(*parameters)
            case Datum.DatumMnemonic.DISCRETE_REACTION_CROSS_SECTION:
                obj = DiscreteReactionCrossSection(*parameters)
            case Datum.DatumMnemonic.PROBLEM_TYPE:
                obj = ProblemType(*parameters)
            case Datum.DatumMnemonic.PARTICLE_PHYSICS_OPTIONS:
                obj = ParticlePhysicsOptions(*parameters)
            case Datum.DatumMnemonic.ACTIVATION_CONTROL:
                obj = ActivationControl(*parameters)
            case Datum.DatumMnemonic.TIME_ENERGY_WEIGHT_CUTOFFS:
                obj = TimeEnergyWeightCutoffs(*parameters)
            case Datum.DatumMnemonic.CELL_ENERGY_CUTOFF:
                obj = CellEnergyCutoff(*parameters)
            case Datum.DatumMnemonic.FREE_GAS_THERMAL_TEMPERATURE:
                obj = FreeGasThermalTemperature(*parameters)
            case Datum.DatumMnemonic.THERMAL_TIMES:
                obj = ThermalTimes(*parameters)
            case Datum.DatumMnemonic.MODEL_PHYSICS_CONTROL:
                obj = ModelPhysicsControl(*parameters)
            case Datum.DatumMnemonic.LCA:
                obj = Lca(*parameters)
            case Datum.DatumMnemonic.LCB:
                obj = Lcb(*parameters)
            case Datum.DatumMnemonic.LCC:
                obj = Lcc(*parameters)
            case Datum.DatumMnemonic.LEA:
                obj = Lea(*parameters)
            case _:
                obj = _Placeholder(mnemonic, parameters)

        self.__dict__ = obj.__dict__
        self.__class__ = obj.__class__

    @staticmethod
    def from_mcnp(source: str, line: int = None):
        """
        ``from_mcnp`` generates ``Datum`` objects from INP.

        ``from_mcnp`` constructs instances of ``Datum`` from INP source
        strings, so it operates as a class constructor method and INP parser
        helper function.

        Parameters:
            source: INP for datum.
            line: Line number.

        Returns:
            ``Datum`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_DATUM, TOOLONG_DATUM.
        """

        source = _parser.Preprocessor.process_inp(source, hasComments=False)
        tokens = _parser.Parser(re.split(r" |:|=", source), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM))

        # Processing Mnemonic
        mnemonic = re.search(r"^[a-zA-z*]+", tokens.peekl())
        mnemonic = mnemonic.group() if mnemonic else ""
        mnemonic = Datum.DatumMnemonic.from_mcnp(mnemonic)

        # Processing Suffix & Parameters
        suffix = None
        designator = None
        match mnemonic:
            case Datum.DatumMnemonic.VOLUME:
                tokens.popl()
                has_no = True if tokens.peekl() == "no" else False
                volumes = tuple(types.cast_fortran_real(tokens.popl()) for _ in range(0, len(tokens)))

                datum = Volume(volumes, has_no=has_no)

            case Datum.DatumMnemonic.AREA:
                tokens.popl()
                areas = tuple(types.cast_fortran_real(tokens.popl()) for _ in range(0, len(tokens)))

                datum = Area(areas)

            case Datum.DatumMnemonic.TRANSFORMATION:
                suffix = types.cast_fortran_integer(tokens.popl()[2:])
                entries = tuple(types.cast_fortran_real(tokens.popl()) for _ in range(0, len(tokens)))
                displacement = tuple(entries[:3])
                rotation = (tuple(entries[3:6]), tuple(entries[6:9]), tuple(entries[9:12]))
                system = int(entires[12])

                datum = Transformation(displacement, rotation, system)

            case Datum.DatumMnemonic.UNIVERSE:
                tokens.popl()
                unvierses = tuple(types.cast_fortran_integer(tokens.popl()) for _ in range(0, len(tokens)))

                datum = Universe(universes)

            case Datum.DatumMnemonic.LATTICE:
                tokens.popl()
                lattices = tuple(types.cast_fortran_integer(tokens.popl()) for _ in range(0, len(tokens)))

                datum = Lattice(lattices)

            case Datum.DatumMnemonic.FILL:
                tokens.popl()
                fills = tuple(types.cast_fortran_real(tokens.popl()) for _ in range(0, len(tokens)))

                datum = Fill(fills)

            case Datum.DatumMnemonic.STOCHASTIC_GEOMETRY:
                tokens.popl()
                transformations = tuple(
                    StochasticGeometry.StochasticGeometryValue(
                        types.fortran_integer(tokens.popl()),
                        typesf(tokens.popl()),
                        typesf(tokens.popl()),
                        typesf(tokens.popl()),
                    )
                    for _ in range(0, len(tokens), 4)
                )

                datum = StochasticGeometry(transformations)

            case Datum.DatumMnemonic.DETERMINISTIC_MATERIALS:
                suffix = types.cast_fortran_integer(tokens.popl()[2:])
                zaids = tuple(types.Zaid.cast_mcnp_zaid(tokens.popl()) for _ in range(0, len(tokens)))

                datum = DeterministicMaterials(zaids)

            case Datum.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW:
                tokens.popl()
                pairs = tuple(
                    DeterministicWeightWindow.DeterministicWeightWindowOption.from_mcnp(tokens.popl())
                    for _ in range(0, len(tokens))
                )

                datum = DeterministicWeightWindow(pairs)

            case Datum.DatumMnemonic.EMBEDDED_GEOMETRY:
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                pairs = tuple()
                while tokens:
                    keyword = tokens.popl()
                    values = tuple()
                    while tokens:
                        try:
                            EmbeddedGeometry.EmbeddedGeometryOption.from_mcnp(tokens.peekl())
                            break
                        except:
                            values.append(tokens.popl())
                            pass
                    pairs.append(EmbeddedGeometry.EmbeddedGeometryOption.from_mcnp(f"{keyword}={" ".join(values)}"))

                datum = EmbeddedGeometry(pairs, suffix)

            case Datum.DatumMnemonic.EMBEDDED_CONTROL:
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                designator = types.Designator.cast_mcnp_designator(tokens.popl())
                pairs = tuple()
                while tokens:
                    keyword = tokens.popl()
                    values = tuple()
                    while tokens:
                        try:
                            EmbeddedControl.EmbeddedControlOption.from_mcnp(tokens.peekl())
                            break
                        except:
                            values.append(tokens.popl())
                            pass
                    pairs.append(EmbeddedControl.EmbeddedControlOption.from_mcnp(f"{keyword}={" ".join(values)}"))

                datum = EmbeddedControl(pairs, suffix, designator)

            case Datum.DatumMnemonic.EMBEDDED_ENERGY_BOUNDARIES:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                energies = tuple(types.cast_fortran_reals(tokens.popl()) for _ in range(0, len(tokens)))

                datum = EmbeddedEnergyBoundaries(energies, suffix)

            case Datum.DatumMnemonic.EMBEDDED_ENERGY_MULTIPLIERS:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                multipliers = tuple([types.cast_fortran_reals(tokens.popl()) for _ in range(0, len(tokens))])

                datum = EmbeddedEnergyMultipliers(multipliers, suffix)

            case Datum.DatumMnemonic.EMBEDDED_TIME_BOUNDARIES:
                if len(tokens) < 1:
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                times = tuple(types.cast_fortran_reals(tokens.popl()) for _ in range(0, len(tokens)))

                datum = EmbeddedTimeBoundaries(times, suffix)

            case Datum.DatumMnemonic.EMBEDDED_TIME_MULTIPLIERS:
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                multipliers = tuple([types.cast_fortran_reals(tokens.popl()) for _ in range(0, len(tokens))])

                datum = EmbeddedTimeMultipliers(multipliers, suffix)

            case Datum.DatumMnemonic.EMBEDDED_DOSE_BOUNDARIES:
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                doses = tuple(types.cast_fortran_reals(tokens.popl()) for _ in range(0, len(tokens)))

                datum = EmbeddedDoseBoundaries(doses, suffix)

            case Datum.DatumMnemonic.EMBEDDED_DOSE_MULTIPLIERS:
                suffix = types.cast_fortran_integer(tokens.popl()[5:])
                multipliers = tuple([types.cast_fortran_reals(tokens.popl()) for _ in range(0, len(tokens))])

                datum = EmbeddedDoseMultipliers(multipliers, suffix)

            case Datum.DatumMnemonic.MATERIAL:
                suffix = types.cast_fortran_integer(tokens.popl()[1:])

                substances = []
                while tokens:
                    try:
                        Material.MaterialOption.MaterialKeyword.from_mcnp(tokens.peekl())
                        break
                    except:
                        substances.append(
                            Material.MaterialValue(
                                types.Zaid.cast_mcnp_zaid(tokens.popl()), types.cast_fortran_real(tokens.popl())
                            )
                        )
                        pass

                options = []
                while tokens:
                    keyword = tokens.popl()
                    values = []
                    while tokens:
                        try:
                            Material.MaterialOption.MaterialKeyword.from_mcnp(tokens.peekl())
                            break
                        except:
                            values.append(tokens.popl())
                            pass
                    options.append(Material.MaterialOption.from_mcnp(f"{keyword}={" ".join(values)}"))

                datum = Material(substances, options, suffix)

            case Datum.DatumMnemonic.MATERIAL_NEUTRON_SCATTERING:
                suffix = types.cast_fortran_integer(tokens.popl()[2:])
                identifiers = tuple(tokens.popl() for _ in range(0, len(tokens)))

                datum = MaterialNeutronScattering(identifiers, suffix)

            case Datum.DatumMnemonic.MATERIAL_NUCLIDE_SUBSTITUTION:
                suffix = types.cast_fortran_integer(tokens.popl()[2:])
                designator = types.Designator.cast_mcnp_designator(tokens.popl())
                zaids = tuple(types.Zaid.cast_mcnp_zaid(tokens.popl()) for _ in range(0, len(tokens)))

                datum = MaterialNuclideSubstitution(zaids, suffix, designator)

            case Datum.DatumMnemonic.ON_THE_FLY_BROADENING:
                tokens.popl()
                zaids = tuple(types.Zaid.cast_mcnp_zaid(tokens.popl()) for _ in range(0, len(tokens)))

                datum = OnTheFlyBroadening(zaids)

            case Datum.DatumMnemonic.TOTAL_FISSION:
                tokens.popl()

                if tokens:
                    if tokens.popl() != "no":
                        raise errors.MCNPSyntaxError(errors.MCNPSytnaxCodes.KEYWORD_DATUM_TOTNU_NO)

                    datum = TotalFission(True)
                else:
                    datum = TotalFission(False)

            case Datum.DatumMnemonic.FISSION_TURNOFF:
                tokens.popl()
                states = tuple(types.cast_fortran_integer(tokens.popl()) for _ in range(0, len(tokens)))

                datum = FissionTurnoff(states)

            case Datum.DatumMnemonic.ATOMIC_WEIGHT:
                tokens.popl()
                weight_ratios = tuple(AtomicWeight.AtomicWeightValue.from_mcnp(f"{tokens.popl()} {tokens.popl()}"))

                datum = AtomicWeight(weight_ratios)

            case Datum.DatumMnemonic.CROSS_SECTION_FILE:
                suffix = types.cast_fortran_integer(tokens.popl()[2:])
                weight_ratios = tuple(CrossSectionFile.CrossSectionFileValue.from_mcnp(f"{tokens.popl()} {tokens.popl()}"))

                datum = CrossSectionFile(weight_ratios, suffix)

            case Datum.DatumMnemonic.VOID:
                tokens.popl()
                numbers = tuple(types.cast_fortran_integer(tokens.popl()) for _ in range(0, len(tokens)))

                datum = Void(numbers)

            case Datum.DatumMnemonic.MULTIGROUP_ADJOINT_TRANSPORT:
                tokens.popl()
                mcal = tokens.popl()
                igm = types.cast_fortran_integer(tokens.popl())
                iplt = types.cast_fortran_integer(tokens.popl())
                isb = types.cast_fortran_integer(tokens.popl())
                icw = types.cast_fortran_integer(tokens.popl())
                fnw = types.cast_fortran_integer(tokens.popl())
                rim = types.cast_fortran_integer(tokens.popl())

                datum = MultigroupAdjointTransport(mcal, igm, iplt, isb, icw, fnw, rim)

            case Datum.DatumMnemonic.DISCRETE_REACTION_CROSS_SECTION:
                tokens.popl()
                zaids = tuple(types.Zaid.cast_mcnp_zaid(tokens.popl()) for _ in range(0, len(tokens)))

                datum = DiscreteReactionCrossSection(zaids)

            case Datum.DatumMnemonic.PROBLEM_TYPE:
                tokens.popl()
                particles = tuple(types.Designator.cast_mcnp_designator(tokens.popl()) for _ in range(0, len(tokens)))

                datum = ProblemType(particles)

            case Datum.DatumMnemonic.PARTICLE_PHYSICS_OPTIONS:
                tokens.popl()
                designator = types.Designator.cast_mcnp_designator(tokens.popl())

                match designator:
                    case types.Designator.NEUTRON:
                        emax = types.cast_fortran_real(tokens.popl())
                        emcnf = types.cast_fortran_real(tokens.popl())
                        iunr = types.cast_fortran_integer(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        colif = types.cast_fortran_real(tokens.popl())
                        cutn = types.cast_fortran_real(tokens.popl())
                        ngam = types.cast_fortran_integer(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        i_int_model = types.cast_fortran_integer(tokens.popl())
                        i_els_model = types.cast_fortran_integer(tokens.popl())

                        parameters = (emax, emcnf, iunr, colif, cutn, ngam, i_int_model, i_els_model)

                    case types.Designator.PHOTON:
                        emcpf = types.cast_fortran_real(tokens.popl())
                        ides = types.cast_fortran_integer(tokens.popl())
                        nocoh = types.cast_fortran_integer(tokens.popl())
                        ispn = types.cast_fortran_integer(tokens.popl())
                        nodop = types.cast_fortran_integer(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        fism = types.cast_fortran_integer(tokens.popl())

                        parameters = (emcpf, ides, nocoh, ispn, nodop, fism)

                    case types.Designator.ELECTRON:
                        emax = types.cast_fortran_real(tokens.popl())
                        ides = types.cast_fortran_integer(tokens.popl())
                        ibad = types.cast_fortran_integer(tokens.popl())
                        istrg = types.cast_fortran_integer(tokens.popl())
                        bnum = types.cast_fortran_real(tokens.popl())
                        xnum = types.cast_fortran_real(tokens.popl())
                        rnok = types.cast_fortran_real(tokens.popl())
                        enum = types.cast_fortran_real(tokens.popl())
                        numb = types.cast_fortran_real(tokens.popl())
                        i_mcs_model = types.cast_fortran_integer(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        efac = types.cast_fortran_real(tokens.popl())
                        electron_method_boundary = types.cast_fortran_real(tokens.popl())
                        ckvnum = types.cast_fortran_real(tokens.popl())

                        parameters = (
                            emax,
                            ides,
                            ibad,
                            istrg,
                            bnum,
                            xnum,
                            rnok,
                            enum,
                            numb,
                            i_mcs_model,
                            efac,
                            electron_method_boundary,
                            ckvnum,
                        )

                    case types.Designator.PROTON:
                        emax = types.cast_fortran_real(tokens.popl())
                        ean = types.cast_fortran_real(tokens.popl())
                        tabl = types.cast_fortran_real(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        istrg = types.cast_fortran_integer(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        recl = types.cast_fortran_real(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        i_mcs_model = types.cast_fortran_integer(tokens.popl())
                        i_int_model = types.cast_fortran_integer(tokens.popl())
                        i_els_model = types.cast_fortran_integer(tokens.popl())
                        efac = types.cast_fortran_real(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        ckvnum = types.cast_fortran_real(tokens.popl())
                        drp = types.cast_fortran_real(tokens.popl())

                        parameters = (emax, ean, tabl, istrg, recl, i_mcs_model, i_int_model, i_els_model, efac, ckvnum, drp)

                    case _:
                        emax = types.cast_fortran_real(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        istrg = types.cast_fortran_integer(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        xmunum = types.cast_fortran_integer(tokens.popl())
                        xmugam = types.cast_fortran_real(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        i_mcs_model = types.cast_fortran_integer(tokens.popl())
                        i_int_model = types.cast_fortran_integer(tokens.popl())
                        i_els_model = types.cast_fortran_integer(tokens.popl())
                        efac = types.cast_fortran_real(tokens.popl())
                        if tokens.popl() != "j":
                            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                        ckvnum = types.cast_fortran_real(tokens.popl())
                        drp = types.cast_fortran_real(tokens.popl())

                        parameters = (emax, istrg, xmunum, xmugam, i_mcs_model, i_int_model, i_els_model, efac, ckvnum, drp)

                datum = ParticlePhysicsOptions(designator, parameters)

            case Datum.DatumMnemonic.ACTIVATION_CONTROL:
                tokens.popl()
                pairs = tuple()
                while tokens:
                    keyword = tokens.popl()
                    values = tuple()
                    while tokens:
                        try:
                            ActivationControl.ActivationControlOption.from_mcnp(tokens.peekl())
                            break
                        except:
                            values.append(tokens.popl())
                            pass
                    pairs.append(ActivationControl.ActivationControlOption.from_mcnp(f"{keyword}={" ".join(values)}"))

                datum = ActivationControl(pairs)

            case Datum.DatumMnemonic.TIME_ENERGY_WEIGHT_CUTOFFS:
                tokens.popl()
                designator = types.Designator.cast_mcnp_designator(tokens.popl())

                t = types.cast_fortran_real(tokens.popl())
                e = types.cast_fortran_real(tokens.popl())
                weight1 = types.cast_fortran_real(tokens.popl())
                weight2 = types.cast_fortran_real(tokens.popl())
                source = types.cast_fortran_real(tokens.popl())

                datum = TimeEnergyWeightCutoffs(t, e, weight1, weight2, source)

            case Datum.DatumMnemonic.CELL_ENERGY_CUTOFFS:
                tokens.popl()
                designator = types.Designator.cast_mcnp_designator(tokens.popl())
                cutoffs = types.cast_fortran_real(tokens.popl())

                datum = CellEnergyCutoffs(designator, cutoffs)

            case Datum.DatumMnemonic.FREE_GAS_THERMAL_TEMPERATURE:
                suffix = types.cast_fortran_integer(tokens.popl()[3:])
                temperatures = tuple(types.cast_fortran_real(tokens.popl()) for _ in range(0, len(tokens)))

                datum = FreeGasThermalTemperature(suffix, temperatures)

            case Datum.DatumMnemonic.THERMAL_TIMES:
                tokens.popl()
                times = tuple(types.cast_fortran_integer(tokens.popl()) for _ in range(0, len(tokens)))

                datum = ThermalTimes(times)

            case Datum.DatumMnemonic.MODEL_PHYSICS_CONTROL:
                tokens.popl()

                if tokens:
                    ModelPhysicsControl(tokens.popl())
                else:
                    datum = ModelPhysicsControl("no")

            case Datum.DatumMnemonic.LCA:
                tokens.popl()
                ielas = types.cast_fortran_integer(tokens.popl())
                ipreq = types.cast_fortran_integer(tokens.popl())
                iexisa = types.cast_fortran_integer(tokens.popl())
                ichoic = tokens.popl()
                jcoul = types.cast_fortran_integer(tokens.popl())
                nexite = types.cast_fortran_integer(tokens.popl())
                npidk = types.cast_fortran_integer(tokens.popl())
                noact = types.cast_fortran_integer(tokens.popl())
                icem = types.cast_fortran_integer(tokens.popl())
                ilaq = types.cast_fortran_integer(tokens.popl())
                nevtype = types.cast_fortran_real(tokens.popl())

                datum = Lca(ielas, ipreq, iexisa, ichoic, jcoul, nexite, npidk, noact, icem, ilaq, nevtype)

            case Datum.DatumMnemonic.LCB:
                tokens.popl()
                lebn1 = types.cast_fortran_real(tokens.popl())
                flebn2 = types.cast_fortran_real(tokens.popl())
                flebn3 = types.cast_fortran_real(tokens.popl())
                flebn4 = types.cast_fortran_real(tokens.popl())
                flebn5 = types.cast_fortran_real(tokens.popl())
                flebn6 = types.cast_fortran_real(tokens.popl())
                ctofe = types.cast_fortran_real(tokens.popl())
                flim0 = types.cast_fortran_real(tokens.popl())

                datum = Lcb(lebn1, flebn2, flebn3, flebn4, flebn5, flebn6, ctofe, flim0)

            case Datum.DatumMnemonic.LCC:
                tokens.popl()
                atincl = types.cast_fortran_real(tokens.popl())
                v0incl = types.cast_fortran_real(tokens.popl())
                xfoisaincl = types.cast_fortran_real(tokens.popl())
                npaulincl = types.cast_fortran_real(tokens.popl())
                nosurfincl = types.cast_fortran_real(tokens.popl())
                if tokens.popl() != "j":
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                if tokens.popl() != "j":
                    raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                ecutincl = types.cast_fortran_real(tokens.popl())
                ebankincl = types.cast_fortran_real(tokens.popl())
                ebankabla = types.cast_fortran_real(tokens.popl())

                datum = Lcc(atincl, v0incl, xfoisaincl, npaulincl, nosurfincl, ecutincl, ebankincl, ebankabla)

            case Datum.DatumMnemonic.LEA:
                tokens.popl()
                ipht = types.cast_fortran_integer(tokens.popl())
                icc = types.cast_fortran_integer(tokens.popl())
                nobalc = types.cast_fortran_integer(tokens.popl())
                nobale = types.cast_fortran_integer(tokens.popl())
                ifbrk = types.cast_fortran_integer(tokens.popl())
                ilvden = types.cast_fortran_integer(tokens.popl())
                ievap = types.cast_fortran_integer(tokens.popl())
                nofis = types.cast_fortran_integer(tokens.popl())

                datum = Lea(ipht, icc, nobalc, nobale, ifbrk, ilvden, ievap, nofis)

            case _:
                datum = _Placeholder(tokens.popl(), [tokens.popl() for _ in range(0, len(tokens))])

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM)

        return datum

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Datum`` objects.

        ``to_mcnp`` creates INP source string from ``Datum``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``Datum`` object.
        """

        suffix_str = f"{self.suffix}" if hasattr(self, "suffix") else ""
        designator_str = f":{self.designator}" if hasattr(self, "designator") else ""

        parameters_str = ""
        for parameter in self.parameters:
            if isinstance(parameter, tuple):
                parameters_str += f" {' '.join([str(entry) for entry in parameter])}"
            elif not hasattr(parameter, "to_mcnp"):
                parameters_str += f" {str(parameter)}"
            else:
                parameters_str += f" {parameter.to_mcnp()}"

        return f"{self.mnemonic}{suffix_str}{designator_str}{parameters_str}"

    def to_arguments(self) -> list:
        """
        ``to_arguments`` makes dictionaries from ``Datum`` objects.

        ``to_arguments`` creates Python dictionaries from ``Datum`` objects, so
        it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual. Although defined on the superclass, it returns key-value pairs
        suffixes and designators as required.

        Returns:
            Dictionary for ``Datum`` object.
        """

        return {
            "mnemonic": self.mnemonic,
            "m": self.suffix if hasattr(self, "suffix") else None,
            "n": self.designator if hasattr(self, "designator") else None,
            "parameters": tuple(
                [parameter.to_mcnp() if hasattr(parameter, "to_mcnp") else parameter for parameter in self.parameters]
            ),
        }


class Volume(Datum):
    """
    ``Volume`` represents INP volume data cards.

    ``Volume`` inherits attributes from ``Datum``. It represents the INP volume
    data card syntax element.

    Attributes:
        has_no: No volume calculation option.
        volumes: Tuple of cell volumes.
    """

    def __init__(self, volumes: tuple[float], has_no: bool = False):
        """
        ``__init__`` initializes ``Volume``.

        Parameters:
            has_no: No volume calculation option.
            volumes: Tuple of cell volumes.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for entry in volumes:
            if entry is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if has_no is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"vol"
        self.mnemonic = Datum.DatumMnemonic.VOLUME
        self.parameters = (has_no, volumes)

        self.has_no = has_no
        self.volumes = volumes

    @override
    def to_mcnp(self) -> str:
        if self.has_no:
            return f"vol no {" ".join(str(volume) for volume in self.volumes)}"
        else:
            return f"vol {" ".join(str(volume) for volume in self.volumes)}"


class Area(Datum):
    """
    ``Area`` represents INP area data cards.

    ``Area`` inherits attributes from ``Datum``. It represents the INP area
    data card syntax element.

    Attributes:
        areas: Tuple of cell areas.
    """

    def __init__(self, areas: tuple[float]):
        """
        ``__init__`` initializes ``Area``.

        Parameters:
            areas: Tuple of cell areas.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in areas:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"area"
        self.mnemonic: final[DatumMnemonic] = Datum.DatumMnemonic.AREA
        self.parameters: final[[tuple[float]]] = areas

        self.areas: final[tuple[float]] = areas


class Transformation(Datum):
    """
    ``Transformation`` represents INP transformion data cards.

    ``Transformation`` inherits attributes from ``Datum``. It represents the INP
    transformion data card syntax element.

    Attributes:
        displacement: Transformation displacement vector.
        rotation: Transformation rotation matrix.
        system: Transformation coordinate system setting.
        suffix: Data card suffix.
    """

    def __init__(self, displacement: tuple[float], rotation: tuple[float], system: int, suffix: int, is_angle: bool):
        """
        ``__init__`` initializes ``Transformation``.

        Parameters:
            displacement: Transformation displacement vector.
            rotation: Transformation rotation matrix.
            system: Transformation coordinate system setting.
            suffix: Data card suffix.
            is_angle: Angle units modifier.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSematnicCodes.INVALID_DATUM_SUFFIX)

        for entry in displacement:
            if entry is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for row in rotation:
            for entry in row:
                if entry is None:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if system is None or system not in {-1, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"tr{suffix}"
        self.mnemonic = Datum.DatumMnemonic.TRANSFORMATION
        self.parameters = tuple(displacement, rotation, system)
        self.suffix = suffix

        self.displacement = displacement
        self.rotation = rotation
        self.system = system
        self.is_angle = is_anlge


class Universe(Datum):
    """
    ``Universe`` represents INP universe data cards.

    ``Universe`` inherits attributes from ``Datum``. It represents the INP
    universe data card syntax element.

    Attributes:
        universes: Tuple of cell universe numbers.
    """

    def __init__(self, universes: tuple[int]):
        """
        ``__init__`` initializes ``Universe``.

        Parameters:
            universes: Tuple of cell universe numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in unvierses:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"u"
        self.mnemonic = Datum.DatumMnemonic.UNIVERSE
        self.universes = unvierses

        self.parameters = unvierses


class Lattice(Datum):
    """
    ``Lattice`` represents INP lattice data cards.

    ``Lattice`` inherits attributes from ``Datum``. It represents the INP
    lattice data card syntax element.

    Attributes:
        lattices: Tuple of cell lattice numbers.
    """

    def __init__(self, lattices: tuple[int]):
        """
        ``__init__`` initializes ``Lattice``.

        Parameters:
            lattices: Tuple of cell lattice numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in lattices:
            if parameter is None or parameter not in {1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"lat"
        self.mnemonic = Datum.DatumMnemonic.LATTICE
        self.lattices = lattices

        self.parameters = lattices


class Fill(Datum):
    """
    ``Fill`` represents INP fill data cards.

    ``Fill`` inherits attributes from ``Datum``. It represents the INP
    universe data card syntax element.

    Attributes:
        fills: Tuple of universe numbers.
        is_angle: Angle unit setting.
    """

    def __init__(self, fills: tuple[int], is_angle: bool = False):
        """
        ``__init__`` initializes ``Fill``.

        Parameters:
            fills: Tuple of universe numbers.
            is_angle: Angle unit setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in fills:
            if parameter is None or not (parameter >= 0 and parameter <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"fill"
        self.mnemonic = Datum.DatumMnemonic.FILL
        self.parameters = fills

        self.fills = fills
        self.is_angle = is_angle


class StochasticGeometry(Datum):
    """
    ``StochasticGeometry`` represents INP stochastic geometry data cards.

    ``StochasticGeometry`` inherits attributes from ``Datum``. It represents
    the INP universe data card syntax element.

    Attributes:
        transformations: Tuple of stochastric geometry transformations.
    """

    class StochasticGeometryValue:
        """
        ``StochasticGeometryValue`` represents INP stochastic geometry data
        card entries.

        ``StochasticGeometryValue`` implements INP stochastic geometry
        specifications as a Python inner class. Its attributes store different
        stochastic geometry entries, and its methods provide entry points
        and endpoints for working with stochastic geometry entries.
        ``StochasticGeometry`` depends on ``StochasticGeometryValue`` as a data
        type.

        Attributes:
            number: Stochastic geometry universe number.
            maximum_x: Stochastic geometry maximum translation in x direction.
            maximum_y: Stochastic geometry maximum translation in y direction.
            maximum_z: Stochastic geometry maximum translation in z direction.
        """

        def __init__(self, number: int, maximum_x: float, maximum_y: float, maximum_z: float):
            """
            ``__init__`` initializes ``StochasticGeometryValue``.

            Parameters:
                number: Stochastic geometry universe number.
                maximum_x: Stochastic geometry maximum translation in x direction.
                maximum_y: Stochastic geometry maximum translation in y direction.
                maximum_z: Stochastic geometry maximum translation in z direction.

            Raises:
                MCNPSemanticCodes: INVALID_DATUM_PARAMETERS.
            """

            if number is None or not (1 <= number <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            if maximum_x is None:
                raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            if maximum_y is None:
                raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            if maximum_z is None:
                raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            self.number: final[int] = number
            self.maximum_x: final[float] = maximum_x
            self.maximum_y: final[float] = maximum_y
            self.maximum_z: final[float] = maximum_z

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``StochasticGeometryValue`` objects from
            INP.

            ``from_mcnp`` constructs instances of ``StochasticGeometryValue``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function.

            Parameters:
                source: INP for stochastic geometry values.

            Returns:
                ``StochasticGeometryValue`` object.

            Raises:
                MCNPSyntaxError: TOOFEW_DATUM_URAN, TOOLONG_DATUM_URAN.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_URAN))

            number = tokens.popl()
            maximum_x = tokens.popl()
            maximum_y = tokens.popl()
            maximum_z = tokens.popl()

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_URAN)

            return StochasticGeometryValue(number, maximum_x, maximum_y, maximum_z)

    def __init__(self, transformations: tuple[StochasticGeometryValue]):
        """
        ``__init__`` initializes ``StochasticGeometry``.

         Parameters:
            *transformations: Tuple of stochastric geometry transformations.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in transformations:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"uran"
        self.mnemonic = Datum.DatumMnemonic.STOCHASTIC_GEOMETRY
        self.parameters = transformations

        self.transformations = transformations


class DeterministicMaterials(Datum):
    """
    ``DeterministicMaterials`` represents INP deterministic materials data
    cards.

    ``DeterministicMaterials`` inherits attributes from ``Datum``. It
    represents the INP deterministic materials data card syntax element.

    Attributes:
        materials: Tuple of Zaids.
        suffix: Data card suffix.
    """

    def __init__(self, materials: tuple[types.Zaid], suffix: int):
        """
        ``__init__`` initializes ``DeterministicMaterials``.

        Parameters:
            materials: Tuple of ZAID aliases.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in materials:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.id: final[str] = f"dm{suffix}"
        self.mnemonic = Datum.DatumMnemonic.DETERMINISTIC_MATERIALS
        self.parameters = materials
        self.suffix = suffix

        self.materials = materials


class DeterministicWeightWindow(Datum):
    """
    ``DeterministicWeightWindow`` represents INP deterministic weight window
    data cards.

    ``DeterministicWeightWindow`` inherits attributes from ``Datum``. It
    represents the INP deterministic weight window data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
    """

    class DeterministicWeightWindowOption:
        """
        ``DeterministicWeightWindowOption`` represents INP deterministic weight
        window data card options.

        ``DeterministicWeightWindowOption`` implements INP deterministic weight
        window data card options. Its attributes store keywords and values, and
        its methods provide entry and endpoints for working with INP
        deterministic weight window data card options. It represents the
        generic INP deterministic weight window data card option syntax
        element, so ``DeterministicWeightWindow`` depends on
        ``DeterministicWeightWindowOption`` as a generic data structure and
        superclass.

        Attributes:
            keyword: Deterministic weight window data card option keyword.
            value: Deterministic weight window data card option value.
        """

        class DeterministicWeightWindowKeyword(StrEnum):
            """
            ``DeterministicWeightWindowKeyword`` represents INP deterministic
            weight window data card keywords.

            ``DeterministicWeightWindowKeyword`` implements INP deterministic
            weight window data card keywords as a Python inner class. It
            enumerates MCNP keywords and provides methods for casting strings
            to ``DeterministicWeightWindowKeyword`` instances. It represents
            the INP deterministic weight window data card keyword syntax
            element, so ``DeterministicWeightWindow`` and
            ``DeterministicWeightWindowOption`` depend on
            ``DeterministicWeightWindowKeyword`` as an enum.
            """

            POINTS = "points"
            BLOCK = "block"
            NGROUP = "ngroup"
            ISN = "isn"
            NISO = "niso"
            MT = "mt"
            IQUAD = "iquad"
            FMMIX = "fmmix"
            NOSOLV = "nosolv"
            NOEDIT = "noedit"
            NOGEOD = "nogeod"
            NOMIX = "nomix"
            NOASG = "noasg"
            NOMACR = "nomacr"
            NOSLNP = "noslnp"
            NOEDTT = "noedtt"
            NOADJM = "noadjm"
            LIB = "lib"
            LIBNAME = "libname"
            FISSNEUT = "fissneut"
            LNG = "lng"
            BALXS = "balxs"
            NTICHI = "ntichi"
            IEVT = "ievt"
            SCT = "sct"
            ITH = "ith"
            TRCOR = "trcor"
            IBL = "ibl"
            IBR = "ibr"
            IBT = "ibt"
            IBB = "ibb"
            IBFRNT = "ibfrnt"
            BIBACK = "biback"
            EPSI = "epsi"
            OITM = "oitm"
            NOSIGF = "nosigf"
            SRCACC = "srcacc"
            DIFFSOL = "diffsol"
            TSASN = "tsasn"
            TSAEPSI = "tsaepsi"
            TSAITS = "tsaits"
            TSABETA = "tsabeta"
            PTCONV = "ptconv"
            NORM = "norm"
            XESCTP = "xesctp"
            FISSRP = "fissrp"
            SOURCP = "sourcp"
            ANGP = "angp"
            BALP = "balp"
            RAFLUX = "raflux"
            RMFLUX = "rmflux"
            AVATAR = "avatar"
            ASLEFT = "asleft"
            ASRITE = "asrite"
            ASBOTT = "asbott"
            ASTOP = "astop"
            ASFRNT = "asfrnt"
            ASBACK = "asback"
            MASSED = "massed"
            PTED = "pted"
            ZNED = "zned"
            RZFLUX = "rzflux"
            RXMFLUX = "rxmflux"
            EDOUTF = "edoutf"
            BYVLOP = "byvlop"
            AJED = "ajed"
            FLUXONE = "fluxone"

            @staticmethod
            def from_mcnp(source: str):
                """
                ``from_mcnp`` generates ``DeterministicWeightWindowKeyword``
                objects from INP.

                ``from_mcnp`` constructs instances of
                ``DeterministicWeightWindowKeyword`` from INP source strings,
                so it operates as a class constructor method and INP parser
                helper function.

                Parameters:
                    source: INP for deterministic weight window keyword.

                Returns:
                    ``DeterministicWeightWindowKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_DAWWG_KEYWORD.
                """

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in DeterministicWeightWindowKeyword]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

                return DeterministicWeightWindowKeyword(source)

        def __init__(self, keyword: DeterministicWeightWindowKeyword, value: any):
            """
            ``__init__`` initializes ``DeterministicWeightWindowOption``.

            Parameters:
                keyword: Deterministic weight window data card option keyword.
                value:  Deterministic weight window data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

            match keyword:
                case DeterministicWeightWindowKeyword.POINTS:
                    obj = DeterministicWeightWindow.Points(keyword, value)
                case DeterministicWeightWindowKeyword.XSEC:
                    obj = DeterministicWeightWindow.Xsec(keyword, value)
                case DeterministicWeightWindowKeyword.TALLY:
                    obj = DeterministicWeightWindow.Tally(keyword, value)
                case DeterministicWeightWindowKeyword.BLOCK:
                    obj = DeterministicWeightWindow.Block(keyword, value)
                case DeterministicWeightWindowKeyword.NGROUP:
                    obj = DeterministicWeightWindow.Ngroup(keyword, value)
                case DeterministicWeightWindowKeyword.ISN:
                    obj = DeterministicWeightWindow.Isn(keyword, value)
                case DeterministicWeightWindowKeyword.NISO:
                    obj = DeterministicWeightWindow.Niso(keyword, value)
                case DeterministicWeightWindowKeyword.MT:
                    obj = DeterministicWeightWindow.Mt(keyword, value)
                case DeterministicWeightWindowKeyword.IQUAD:
                    obj = DeterministicWeightWindow.Iquad(keyword, value)
                case DeterministicWeightWindowKeyword.FMMIX:
                    obj = DeterministicWeightWindow.Fmmix(keyword, value)
                case DeterministicWeightWindowKeyword.NOSOLV:
                    obj = DeterministicWeightWindow.Nosolv(keyword, value)
                case DeterministicWeightWindowKeyword.NOEDIT:
                    obj = DeterministicWeightWindow.Noedit(keyword, value)
                case DeterministicWeightWindowKeyword.NOGEOD:
                    obj = DeterministicWeightWindow.Nogeod(keyword, value)
                case DeterministicWeightWindowKeyword.NOMIX:
                    obj = DeterministicWeightWindow.Nomix(keyword, value)
                case DeterministicWeightWindowKeyword.NOASG:
                    obj = DeterministicWeightWindow.Noasg(keyword, value)
                case DeterministicWeightWindowKeyword.NOMACR:
                    obj = DeterministicWeightWindow.Nomacr(keyword, value)
                case DeterministicWeightWindowKeyword.NOSLNP:
                    obj = DeterministicWeightWindow.Noslnp(keyword, value)
                case DeterministicWeightWindowKeyword.NOEDTT:
                    obj = DeterministicWeightWindow.Noedtt(keyword, value)
                case DeterministicWeightWindowKeyword.NOADJM:
                    obj = DeterministicWeightWindow.Noadjm(keyword, value)
                case DeterministicWeightWindowKeyword.LIB:
                    obj = DeterministicWeightWindow.Lib(keyword, value)
                case DeterministicWeightWindowKeyword.LIBNAME:
                    obj = DeterministicWeightWindow.Libname(keyword, value)
                case DeterministicWeightWindowKeyword.FISSNEUT:
                    obj = DeterministicWeightWindow.Fissneut(keyword, value)
                case DeterministicWeightWindowKeyword.LNG:
                    obj = DeterministicWeightWindow.Lng(keyword, value)
                case DeterministicWeightWindowKeyword.BALXS:
                    obj = DeterministicWeightWindow.Balxs(keyword, value)
                case DeterministicWeightWindowKeyword.NTICHI:
                    obj = DeterministicWeightWindow.Ntichi(keyword, value)
                case DeterministicWeightWindowKeyword.IEVT:
                    obj = DeterministicWeightWindow.Ievt(keyword, value)
                case DeterministicWeightWindowKeyword.SCT:
                    obj = DeterministicWeightWindow.Isct(keyword, value)
                case DeterministicWeightWindowKeyword.ITH:
                    obj = DeterministicWeightWindow.Ith(keyword, value)
                case DeterministicWeightWindowKeyword.TRCOR:
                    obj = DeterministicWeightWindow.Trcor(keyword, value)
                case DeterministicWeightWindowKeyword.IBL:
                    obj = DeterministicWeightWindow.Ibl(keyword, value)
                case DeterministicWeightWindowKeyword.IBR:
                    obj = DeterministicWeightWindow.Ibr(keyword, value)
                case DeterministicWeightWindowKeyword.IBT:
                    obj = DeterministicWeightWindow.Ibt(keyword, value)
                case DeterministicWeightWindowKeyword.IBB:
                    obj = DeterministicWeightWindow.Ibb(keyword, value)
                case DeterministicWeightWindowKeyword.IBFRNT:
                    obj = DeterministicWeightWindow.Ibfrnt(keyword, value)
                case DeterministicWeightWindowKeyword.BIBACK:
                    obj = DeterministicWeightWindow.Ibback(keyword, value)
                case DeterministicWeightWindowKeyword.EPSI:
                    obj = DeterministicWeightWindow.Epsi(keyword, value)
                case DeterministicWeightWindowKeyword.OITM:
                    obj = DeterministicWeightWindow.Oitm(keyword, value)
                case DeterministicWeightWindowKeyword.NOSIGF:
                    obj = DeterministicWeightWindow.Nosigf(keyword, value)
                case DeterministicWeightWindowKeyword.SRCACC:
                    obj = DeterministicWeightWindow.Srcacc(keyword, value)
                case DeterministicWeightWindowKeyword.DIFFSOL:
                    obj = DeterministicWeightWindow.Diffsol(keyword, value)
                case DeterministicWeightWindowKeyword.TSASN:
                    obj = DeterministicWeightWindow.Tsasn(keyword, value)
                case DeterministicWeightWindowKeyword.TSAEPSI:
                    obj = DeterministicWeightWindow.Tsaepsi(keyword, value)
                case DeterministicWeightWindowKeyword.TSAITS:
                    obj = DeterministicWeightWindow.Tsaits(keyword, value)
                case DeterministicWeightWindowKeyword.TSABETA:
                    obj = DeterministicWeightWindow.Tsabeta(keyword, value)
                case DeterministicWeightWindowKeyword.PTCONV:
                    obj = DeterministicWeightWindow.Ptconv(keyword, value)
                case DeterministicWeightWindowKeyword.NORM:
                    obj = DeterministicWeightWindow.Norm(keyword, value)
                case DeterministicWeightWindowKeyword.XESCTP:
                    obj = DeterministicWeightWindow.Xesctp(keyword, value)
                case DeterministicWeightWindowKeyword.FISSRP:
                    obj = DeterministicWeightWindow.Fissrp(keyword, value)
                case DeterministicWeightWindowKeyword.SOURCP:
                    obj = DeterministicWeightWindow.Sourcp(keyword, value)
                case DeterministicWeightWindowKeyword.ANGP:
                    obj = DeterministicWeightWindow.Angp(keyword, value)
                case DeterministicWeightWindowKeyword.BALP:
                    obj = DeterministicWeightWindow.Balp(keyword, value)
                case DeterministicWeightWindowKeyword.RAFLUX:
                    obj = DeterministicWeightWindow.Raflux(keyword, value)
                case DeterministicWeightWindowKeyword.RMFLUX:
                    obj = DeterministicWeightWindow.Rmflux(keyword, value)
                case DeterministicWeightWindowKeyword.AVATAR:
                    obj = DeterministicWeightWindow.Avatar(keyword, value)
                case DeterministicWeightWindowKeyword.ASLEFT:
                    obj = DeterministicWeightWindow.Asleft(keyword, value)
                case DeterministicWeightWindowKeyword.ASRITE:
                    obj = DeterministicWeightWindow.Asrite(keyword, value)
                case DeterministicWeightWindowKeyword.ASBOTT:
                    obj = DeterministicWeightWindow.Asbott(keyword, value)
                case DeterministicWeightWindowKeyword.ASTOP:
                    obj = DeterministicWeightWindow.Astop(keyword, value)
                case DeterministicWeightWindowKeyword.ASFRNT:
                    obj = DeterministicWeightWindow.Asfrnt(keyword, value)
                case DeterministicWeightWindowKeyword.ASBACK:
                    obj = DeterministicWeightWindow.Asback(keyword, value)
                case DeterministicWeightWindowKeyword.MASSED:
                    obj = DeterministicWeightWindow.Massed(keyword, value)
                case DeterministicWeightWindowKeyword.PTED:
                    obj = DeterministicWeightWindow.Pted(keyword, value)
                case DeterministicWeightWindowKeyword.ZNED:
                    obj = DeterministicWeightWindow.Zned(keyword, value)
                case DeterministicWeightWindowKeyword.RZFLUX:
                    obj = DeterministicWeightWindow.Rzflux(keyword, value)
                case DeterministicWeightWindowKeyword.RXMFLUX:
                    obj = DeterministicWeightWindow.Rzmflux(keyword, value)
                case DeterministicWeightWindowKeyword.EDOUTF:
                    obj = DeterministicWeightWindow.Edoutf(keyword, value)
                case DeterministicWeightWindowKeyword.BYVLOP:
                    obj = DeterministicWeightWindow.Byvlop(keyword, value)
                case DeterministicWeightWindowKeyword.AJED:
                    obj = DeterministicWeightWindow.Ajed(keyword, value)
                case DeterministicWeightWindowKeyword.FLUXONE:
                    obj = DeterministicWeightWindow.Fluxone(keyword, value)

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``DeterministicWeightWindowOption`` objects
            from INP.

            ``from_mcnp`` constructs instances of
            ``DeterministicWeightWindowOption`` from INP source strings, so it
            operates as a class constructor method and INP parser helper
            function. Although defined on the superclass, it returns
            ``DeterministicWeightWindowOption`` subclasses.

            Parameters:
                source: INP for deterministic weight window data card option.

            Returns:
                ``DeterministicWeightWindowOption`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_KEYWORD.
                MCNPSyntaxError: TOOFEW_DATUM_DAWWG, TOOLONG_DATUM_DAWWG.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_DAWWG))

            # Processing Keyword
            keyword = DeterministicWeightWindowOption.DeterministicWeightWindowKeyword.cast_keyword(tokens.peekl())

            # Processing Values
            match keyword:
                case DeterministicWeightWindowKeyword.POINTS | DeterministicWeightWindowKeyword.BLOCK | DeterministicWeightWindowKeyword.NGROUP | DeterministicWeightWindowKeyword.ISN | DeterministicWeightWindowKeyword.NISO | DeterministicWeightWindowKeyword.MT | DeterministicWeightWindowKeyword.IQUAD | DeterministicWeightWindowKeyword.FMMIX | DeterministicWeightWindowKeyword.NOSOLV | DeterministicWeightWindowKeyword.NOEDIT | DeterministicWeightWindowKeyword.NOGEOD | DeterministicWeightWindowKeyword.NOMIX | DeterministicWeightWindowKeyword.NOASG | DeterministicWeightWindowKeyword.NOMACR | DeterministicWeightWindowKeyword.NOSLNP | DeterministicWeightWindowKeyword.NOEDTT | DeterministicWeightWindowKeyword.NOADJM | DeterministicWeightWindowKeyword.FISSNEUT | DeterministicWeightWindowKeyword.LNG | DeterministicWeightWindowKeyword.BALXS | DeterministicWeightWindowKeyword.NTICHI | DeterministicWeightWindowKeyword.IEVT | DeterministicWeightWindowKeyword.SCT | DeterministicWeightWindowKeyword.ITH | DeterministicWeightWindowKeyword.TRCOR | DeterministicWeightWindowKeyword.IBL | DeterministicWeightWindowKeyword.IBR | DeterministicWeightWindowKeyword.IBT | DeterministicWeightWindowKeyword.IBB | DeterministicWeightWindowKeyword.IBFRNT | DeterministicWeightWindowKeyword.BIBACK | DeterministicWeightWindowKeyword.OITM | DeterministicWeightWindowKeyword.NOSIGF | DeterministicWeightWindowKeyword.TSASN | DeterministicWeightWindowKeyword.TSAEPSI | DeterministicWeightWindowKeyword.PTCONV | DeterministicWeightWindowKeyword.XESCTP | DeterministicWeightWindowKeyword.FISSRP | DeterministicWeightWindowKeyword.SOURCP | DeterministicWeightWindowKeyword.ANGP | DeterministicWeightWindowKeyword.BALP | DeterministicWeightWindowKeyword.RAFLUX | DeterministicWeightWindowKeyword.RMFLUX | DeterministicWeightWindowKeyword.AVATAR | DeterministicWeightWindowKeyword.ASLEFT | DeterministicWeightWindowKeyword.ASRITE | DeterministicWeightWindowKeyword.ASBOTT | DeterministicWeightWindowKeyword.ASTOP | DeterministicWeightWindowKeyword.ASFRNT | DeterministicWeightWindowKeyword.ASBACK | DeterministicWeightWindowKeyword.MASSED | DeterministicWeightWindowKeyword.PTED | DeterministicWeightWindowKeyword.ZNED | DeterministicWeightWindowKeyword.RZFLUX | DeterministicWeightWindowKeyword.RXMFLUX | DeterministicWeightWindowKeyword.EDOUTF | DeterministicWeightWindowKeyword.BYVLOP | DeterministicWeightWindowKeyword.AJED | DeterministicWeightWindowKeyword.FLUXONE:
                    value = types.cast_fortran_integer(tokens.popl())
                case DeterministicWeightWindowKeyword.LIB | DeterministicWeightWindowKeyword.LIBNAME | DeterministicWeightWindowKeyword.TRCOR | DeterministicWeightWindowKeyword.SRCACC | DeterministicWeightWindowKeyword.DIFFSOL:
                    value = types.cast_fortran_real(tokens.popl())
                case DeterministicWeightWindowKeyword.EPSI | DeterministicWeightWindowKeyword.TSAEPSI | DeterministicWeightWindowKeyword.TSAITS | DeterministicWeightWindowKeyword.TSABETA:
                    value = tokens.popl()
                case _:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_DAWWG)

            return DeterministicWeightWindowOption(keyword, value)

    class Points(DeterministicWeightWindowOption):
        """
        ``Points`` represents INP points deterministic weight window data card
        options.

        ``Points`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP points
        deterministic weight window data card option syntax element.

        Attributes:
            point: Deterministic weight window data card sample point count.
        """

        def __init__(self, point: int):
            """
            ``__init__`` initializes ``Points``.

            Parameters:
                point: Deterministic weight window data card sample point count.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.POINTS
            self.value = value
            self.point = value

    class Block(DeterministicWeightWindowOption):
        """
        ``Block`` represents INP block deterministic weight window data card
        options.

        ``Block`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP block deterministic weight window data card
        option syntax element.

        Attributes:
            state: PARTISN input file passed value setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Block``.

            Parameters:
                state: PARTISN input file passed value setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {1, 3, 5, 6}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BLOCK
            self.value = value
            self.state = value

    class Ngroup(DeterministicWeightWindowOption):
        """
        ``Ngroup`` represents INP ngroup deterministic weight window data card
        options.

        ``Ngroup`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ngroup
        deterministic weight window data card option syntax element.

        Attributes:
            energy_group_number: DAWWG energy group count.
        """

        def __init__(self, energy_group_number: int):
            """
            ``__init__`` initializes ``Ngroup``.

            Parameters:
                energy_group_number: DAWWG energy group count.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NGROUP
            self.value = value
            self.energy_group_number = value

    class Isn(DeterministicWeightWindowOption):
        """
        ``Isn`` represents INP isn deterministic weight window data card
        options.

        ``Isn`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP isn deterministic weight window data option
        syntax element.

        Attributes:
            sn_order: DAWWG Sn order.
        """

        def __init__(self, sn_order: int):
            """
            ``__init__`` initializes ``Isn``.

            Parameters:
                sn_order: DAWWG Sn order.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ISN
            self.value = value
            self.sn_order = value

    class Niso(DeterministicWeightWindowOption):
        """
        ``Niso`` represents INP niso deterministic weight window data card
        options.

        ``Niso`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP niso deterministic weight window data card option
        syntax element.

        Attributes:
            isotopes_number: DAWWG isotopes number.
        """

        def __init__(self, isotopes_number: int):
            """
            ``__init__`` initializes ``Niso``.

            Parameters:
                isotopes_number: DAWWG isotopes number.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NISO
            self.value = value
            self.isotopes_number = value

    class Mt(DeterministicWeightWindowOption):
        """
        ``Mt`` represents INP mt deterministic weight window data card options.

        ``Mt`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP mt deterministic weight window data card option
        syntax element.

        Attributes:
            materials_number: DAWWG materials number.
        """

        def __init__(self, materials_number: int):
            """
            ``__init__`` initializes ``Mt``.

            Parameters:
                materials_number: DAWWG materials number.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.MT
            self.value = value
            self.materials_number = value

    class Iquad(DeterministicWeightWindowOption):
        """
        ``Iquad`` represents INP iquad deterministic weight window data card
        options.

        ``Iquad`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP iquad deterministic weight window data card
        option syntax element.

        Attributes:
            quadrature: DAWWG quadrature.
        """

        def __init__(self, quadrature: int):
            """
            ``__init__`` initializes ``Iquad``.

            Parameters:
                quadrature: DAWWG quadrature.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {1, 3, 4, 5, 6, 7, 8, 9}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IQUAD
            self.value = value
            self.quadrature = value

    class Fmmix(DeterministicWeightWindowOption):
        """
        ``Fmmix`` represents INP fmmix deterministic weight window data card
        options.

        ``Fmmix`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP fmmix deterministic weight window data card
        option sytnax element.

        Attributes:
            state: DAWWG LNK3DNT reading comprehension toggle.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Fmmix``.

            Parameters:
                state: DAWWG LNK3DNT reading comprehension toggle.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.FMMIX
            self.value = value
            self.state = value

    class Nosolv(DeterministicWeightWindowOption):
        """
        ``Nosolv`` represents INP nosolv deterministic weight window data card
        options.

        ``Nosolv`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP nosolv
        deterministic weight window data card option syntax element

        Attributes:
            state: Suppress solver module setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nosolv``.

            Parameters:
                state: Suppress solver module setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOSOLV
            self.value = value
            self.state = value

    class Noedit(DeterministicWeightWindowOption):
        """
        ``Noedit`` represents INP noedit deterministic weight window data card
        options.

        ``Noedit`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP noedit
        deterministic weight window data card option syntax element.

        Attributes:
            state: Suppress edit module setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noedit``.

            Parameters:
                state: Suppress edit module setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOEDIT
            self.value = value
            self.state = value

    class Nogeod(DeterministicWeightWindowOption):
        """
        ``Nogeod`` represents INP nogeod deterministic weight window data card
        options.

        ``Nogeod`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP nogeod
        deterministic weight window data card option syntax element.

        Attributes:
            state: Supress writing GEODST file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nogeod``.

            Parameters:
                state: Supress writing GEODST file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOGEOD
            self.value = value
            self.state = value

    class Nomix(DeterministicWeightWindowOption):
        """
        ``Nomix`` represents INP nomix deterministic weight window data card
        options.

        ``Nomix`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP nomix deterministic weight window data card
        option syntax element.

        Attributes:
            state: Suppress writing mixing file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nomix``.

            Parameters:
                state: Suppress writing mixing file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOMIX
            self.value = value
            self.state = value

    class Noasg(DeterministicWeightWindowOption):
        """
        ``Noasg`` represents INP noasg deterministic weight window data card
        options.

        ``Noasg`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP noasg deterministic weight window data card
        option syntax element.

        Attributes:
            state: Suppress wirting ASGMAT file seting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noasg``.

            Parameters:
                state: Suppress wirting ASGMAT file seting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOASG
            self.value = value
            self.state = value

    class Nomacr(DeterministicWeightWindowOption):
        """
        ``Nomacr`` represents INP nomacr deterministic weight window data card
        options.

        ``Nomacr`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP nomacr
        deterministic weight window data card option syntax element.

        Attributes:
            state: Suppress writing MACRXS file.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nomacr``.

            Parameters:
                state: Suppress writing MACRXS file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOMACR
            self.value = value
            self.state = value

    class Noslnp(DeterministicWeightWindowOption):
        """
        ``Noslnp`` represents INP noslnp deterministic weight window data card
        options.

        ``Noslnp`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP noslnp
        deterministic weight window data card option syntax element.

        Attributes:
            state: Suppress writing SOLINP file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noslnp``.

            Parameters:
                state: Suppress writing SOLINP file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOSLNP
            self.value = value
            self.state = value

    class Noedtt(DeterministicWeightWindowOption):
        """
        ``Noedtt`` represents INP noedtt deterministic weight window data card
        options.

        ``Noedtt`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP noedtt
        deterministic weight window data card option syntax element.

        Attributes:
            state: Supress writing EDITIT file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noedtt``.

            Parameters:
                state: Supress writing EDITIT file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOEDTT
            self.value = value
            self.state = value

    class Noadjm(DeterministicWeightWindowOption):
        """
        ``Noadjm`` represents INP noadjm deterministic weight window data card
        options.

        ``Noadjm`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP noadjm
        deterministic weight window data card option syntax element.

        Attributes:
            state: Suppress writing ADJMAC file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Noadjm``.

            Parameters:
                state: Suppress writing ADJMAC file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOADJM
            self.value = value
            self.state = value

    class Lib(DeterministicWeightWindowOption):
        """
        ``Lib`` represents lib deterministic weight window datacell coptions.

        ``Lib`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Libents deterministic weight window data cell option
        syntax element.

        Attributes:
            name: Name/Form of corss-seciotn data file.
        """

        def __init__(self, name: str):
            """
            ``__init__`` initializes ``Lib``.

            Parameters:
                name: Name/Form of corss-seciotn data file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.LIB
            self.value = value
            self.name = value

    class Libname(DeterministicWeightWindowOption):
        """
        ``Libname`` represents INP libname deterministic weight window data
        card options.

        ``Libname`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP libname
        deterministic weight window data card option syntax element.

        Attributes:
            filename: Cross-section file name.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Libname``.

            Parameters:
                filename: Cross-section file name.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.LIBNAME
            self.value = value
            self.filename = value

    class Fissneut(DeterministicWeightWindowOption):
        """
        ``Fissneut`` represents INP fissneut deterministic weight window data
        card options.

        ``Fissneut`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP fissneut
        deterministic weight window data card option syntax element.

        Attributes:
            fission_neutron_flag: Fission neutron flag.
        """

        def __init__(self, fission_neutron_flag: int):
            """
            ``__init__`` initializes ``Fissneut``.

            Parameters:
                fission_neutron_flag: Fission neutron flag.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.FISSNEUT
            self.value = value
            self.fission_neutron_flag = value

    class Lng(DeterministicWeightWindowOption):
        """
        ``Lng`` represents lng deterministic weight window datacell coptions.

        ``Lng`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Lngents deterministic weight window datacell coption
        syntax element.

        Attributes:
            last_neutron_group_number: Number of the last neutron group.
        """

        def __init__(self, last_neutron_group_number: int):
            """
            ``__init__`` initializes ``Lng``.

            Parameters:
                last_neutron_group_number: Number of the last neutron group.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.LNG
            self.value = value
            self.last_neutron_group_number = value

    class Balxs(DeterministicWeightWindowOption):
        """
        ``Balxs`` represents INP balxs deterministic weight window data card
        options.

        ``Balxs`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP balxs deterministic weight window data card
        option syntax element.

        Attributes:
            cross_section_balance_control: Cross-section balance control.
        """

        def __init__(self, cross_section_balance_control: int):
            """
            ``__init__`` initializes ``Balxs``.

            Parameters:
                cross_section_balance_control: Cross-section balance control.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BALXS
            self.value = value
            self.cross_section_balance_control = value

    class Ntichi(DeterministicWeightWindowOption):
        """
        ``Ntichi`` represents INP ntichi deterministic weight window data card
        options.

        ``Ntichi`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ntichi
        deterministic weight window data card option syntax element.

        Attributes:
            mendf_fission_fraction: MENDF fission fraction to use.
        """

        def __init__(self, mendf_fission_fraction: int):
            """
            ``__init__`` initializes ``Ntichi``.

            Parameters:
                mendf_fission_fraction: MENDF fission fraction to use.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NTICHI
            self.value = value
            self.mendf_fission_fraction = value

    class Ievt(DeterministicWeightWindowOption):
        """
        ``Ievt`` represents INP ievt deterministic weight window data card
        options.

        ``Ievt`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP ievt deterministic weight window data card option
        syntax element.

        Attributes:
            calculation_type: Calculation type.
        """

        def __init__(self, calculation_type: int):
            """
            ``__init__`` initializes ``Ievt``.

            Parameters:
                calculation_type: Calculation type.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1, 2, 3, 4}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IEVT
            self.value = value
            self.calculation_type = value

    class Isct(DeterministicWeightWindowOption):
        """
        ``Isct`` represents INP isct deterministic weight window data card
        options.

        ``Isct`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP isct deterministic weight window data card option
        syntax element.

        Attributes:
            legendre_order: Legendre order.
        """

        def __init__(self, legendre_order: int):
            """
            ``__init__`` initializes ``Isct``.

            Parameters:
                legendre_order: Legendre order.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.SCT
            self.value = value
            self.legendre_order = value

    class Ith(DeterministicWeightWindowOption):
        """
        ``Ith`` represents ith deterministic weight window datacell coptions.

        ``Ith`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Ithents deterministic weight window datacell coption
        syntax element.

        Attributes:
            calculation_state: Direct or adjoint calculation.
        """

        def __init__(self, calculation_state: int):
            """
            ``__init__`` initializes ``Ith``.

            Parameters:
                calculation_state: Direct or adjoint calculation.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ITH
            self.value = value
            self.calculation_state = value

    class Trcor(DeterministicWeightWindowOption):
        """
        ``Trcor`` represents INP trcor deterministic weight window data card
        options.

        ``Trcor`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP trcor deterministic weight window data card
        option syntax element.

        Attributes:
            trcor: trcor.
        """

        def __init__(self, trcor: str):
            """
            ``__init__`` initializes ``Trcor``.

            Parameters:
                trcor: trcor.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TRCOR
            self.value = value
            self.trcor = value

    class Ibl(DeterministicWeightWindowOption):
        """
        ``Ibl`` represents ibl deterministic weight window datacell coptions.

        ``Ibl`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Iblents deterministic weight window datacell coption
        syntax element.

        Attributes:
            left_boundary: Left boundary condition.
        """

        def __init__(self, left_boundary: int):
            """
            ``__init__`` initializes ``Ibl``.

            Parameters:
                left_boundary: Left boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBL
            self.value = value
            self.left_boundary = value

    class Ibr(DeterministicWeightWindowOption):
        """
        ``Ibr`` represents ibr deterministic weight window datacell coptions.

        ``Ibr`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Ibrents deterministic weight window datacell coption
        syntax element.

        Attributes:
            right_boundary: Right boundary condition.
        """

        def __init__(self, right_boundary: int):
            """
            ``__init__`` initializes ``Ibr``.

            Parameters:
                right_boundary: Right boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBR
            self.value = value
            self.right_boundary = value

    class Ibt(DeterministicWeightWindowOption):
        """
        ``Ibt`` represents ibt deterministic weight window datacell coptions.

        ``Ibt`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Ibtents deterministic weight window datacell coption
        syntax element.

        Attributes:
            top_boundary: Top boundary condition.
        """

        def __init__(self, top_boundary: int):
            """
            ``__init__`` initializes ``Ibt``.

            Parameters:
                top_boundary: Top boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBT
            self.value = value
            self.top_boundary = value

    class Ibb(DeterministicWeightWindowOption):
        """
        ``Ibb`` represents ibb deterministic weight window datacell coptions.

        ``Ibb`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the Ibbents deterministic weight window datacell coption
        syntax element.

        Attributes:
            bottom_boundary: Bottom boundary condition.
        """

        def __init__(self, bottom_boundary: int):
            """
            ``__init__`` initializes ``Ibb``.

            Parameters:
                bottom_boundary: Bottom boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBB
            self.value = value
            self.bottom_boundary = value

    class Ibfrnt(DeterministicWeightWindowOption):
        """
        ``Ibfrnt`` represents INP ibfrnt deterministic weight window data card
        options.

        ``Ibfrnt`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ibfrnt
        deterministic weight window data card option syntax element.

        Attributes:
            front_boundary: Front boundary condition.
        """

        def __init__(self, front_boundary: int):
            """
            ``__init__`` initializes ``Ibfrnt``.

            Parameters:
                front_boundary: Front boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.IBFRNT
            self.value = value
            self.front_boundary = value

    class Ibback(DeterministicWeightWindowOption):
        """
        ``Ibback`` represents INP ibback deterministic weight window data card
        options.

        ``Ibback`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ibback
        deterministic weight window data card option syntax element.

        Attributes:
            back_boundary: Back boundary condition.
        """

        def __init__(self, back_boundary: int):
            """
            ``__init__`` initializes ``Ibback``.

            Parameters:
                back_boundary: Back boundary condition.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BIBACK
            self.value = value
            self.back_boundary = value

    class Epsi(DeterministicWeightWindowOption):
        """
        ``Epsi`` represents INP epsi deterministic weight window data card
        options.

        ``Epsi`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP epsi deterministic weight window data card option
        syntax element.

        Attributes:
            Convergence percision: Convergence percision.
        """

        def __init__(self, convergence_percision: float):
            """
            ``__init__`` initializes ``Epsi``.

            Parameters:
                Convergence percision: Convergence percision.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.EPSI
            self.value = value
            self.convergence_percision = value

    class Oitm(DeterministicWeightWindowOption):
        """
        ``Oitm`` represents INP oitm deterministic weight window data card
        options.

        ``Oitm`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP oitm deterministic weight window data card option
        syntax element.

        Attributes:
            maximnum_outer_iteration: Maximum outer iteration count.
        """

        def __init__(self, maximum_outer_iteration: int):
            """
            ``__init__`` initializes ``Oitm``.

            Parameters:
                maximnum_outer_iteration: Maximum outer iteration count.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.OITM
            self.value = value
            self.maximum_outer_iteration = value

    class Nosigf(DeterministicWeightWindowOption):
        """
        ``Nosigf`` represents INP nosigf deterministic weight window data card
        options.

        ``Nosigf`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP nosigf
        deterministic weight window data card option syntax element.

        Attributes:
            state: Inhibit fission multiplication setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Nosigf``.

            Parameters:
                state: Inhibit fission multiplication setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NOSIGF
            self.value = value
            self.state = value

    class Srcacc(DeterministicWeightWindowOption):
        """
        ``Srcacc`` represents INP srcacc deterministic weight window data card
        options.

        ``Srcacc`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP srcacc
        deterministic weight window data card option syntax element.

        Attributes:
            transport_accelerations: Transport accelerations.
        """

        def __init__(self, transport_accelerations: str):
            """
            ``__init__`` initializes ``Srcacc``.

            Parameters:
                transport_accelerations: Transport accelerations.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.SRCACC
            self.value = value
            self.transport_accelerations = value

    class Diffsol(DeterministicWeightWindowOption):
        """
        ``Diffsol`` represents INP diffsol deterministic weight window data
        card options.

        ``Diffsol`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP diffsol
        deterministic weight window data card option syntax element.

        Attributes:
            diffusion_operator_solver: Diffusion operator solver.
        """

        def __init__(self, diffusion_operator_solver: str):
            """
            ``__init__`` initializes ``Diffsol``.

            Parameters:
                diffusion_operator_solver: Diffusion operator solver.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.DIFFSOL
            self.value = value
            self.diffusion_operator_solver = value

    class Tsasn(DeterministicWeightWindowOption):
        """
        ``Tsasn`` represents INP tsasn deterministic weight window data card
        options.

        ``Tsasn`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP tsasn deterministic weight window data card
        option syntax element.

        Attributes:
            sn_order: Sn order for low order TSA sweeps.
        """

        def __init__(self, sn_order: int):
            """
            ``__init__`` initializes ``Tsasn``.

            Parameters:
                sn_order: Sn order for low order TSA sweeps.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TSASN
            self.value = value
            self.sn_order = value

    class Tsaepsi(DeterministicWeightWindowOption):
        """
        ``Tsaepsi`` represents INP tsaepsi deterministic weight window data
        card options.

        ``Tsaepsi`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP tsaepsi
        deterministic weight window data card option syntax element.

        Attributes:
            convergence_criteria: Convergence criteria for TSA sweeps.
        """

        def __init__(self, convergence_criteria: float):
            """
            ``__init__`` initializes ``Tsaepsi``.

            Parameters:
                convergence_criteria: Convergence criteria for TSA sweeps.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TSAEPSI
            self.value = value
            self.convergence_criteria = value

    class Tsaits(DeterministicWeightWindowOption):
        """
        ``Tsaits`` represents INP tsaits deterministic weight window data card
        options.

        ``Tsaits`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP tsaits
        deterministic weight window data card option syntax element.

        Attributes:
            maximum_tsa_iteration: Maximmum TSA iteration count.
        """

        def __init__(self, maximum_tsa_iteration: int):
            """
            ``__init__`` initializes ``Tsaits``.

            Parameters:
                maximum_tsa_iteration: Maximmum TSA iteration count.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TSAITS
            self.value = value
            self.maximum_tsa_iteration = value

    class Tsabeta(DeterministicWeightWindowOption):
        """
        ``Tsabeta`` represents INP tsabeta deterministic weight window data
        card options.

        ``Tsabeta`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP tsabeta
        deterministic weight window data card option syntax element.

        Attributes:
            tsa_scattering_corss_section: Scatting cross-section reduction.
        """

        def __init__(self, tsa_scattering_cross_section: float):
            """
            ``__init__`` initializes ``Tsabeta``.

            Parameters:
                tsa_scattering_corss_section: Scatting cross-section reduction.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.TSABETA
            self.value = value
            self.tsa_scattering_cross_section = value

    class Ptconv(DeterministicWeightWindowOption):
        """
        ``Ptconv`` represents INP ptconv deterministic weight window data card
        options.

        ``Ptconv`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP ptconv
        deterministic weight window data card option syntax element.

        Attributes:
            state: Special criticality convergence scheme.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Ptconv``.

            Parameters:
                state: Special criticality convergence scheme.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.PTCONV
            self.value = value
            self.state = value

    class Norm(DeterministicWeightWindowOption):
        """
        ``Norm`` represents INP norm deterministic weight window data card
        options.

        ``Norm`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP norm deterministic weight window data card option
        syntax element.

        Attributes:
            norm: Norm.
        """

        def __init__(self, norm: float):
            """
            ``__init__`` initializes ``Norm``.

            Parameters:
                norm: Norm.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.NORM
            self.value = value
            self.norm = value

    class Xesctp(DeterministicWeightWindowOption):
        """
        ``Xesctp`` represents INP xesctp deterministic weight window data card
        options.

        ``Xesctp`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP xesctp
        deterministic weight window data card option syntax element.

        Attributes:
            cross_section_print_flag: Corss-section print flag.
        """

        def __init__(self, cross_section_print_flag: int):
            """
            ``__init__`` initializes ``Xesctp``.

            Parameters:
                cross_section_print_flag: Corss-section print flag.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.XESCTP
            self.value = value
            self.cross_section_print_flag = value

    class Fissrp(DeterministicWeightWindowOption):
        """
        ``Fissrp`` represents INP fissrp deterministic weight window data card
        options.

        ``Fissrp`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP fissrp
        deterministic weight window data card option syntax element.

        Attributes:
            state: Print fission source rate.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Fissrp``.

            Parameters:
                state: Print fission source rate.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.FISSRP
            self.value = value
            self.state = value

    class Sourcp(DeterministicWeightWindowOption):
        """
        ``Sourcp`` represents INP sourcp deterministic weight window data card
        options.

        ``Sourcp`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP sourcp
        deterministic weight window data card option syntax element.

        Attributes:
           source_print_flag: Source print flag.
        """

        def __init__(self, source_print_flag: int):
            """
            ``__init__`` initializes ``Sourcp``.

            Parameters:
                ource_print_flag: Source print flag.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1, 2, 3}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.SOURCP
            self.value = value
            self.source_print_flag = value

    class Angp(DeterministicWeightWindowOption):
        """
        ``Angp`` represents INP angp deterministic weight window data card
        options.

        ``Angp`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP angp deterministic weight window data card option
        syntax element.

        Attributes:
            state: Print angular flux setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Angp``.

            Parameters:
                state: Print angular flux setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ANGP
            self.value = value
            self.state = value

    class Balp(DeterministicWeightWindowOption):
        """
        ``Balp`` represents INP balp deterministic weight window data card
        options.

        ``Balp`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP balp deterministic weight window data card option
        syntax element.

        Attributes:
            state: Print coarse-mesh balance tables setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Balp``.

            Parameters:
                state: Print coarse-mesh balance tables setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BALP
            self.value = value
            self.state = value

    class Raflux(DeterministicWeightWindowOption):
        """
        ``Raflux`` represents INP raflux deterministic weight window data card
        options.

        ``Raflux`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP raflux
        deterministic weight window data card option syntax element.

        Attributes:
            state: Prepare angular flux file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Raflux``.

            Parameters:
                state: Prepare angular flux file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.RAFLUX
            self.value = value
            self.state = value

    class Rmflux(DeterministicWeightWindowOption):
        """
        ``Rmflux`` represents INP rmflux deterministic weight window data card
        options.

        ``Rmflux`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP rmflux
        deterministic weight window data card option syntax element.

        Attributes:
            state: Prepare flux moments file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Rmflux``.

            Parameters:
                state: Prepare flux moments file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.RMFLUX
            self.value = value
            self.state = value

    class Avatar(DeterministicWeightWindowOption):
        """
        ``Avatar`` represents INP avatar deterministic weight window data card
        options.

        ``Avatar`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP avatar
        deterministic weight window data card option syntax element.

        Attributes:
            state: Prepare special XMFLUXA file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Avatar``.

            Parameters:
                state: Prepare special XMFLUXA file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.AVATAR
            self.value = value
            self.state = value

    class Asleft(DeterministicWeightWindowOption):
        """
        ``Asleft`` represents INP asleft deterministic weight window data card
        options.

        ``Asleft`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asleft
        deterministic weight window data card option syntax element.

        Attributes:
            right_going_flux: Right-going flux at plane i.
        """

        def __init__(self, right_going_flux: int):
            """
            ``__init__`` initializes ``Asleft``.

            Parameters:
                right_going_flux: Right-going flux at plane i.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASLEFT
            self.value = value
            self.right_going_flux = value

    class Asrite(DeterministicWeightWindowOption):
        """
        ``Asrite`` represents INP asrite deterministic weight window data card
        options.

        ``Asrite`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asrite
        deterministic weight window data card option syntax element.

        Attributes:
            left_going_flux: Left-going flux at plane i.
        """

        def __init__(self, left_going_flux: int):
            """
            ``__init__`` initializes ``Asrite``.

            Parameters:
                left_going_flux: Left-going flux at plane i.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASRITE
            self.value = value
            self.left_going_flux = value

    class Asbott(DeterministicWeightWindowOption):
        """
        ``Asbott`` represents INP asbott deterministic weight window data card
        options.

        ``Asbott`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asbott
        deterministic weight window data card option syntax element.

        Attributes:
            top_going_flux: Top-going flux at plane j.
        """

        def __init__(self, top_going_flux: int):
            """
            ``__init__`` initializes ``Asbott``.

            Parameters:
                top_going_flux: Top-going flux at plane j.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASBOTT
            self.value = value
            self.top_going_flux = value

    class Astop(DeterministicWeightWindowOption):
        """
        ``Astop`` represents INP astop deterministic weight window data card
        options.

        ``Astop`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP astop deterministic weight window data card
        option syntax element.

        Attributes:
            bottom_going_flux: Bottom-going flux at plane j.
        """

        def __init__(self, bottom_going_flux: int):
            """
            ``__init__`` initializes ``Astop``.

            Parameters:
                bottom_going_flux: Bottom-going flux at plane j.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASTOP
            self.value = value
            self.bottom_going_flux = value

    class Asfrnt(DeterministicWeightWindowOption):
        """
        ``Asfrnt`` represents INP asfrnt deterministic weight window data card
        options.

        ``Asfrnt`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asfrnt
        deterministic weight window data card option syntax element.

        Attributes:
            back_going_flux: Back-going flux at plane k.
        """

        def __init__(self, back_going_flux: int):
            """
            ``__init__`` initializes ``Asfrnt``.

            Parameters:
                back_going_flux: Back-going flux at plane k.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASFRNT
            self.value = value
            self.back_going_flux = value

    class Asback(DeterministicWeightWindowOption):
        """
        ``Asback`` represents INP asback deterministic weight window data card
        options.

        ``Asback`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP asback
        deterministic weight window data card option syntax element.

        Attributes:
            front_going_flux: Front-going flux at plane k.
        """

        def __init__(self, front_going_flux: int):
            """
            ``__init__`` initializes ``Asback``.

            Parameters:
                front_going_flux: Front-going flux at plane k.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ASBACK
            self.value = value
            self.front_going_flux = value

    class Massed(DeterministicWeightWindowOption):
        """
        ``Massed`` represents INP massed deterministic weight window data card
        options.

        ``Massed`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP massed
        deterministic weight window data card option syntax element.

        Attributes:
            state: Mass edits setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Massed``.

            Parameters:
                state: Mass edits setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.MASSED
            self.value = value
            self.state = value

    class Pted(DeterministicWeightWindowOption):
        """
        ``Pted`` represents INP pted deterministic weight window data card
        options.

        ``Pted`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP pted deterministic weight window data card option
        syntax element.

        Attributes:
            state: Edits by fine mesh setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Pted``.

            Parameters:
                state: Edits by fine mesh setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.PTED
            self.value = value
            self.state = value

    class Zned(DeterministicWeightWindowOption):
        """
        ``Zned`` represents INP zned deterministic weight window data card
        options.

        ``Zned`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP zned deterministic weight window data card option
        syntax element.

        Attributes:
            state: Edits by zone setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Zned``.

            Parameters:
                state: Edits by zone setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.ZNED
            self.value = value
            self.state = value

    class Rzflux(DeterministicWeightWindowOption):
        """
        ``Rzflux`` represents INP rzflux deterministic weight window data card
        options.

        ``Rzflux`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP rzflux
        deterministic weight window data card option syntax element.

        Attributes:
            state: Write a-flux file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Rzflux``.

            Parameters:
                state: Write a-flux file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.RZFLUX
            self.value = value
            self.state = value

    class Rzmflux(DeterministicWeightWindowOption):
        """
        ``Rzmflux`` represents INP rzmflux deterministic weight window data
        card options.

        ``Rzmflux`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP rzmflux
        deterministic weight window data card option syntax element.

        Attributes:
            state: Write b-flux file setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Rzmflux``.

            Parameters:
                state: Write b-flux file setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.RXMFLUX
            self.value = value
            self.state = value

    class Edoutf(DeterministicWeightWindowOption):
        """
        ``Edoutf`` represents INP edoutf deterministic weight window data card
        options.

        ``Edoutf`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP edoutf
        deterministic weight window data card option syntax element.

        Attributes:
            ascii_output_control: ASCII output file control.
        """

        def __init__(self, ascii_output_control: int):
            """
            ``__init__`` initializes ``Edoutf``.

            Parameters:
                ascii_output_control: ASCII output file control.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or not (-3 <= value <= 3):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.EDOUTF
            self.value = value
            self.ascii_output_control = value

    class Byvlop(DeterministicWeightWindowOption):
        """
        ``Byvlop`` represents INP byvlop deterministic weight window data card
        options.

        ``Byvlop`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP byvlop
        deterministic weight window data card option syntax element.

        Attributes:
            state: Printed point reaction rates scaled by mesh volume setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Byvlop``.

            Parameters:
                state: Printed point reaction rates scaled by mesh volume setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.BYVLOP
            self.value = value
            self.state = value

    class Ajed(DeterministicWeightWindowOption):
        """
        ``Ajed`` represents INP ajed deterministic weight window data card
        options.

        ``Ajed`` inherits attributes from ``DeterministicWeightWindowOption``.
        It represents the INP ajed deterministic weight window data card option
        syntax element.

        Attributes:
            state: Regular and adjoint edit setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Ajed``.

            Parameters:
                state: Regular and adjoint edit setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.AJED
            self.value = value
            self.state = value

    class Fluxone(DeterministicWeightWindowOption):
        """
        ``Fluxone`` represents INP fluxone deterministic weight window data
        card options.

        ``Fluxone`` inherits attributes from
        ``DeterministicWeightWindowOption``. It represents the INP fluxone
        deterministic weight window data card option syntax element.

        Attributes:
            state: Flux override setting.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Fluxone``.

            Parameters:
                state: Flux override setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
            """

            if value is None or value not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

            self.keyword = DeterministicWeightWindowKeyword.FLUXONE
            self.value = value
            self.state = value

    def __init__(self, pairs: tuple[DeterministicWeightWindowOption]):
        """
        ``__init__`` initializes ``DeterministicWeightWindow``.

        Parameters:
            pairs: Tuple of key-value pairs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"dawwg"
        self.mnemonic = Datum.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW
        self.parameters = pairs

        self.pairs = pairs


class EmbeddedGeometry(Datum):
    """
    ``EmbeddedGeometry`` represents INP deterministic embedded geometry data
    cards.

    ``EmbeddedGeometry`` inherits attributes from ``Datum``. It represents the
    INP embedded geometry data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
        suffix: Data card suffix.
    """

    class EmbeddedGeometryOption:
        """
        ``EmbeddedGeometryOption`` represents INP embedded geometry specification
        data card options.

        ``EmbeddedGeometryOption`` implements INP embedded geometry specification
        data card options. Its attributes store keywords and values, and its
        methods provide entry and endpoints for working with INP embedded
        geometry specification data card options. It represents the generic INP
        embedded geometry specification data card option syntax element, so
        ``EmbeddedGeometry`` depends on ``EmbeddedGeometryOption`` as a genric
        data structre and superclass.

        Attributes:
            keyword: INP embedded geometry specification option keyword.
            value: INP embedded geometry specification option value.
        """

        class EmbeddedGeometryKeyword(StrEnum):
            """
            ``EmbeddedGeometryKeyword`` represents INP embedded geometry
            specification data card option keywords.

            ``EmbeddedGeometryKeyword`` implements INP embedded geometry
            specification data card option keywords as a Python inner class. It
            enumerates MCNP keywords and provides methods for casting strings
            to ``EmbeddedGeometryKeyword`` instances. It represents the INP
            embedded geometry specification data card option keyword syntax
            element, so ``EmbeddedGeometry`` and ``EmbeddedGeometryOption``
            depend on ``EmbeddedGeometryKeyword`` as an enum.
            """

            MATCELL = "matcell"
            MESHOGEO = "meshgeo"
            MGEOIN = "mgeoin"
            MEEOUT = "meeout"
            MEEIN = "meein"
            CALC_VOLS = "calc_vols"
            DEBUG = "debug"
            FILETYPE = "filetype"
            GMVFILE = "gmvfile"
            LENGTH = "length"
            MCNPUMFILE = "mcnpumfile"
            OVERLAP = "overlap"

            @staticmethod
            def from_mcnp(source: str):
                """
                ``from_mcnp`` generates ``EmbeddedGeometryKeyword``
                objects from INP.

                ``from_mcnp`` constructs instances of
                ``EmbeddedGeometryKeyword`` from INP source strings,
                so it operates as a class constructor method and INP parser
                helper function.

                Parameters:
                    source: INP for embedded geometry option keyword.

                Returns:
                    ``EmbeddedGeometryKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
                """

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in EmbeddedGeometryKeyword]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

                return EmbeddedGeometryKeyword(source)

        def __init__(self, keyword: EmbeddedGeometryKeyword, value: any):
            """
            ``__init__`` initializes ``EmbeddedGeometryOption``.

            Parameters:
                keyword: Embedded geometry data card option keyword.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

            match keyword:
                case EmbeddedGeometryKeyword.MATCELL:
                    obj = EmbeddedGeometryOption.Matcell(keyword, value)
                case EmbeddedGeometryKeyword.MESHOGEO:
                    obj = EmbeddedGeometryOption.Meshgeo(keyword, value)
                case EmbeddedGeometryKeyword.MGEOIN:
                    obj = EmbeddedGeometryOption.Mgeoin(keyword, value)
                case EmbeddedGeometryKeyword.MEEOUT:
                    obj = EmbeddedGeometryOption.Meeout(keyword, value)
                case EmbeddedGeometryKeyword.MEEIN:
                    obj = EmbeddedGeometryOption.Meein(keyword, value)
                case EmbeddedGeometryKeyword.CALC_VOLS:
                    obj = EmbeddedGeometryOption.CalcVols(keyword, value)
                case EmbeddedGeometryKeyword.DEBUG:
                    obj = EmbeddedGeometryOption.Debug(keyword, value)
                case EmbeddedGeometryKeyword.FILETYPE:
                    obj = EmbeddedGeometryOption.Filetype(keyword, value)
                case EmbeddedGeometryKeyword.GMVFILE:
                    obj = EmbeddedGeometryOption.Gmvfile(keyword, value)
                case EmbeddedGeometryKeyword.LENGTH:
                    obj = EmbeddedGeometryOption.Length(keyword, value)
                case EmbeddedGeometryKeyword.MCNPUMFILE:
                    obj = EmbeddedGeometryOption.Mcnpumfile(keyword, value)
                case EmbeddedGeometryKeyword.OVERLAP:
                    obj = EmbeddedGeometryOption.Overlap(keyword, value)

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``EmbeddedGeometryOption`` objects from INP.

            ``from_mcnp`` constructs instances of ``EmbeddedGeometryOption``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function. Although defined on the
            superclass, it returns ``EmbeddedGeometryOption`` subclasses.

            Parameters:
                source: INP for embedded geometry specification option.

            Returns:
                ``EmbeddedGeometryOption`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
                MCNPSyntaxError: TOOFEW_DATUM_EMBED, TOOLONG_DATUM_EMBED.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_EMBED))

            keyword = EmbeddedGeometryOption.EmbeddedGeometryKeyword.from_mcnp(tokens.popl())

            match keyword:
                case EmbeddedGeometryKeyword.MATCELL:
                    assert False, "Unimplemented"
                case EmbeddedGeometryKeyword.MESHOGEO | EmbeddedGeometryKeyword.MGEOIN | EmbeddedGeometryKeyword.MEEOUT | EmbeddedGeometryKeyword.MEEIN | EmbeddedGeometryKeyword.CALC_VOLS | EmbeddedGeometryKeyword.DEBUG | EmbeddedGeometryKeyword.FILETYPE | EmbeddedGeometryKeyword.GMVFILE | EmbeddedGeometryKeyword.MCNPUMFILE:
                    value = tokens.popl()
                case EmbeddedGeometryKeyword.LENGTH:
                    value = types.cast_fortran_real(tokens.popl())
                case EmbeddedGeometryKeyword.OVERLAP:
                    assert False, "Unimplemented"
                case _:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_EMBED)

    class Meshgeo(EmbeddedGeometryOption):
        """
        ``Meshgeo`` represents INP meshgeo embedded geometry specification
        options.

        ``Meshgeo`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP meshgeo embedded geometry data card option sytnax
        element.

        Attributes:
            form: Format specification of the embedded mesh input file.
        """

        def __init__(self, form: str):
            """
            ``__init__`` initializes ``Meshgeo``.

            Parameters:
                form: Format specification of the embedded mesh input file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if form is None or form not in {"lnk3dnt", "abaqus", "mcnpum"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MESHOGEO
            self.value = value
            self.form = value

    class Mgeoin(EmbeddedGeometryOption):
        """
        ``Mgeoin`` represents INP mgeoin embedded geometry specification
        options.

        ``Mgeoin`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP mgeoin embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the input file with mesh description.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Mgeoin``.

            Parameters:
                filename: Name of the input file with mesh description.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filename is None or not filename:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MGEOIN
            self.value = value
            self.filename = value

    class Meeout(EmbeddedGeometryOption):
        """
        ``Meeout`` represents INP meeout embedded geometry specification
        options.

        ``Meeout`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP meeout embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name assigned to EEOUT, the elemental edit output file.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Meeout``.

            Parameters:
                filename: Name assigned to EEOUT, the elemental edit output file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if value is None or not value:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MEEOUT
            self.value = value
            self.filename = value

    class Meein(EmbeddedGeometryOption):
        """
        ``Meein`` represents INP meein embedded geometry specification options.

        ``Meein`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP meein embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the EEOUT results file to read.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Meein``.

            Parameters:
                filename: Name of the EEOUT results file to read.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filename is None or not filename:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MEEIN
            self.value = filename
            self.filename = filename

    class CalcVols(EmbeddedGeometryOption):
        """
        ``CalcVols`` represents INP calc_vols embedded geometry specification
        options.

        ``CalcVols`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP calc_vols embedded geometry data card option sytnax
        element.

        Attributes:
            yes_no: Inferred geometry volume and masses calculation setting.
        """

        def __init__(self, yes_no: str):
            """
            ``__init__`` initializes ``CalcVols``.

            Parameters:
                yes_no: Inferred geometry volume and masses calculation setting.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if yes_no is None or yes_no not in {"yes", "no"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.CALC_VOLS
            self.value = yes_no
            self.yes_no = yes_no

    class Debug(EmbeddedGeometryOption):
        """
        ``Debug`` represents INP debug embedded geometry specification options.

        ``Debug`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP debug embedded geometry data card option sytnax
        element.

        Attributes:
            form: Write the embedded geometry parameters to the OUTP file.
        """

        def __init__(self, form: str):
            """
            ``__init__`` initializes ``Debug``.

            Parameters:
                form: Write the embedded geometry parameters to the OUTP file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if form is None or form not in {"echomesh"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.DEBUG
            self.value = form
            self.form = form

    class Filetype(EmbeddedGeometryOption):
        """
        ``Filetype`` represents INP filetype embedded geometry specification
        options.

        ``Filetype`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP filetype embedded geometry data card option sytnax
        element.

        Attributes:
            filetype: File type for the elemental edit output file.
        """

        def __init__(self, filetype: str):
            """
            ``__init__`` initializes ``Filetype``.

            Parameters:
                filetype: File type for the elemental edit output file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filetype is None or filetype not in {"ascii", "binary"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.FILETYPE
            self.value = filetype
            self.filetype = filetype

    class Gmvfile(EmbeddedGeometryOption):
        """
        ``Gmvfile`` represents INP gmvfile embedded geometry specification
        options.

        ``Gmvfile`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP gmvfile embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the GMV output file.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Gmvfile``.

            Parameters:
                filename: Name of the GMV output file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filename is None or not filename:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.GMVFILE
            self.value = filename
            self.filename = filename

    class Length(EmbeddedGeometryOption):
        """
        ``Length`` represents INP length embedded geometry specification
        options.

        ``Length`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP length embedded geometry data card option sytnax
        element.

        Attributes:
            factor: Multiplicative conversion factor to centimeters from mesh.
        """

        def __init__(self, factor: float):
            """
            ``__init__`` initializes ``Length``.

            Parameters:
                factor: Multiplicative conversion factor to centimeters from mesh.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if factor is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.LENGTH
            self.value = factor
            self.factor = factor

    class Mcnpumfile(EmbeddedGeometryOption):
        """
        ``Mcnpumfile `` represents INP mcnpumfile embedded geometry
        specification options.

        ``Mcnpumfile`` inherits attributes from ``EmbeddedGeometryOption``. It
        represents the INP mcnpumfile embedded geometry data card option sytnax
        element.

        Attributes:
            filename: Name of the MCNPUM output file.
        """

        def __init__(self, filename: str):
            """
            ``__init__`` initializes ``Mcnpumfile``.

            Parameters:
                filename: Name of the MCNPUM output file.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
            """

            if filename is None or not filename:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

            self.keyword = EmbeddedGeometryKeyword.MCNPUMFILE
            self.value = filename
            self.filename = filename

    def __init__(self, pairs: tuple[EmbeddedGeometryOption], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedGeometry``.

        Parameters:
            pairs: Tuple of key-value pairs.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.id: final[str] = f"embed{suffix}"
        self.mnemonic = Datum.DatumMnemonic.EMBEDDED_GEOMETRY
        self.parameters = pairs
        self.suffix: final[int] = suffix

        self.pairs = pairs


class EmbeddedControl(Datum):
    """
    ``EmbeddedControl`` represents INP embedded elemental edits control
    data cards.

    ``EmbeddedGeometry`` inherits attributes from ``Datum``. It represents the
    INP embedded elemental edits control data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
        suffix: Data card suffix.
        designator: Data card designator.
    """

    class EmbeddedControlOption:
        """
        ``EmbeddedControlOption`` represents INP embedded elemental
        edits control data card options.

        ``EmbeddedControlOption`` implements INP embedded elemental
        edits control data card options. Its attributes store keywords and
        values, and its methods provide entry and endpoints for working wit
        INP embedded elemental edits control data card options. It represents
        the generic INP embedded elemental edits control data card option
        syntax element, so ``EmbeddedControl`` depends on
        ``EmbeddedControlOption`` as a genric data structre and superclass.

        Attributes:
            keyword: INP embedded elemental control  option keyword.
            value: INP embedded elemental control option value.
        """

        class EmbeddedControlKeyword(StrEnum):
            """
            ``EmbeddedControlKeyword`` represents INP embedded elemental
            edits control data card option keywords.

            ``EmbeddedControlKeyword`` implements INP embedded elemental
            edits control data card option keywords as a Python inner class. It
            enumerates MCNP keywords and provides methods for casting strings
            to ``EmbeddedControlKeyword`` instances. It represents the
            INP embedded elemental edits control data card option keyword
            syntax element, so ``EmbeddedControl`` and
            ``EmbeddedControlOption`` depend on ``EmbeddedControlKeyword`` as
            an enum.
            """

            EMBED = "embed"
            ENERGY = "energy"
            TIME = "time"
            ATOM = "atom"
            FACTOR = "factor"
            LIST = "list"
            MAT = "mat"
            MTYPE = "mtype"

            @staticmethod
            def from_mcnp(source: str):
                """
                ``from_mcnp`` generates ``EmbeddedControlKeyword``
                objects from INP.

                ``from_mcnp`` constructs instances of ``EmbeddedControlKeyword``
                from INP source strings, so it operates as a class constructor
                method and INP parser helper function.

                Parameters:
                    source: INP for embedded edits control option keyword.

                Returns:
                    ``EmbeddedControlKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
                """

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in EmbeddedControlKeyword]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

                return EmbeddedControlKeyword(source)

        def __init__(self, keyword: EmbeddedControlKeyword, value: any):
            """
            ``__init__`` initializes ``EmbeddedControlOption``.

            Parameters:
                keyword: Embedded edits control data card option keyword.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

            match mnemoinc:
                case EmbeddedControlOption.EmbeddedControlKeyword.EMBED:
                    obj = EmbeddedControlOption.Embed(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.ENERGY:
                    obj = EmbeddedControlOption.Energy(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.TIME:
                    obj = EmbeddedControlOption.Time(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.ATOM:
                    obj = EmbeddedControlOption.Atom(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.FACTOR:
                    obj = EmbeddedControlOption.Factor(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.LIST:
                    assert False, "Unimplemented"
                case EmbeddedControlOption.EmbeddedControlKeyword.MAT:
                    obj = EmbeddedControlOption.Mat(keyword, value)
                case EmbeddedControlOption.EmbeddedControlKeyword.MTYPE:
                    obj = EmbeddedControlOption.Mtype(keyword, value)

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``EmbeddedControlOption`` objects from INP.

            ``from_mcnp`` constructs instances of ``EmbeddedControlOption``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function. Although defined on the
            superclass, it returns ``EmbeddedControlOption`` subclasses.

            Parameters:
                source: INP for embedded elemental edits control option.

            Returns:
                ``EmbeddedControlOption`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
                MCNPSyntaxError: TOOFEW_DATUM_EMBEE, TOOLONG_DATUM_EMBEE.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_EMBEE))

            # Processing Keyword
            keyword = EmbeddedGeometryOption.EmbeddedGeometryKeyword.from_mcnp(tokens.peekl())

            # Processing Values
            match keyword:
                case EmbeddedGeometryKeyword.EMBED:
                    value = types.cast_fortran_integer(tokens.popl())
                case EmbeddedGeometryKeyword.ENERGY | EmbeddedGeometryKeyword.TIME | EmbeddedGeometryKeyword.FRACTOR:
                    value = types.cast_fortran_real(tokens.popl())
                case EmbeddedGeometryKeyword.ATOM | EmbeddedGeometryKeyword.MTYPE:
                    value = tokens.popl()
                case _:
                    errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_EMBEE)

            return EmbeddedControlOption(keyword, value)

    class Embed(EmbeddedControlOption):
        """
        ``Embed`` represents INP Embed embedded elemental edits control data
        card options.

        ``Embed`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Embed embedded elemental edits control data card
        option syntax element.

        Attributes:
            number: Embedded mesh universe number.
        """

        def __init__(self, number: int):
            """
            ``__init__`` initializes ``Embed``.

            Parameters:
                number: Embedded mesh universe number.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if number is None or not (1 <= value <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.EMBED
            self.value = number
            self.number = number

    class Energy(EmbeddedControlOption):
        """
        ``Energy`` represents INP Energy embedded elemental edits control data
        card options.

        ``Energy`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Energy embedded elemental edits control data card
        option syntax element.

        Attributes:
            factor: Conversion factor for all energy outputs.
        """

        def __init__(self, factor: float):
            """
            ``__init__`` initializes ``Energy``.

            Parameters:
                factor: Conversion factor for all energy outputs.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if factor is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.ENERGY
            self.value = factor
            self.factor = factor

    class Time(EmbeddedControlOption):
        """
        ``Time`` represents INP Time embedded elemental edits control data card
        options.

        ``Time`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Time embedded elemental edits control data card
        option syntax element.

        Attributes:
            factor: Conversion factor for all time-related outputs.
        """

        def __init__(self, factor: float):
            """
            ``__init__`` initializes ``Time``.

            Parameters:
                factor: Conversion factor for all time-related outputs.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if factor is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.TIME
            self.value = factor
            self.factor = factor

    class Atom(EmbeddedControlOption):
        """
        ``Atom`` represents INP Atom embedded elemental edits control data card
        options.

        ``Atom`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Atom embedded elemental edits control data card
        option syntax element.

        Attributes:
            yes_no: Flag to multiply by atom density.
        """

        def __init__(self, yes_no: str):
            """
            ``__init__`` initializes ``Atom``.

            Parameters:
                yes_no: Flag to multiply by atom density.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if yes_no is None or yes_no not in {"yes", "no"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.ATOM
            self.value = yes_no
            self.yes_no = yes_no

    class Factor(EmbeddedControlOption):
        """
        ``Factor`` represents INP Factor embedded elemental edits control data
        card options.

        ``Factor`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Factor embedded elemental edits control data card
        option syntax element.

        Attributes:
            factor: Multiplicative constant.
        """

        def __init__(self, factor: float):
            """
            ``__init__`` initializes ``Factor``.

            Parameters:
                factor: Multiplicative constant.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if factor is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.FACTOR
            self.value = factor
            self.factor = factor

    class Mat(EmbeddedControlOption):
        """
        ``Mat`` represents INP Mat embedded elemental edits control data card
        options.

        ``Mat`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Mat embedded elemental edits control data card option
        syntax element.

        Attributes:
            number: Material number.
        """

        def __init__(self, number: int):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                number: Material number.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if number is None or not (0 <= number <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.MAT
            self.value = number
            self.number = number

    class Mtype(EmbeddedControlOption):
        """
        ``Mtype`` represents INP Mtype embedded elemental edits control data
        card options.

        ``Mtype`` inherits attributes from ``EmbeddedControlOption``. It
        represents the INP Mtype embedded elemental edits control data card
        option syntax element.

        Attributes:
            mtype: Multiplier type.
        """

        def __init__(self, mtype: str):
            """
            ``__init__`` initializes ``Mtype``.

            Parameters:
                mtype: Multiplier type.

            Raises:
                MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
            """

            if mtype is None or mtype not in {"flux", "isotopic", "population", "reaction", "source", "tracks"}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

            self.keyword = EmbeddedControlKeyword.MTYPE
            self.value = mtype
            self.mtype = mtype

    def __init__(self, pairs: tuple[EmbeddedControlOption], suffix: int, designator: tuple[types.Designator]):
        """
        ``__init__`` initializes ``EmbeddedControl``.

        Parameters:
            pairs: Tuple of key-value pairs.
            suffix: Data card suffix.
            designator: Data card designator.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        for particle in designator:
            if particle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        self.id: final[str] = f"embee{suffix}:{designator.to_mcnp()}"
        self.mnemonic = Datum.DatumMnemonic.EMBEDDED_CONTROL
        self.parameters = pairs
        self.suffix = suffix
        self.designator = designator

        self.pairs = pairs


class EmbeddedEnergyBoundaries(Datum):
    """
    ``EmbeddedEnergyBoundaries`` represents INP embedded elemental
    edits energy boundaries.

    ``EmbeddedEnergyBoundaries`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits energy boundaries data
    card syntax element.

    Attributes:
        energies: Tuple of energy lower bounds.
        suffix: Data card suffix.
    """

    def __init__(self, energies: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedEnergyBoundaries``.

        Parameters:
            energies: Tuple of energy lower bounds.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in energies:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.id: final[str] = f"embeb{suffix}"
        self.mnemonic = Datum.DatumMnemonic.EMBEDDED_ENERGY_BOUNDARIES
        self.parameters = energies
        self.suffix = suffix

        self.energies = energies


class EmbeddedEnergyMultipliers(Datum):
    """
    ``EmbeddedEnergyMultipliers`` represents INP embedded elemental
    edits energy multipliers.

    ``EmbeddedEnergyMultipliers`` inherits attributes from ``Datum``. It
    represents the INP embedded elemental edits energy multipliers data card
    syntax element.

    Attributes:
        multipliers: Tuple of energy multipliers.
    """

    def __init__(self, multipliers: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedEnergyMultipliers``.

        Parameters:
            multipliers: Tuple of energy multipliers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.id: final[str] = f"embem{suffix}"
        self.mnemonic = Datum.DatumMnemonic.EMBEDDED_ENERGY_MULTIPLIERS
        self.parameters = multipliers
        self.suffix = suffix

        self.multipliers = multipliers


class EmbeddedTimeBoundaries(Datum):
    """
    ``EmbeddedTimeBoundaries`` represents INP embedded elemental edits
    time boundaries.

    ``EmbeddedTimeBoundaries`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits time boundaries data
    card syntax element.

    Attributes:
        times: Tuple of time lower bounds.
    """

    def __init__(self, times: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedTimeBoundaries``.

        Parameters:
            times: Tuple of time lower bounds.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX
        """

        for parameter in times:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.id: final[str] = f"embtb{suffix}"
        self.mnemonic = Datum.DatumMnemonic.EMBEDDED_TIME_BOUNDARIES
        self.parameters = times
        self.suffix = suffix

        self.times = times


class EmbeddedTimeMultipliers(Datum):
    """
    ``EmbeddedTimeMultipliers`` represents INP embedded elemental
    edits time multipliers.

    ``EmbeddedTimeMultipliers`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits time multipliers data
    card syntax element.

    Attributes:
        multipliers: Tuple of time multipliers.
    """

    def __init__(self, multipliers: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedTimeMultipliers``.

        Parameters:
            multipliers: Tuple of time multipliers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.id: final[str] = f"embtm{suffix}"
        self.mnemonic = Datum.DatumMnemonic.EMBEDDED_TIME_MULTIPLIERS
        self.parameters = multipliers
        self.suffix = suffix

        self.multipliers = multipliers


class EmbeddedDoseBoundaries(Datum):
    """
    ``EmbeddedDoseBoundaries`` represents INP embedded elemental edits
    dose boundaries.

    ``EmbeddedDoseBoundaries`` inherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits dose boundaries data
    card syntax element.

    Attributes:
        doses: Tuple of dose lower bounds.
    """

    def __init__(self, doses: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedDoseBoundaries``.

        Parameters:
            doses: Tuple of dose lower bounds.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in doses:
            if parameter is None or not (parameter >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.id: final[str] = f"embde{suffix}"
        self.mnemonic = Datum.DatumMnemonic.EMBEDDED_DOSE_BOUNDARIES
        self.parameters = doses
        self.suffix = suffix

        self.doses = doses


class EmbeddedDoseMultipliers(Datum):
    """
    ``EmbeddedDoseMultipliers`` represents INP embedded elemental
    edits dose multipliers.

    ``EmbeddedDoseMultipliers`` iinherits attributes from ``Datum``. It
    represents the INP embedded embedded elemental edits dose multipliers data
    card syntax element.

    Attributes:
        doses: Tuple of dose multipliers.
    """

    def __init__(self, multipliers: tuple[float], suffix: int):
        """
        ``__init__`` initializes ``EmbeddedDoseMultipliers``.

        Parameters:
            multipliers: Tuple of dose multipliers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in multipliers:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"embdf{suffix}"
        self.mnemonic = Datum.DatumMnemonic.EMBEDDED_DOSE_MULTIPLIERS
        self.parameters = multipliers
        self.suffix = suffix

        self.multipliers = multipliers


class Material(Datum):
    """
    ``Material`` represents INP matieral specification data cards.

    ``Material`` inherits attributes from ``Datum``. It represents the INP
    material data card syntax element.

    Attributes:
        substances: Tuple of substance specification.
        paris: Tuple of key-value pairs.
    """

    class MaterialValue:
        """
        ``MaterialValue`` represents INP material data card
        entries.

        ``MaterialValue`` implements INP material specifications
        as a Python inner class. Its attributes store different mateiral
        entries, and its methods provide entry points and endpoints for working
        with material entries. ``Material`` depends on ``MateiralValue`` as a
        data type.

        Attributes:
            zaid: Material value Zaid specifier.
            fraction: Material value fraction.
        """

        def __init__(self, zaid: types.Zaid, fraction: float):
            """
            ``__init__`` initializes ``MaterialValue``.

            Parameters:
                zaid: Material value Zaid specifier.
                fraction: Material value fraction.

            Raises:
                MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            """

            self.zaid: types.Zaid = zaid
            self.fraction: float = fraction

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``MaterialValue`` objects from INP.

            ``from_mcnp`` constructs instances of ``MaterialValue`` from INP
            source strings, so it operates as a class constructor method and
            INP parser helper function.

            Parameters:
                source: INP for mateiral values.

            Returns:
                ``MaterialValue`` object.

            Raises:
                MCNPSyntaxError: TOOFEW_DATUM_MATERIAL, TOOLONG_DATUM_MATERIAL.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL))

            zaid = types.Zaid().cast_mcnp_zaid(tokens.popl())
            fraction = types.cast_fortran_real(tokens.popl())

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL)

            return MaterialValue(zaid, fraction)

        def to_mcnp(self):
            """
            ``to_mcnp`` generates INP from ``MaterialValue`` objects.

            ``to_mcnp`` creates INP source string from ``MaterialValue``
            objects, so it provides an MCNP endpoint.

            Returns:
                INP string for ``MaterialValue`` object.
            """

            return f"{self.zaid.to_mcnp()} {self.fraction}"

    class MaterialOption:
        """
        ``MaterialOption`` represents INP material data card
        options.

        ``MaterialOption`` implements INP material data card
        options. Its attributes store keywords and values, and its methods
        provide entry and endpoints for working with INP mateiral data card
        options. It represents the generic INP material data card option syntax
        element, so ``Material`` depends on ``MaterialOptino`` as a genric data
        structre and superclass.

        Attributes:
            keyword: INP material option keyword.
            value: INP material option value.
        """

        class MaterialKeyword(StrEnum):
            """
            ``MaterialKeyword`` represents INP material data card option
            keywords.

            ``MaterialKeyword`` implements INP material data card option
            keywords as a Python inner class. It enumerates MCNP keywords and
            provides methods for casting strings to ``MaterialKeyword``
            instances. It represents the INP material data card option keyword
            syntax element, so ``Material`` and ``MaterialOption`` depend on
            ``MaterialKeyword`` as an enum.
            """

            GAS = "gas"
            ESTEP = "estep"
            HSTEP = "hstep"
            NLIB = "nlib"
            PLIB = "plib"
            PNLIB = "pnlib"
            ELIB = "elib"
            HLIB = "hlib"
            ALIB = "alib"
            SLIB = "slib"
            TLIB = "tlib"
            DLIB = "dlib"
            COND = "cond"
            REFI = "refi"
            REFC = "refc"
            REFS = "refs"

            @staticmethod
            def from_mcnp(source: str):
                """
                ``from_mcnp`` generates ``MaterialKeyword`` objects from INP.

                ``from_mcnp`` constructs instances of ``MaterialKeyword`` from
                INP source strings, so it operates as a class constructor
                method and INP parser helper function.

                Parameters:
                    source: INP for material option keyword.

                Returns:
                    ``MaterialKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_MATERIAL_KEYWORD.
                """

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in Material.MaterialOption.MaterialKeyword]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD)

                return Material.MaterialOption.MaterialKeyword(source)

        def __init__(self, keyword: MaterialKeyword, value: any):
            """
            ``__init__`` initializes ``MaterialOption``.

            Parameters:
                keyword: Material specification data card option keyword.
                value: Material specification data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MATERIAL_KEYWORD)

            match keyword:
                case Material.MaterialOption.MaterialKeyword.GAS:
                    obj = Material.Gas(value)
                case Material.MaterialOption.MaterialKeyword.ESTEP:
                    obj = Material.Estep(value)
                case Material.MaterialOption.MaterialKeyword.HSTEP:
                    obj = Material.Hstep(value)
                case Material.MaterialOption.MaterialKeyword.NLIB:
                    obj = Material.Nlib(value)
                case Material.MaterialOption.MaterialKeyword.PLIB:
                    obj = Material.Plib(value)
                case Material.MaterialOption.MaterialKeyword.PNLIB:
                    obj = Material.Pnlib(value)
                case Material.MaterialOption.MaterialKeyword.ELIB:
                    obj = Material.Elib(value)
                case Material.MaterialOption.MaterialKeyword.HLIB:
                    obj = Material.Hlib(value)
                case Material.MaterialOption.MaterialKeyword.ALIB:
                    obj = Material.Alib(value)
                case Material.MaterialOption.MaterialKeyword.SLIB:
                    obj = Material.Slib(value)
                case Material.MaterialOption.MaterialKeyword.TLIB:
                    obj = Material.Tlib(value)
                case Material.MaterialOption.MaterialKeyword.DLIB:
                    obj = Material.Dlib(value)
                case Material.MaterialOption.MaterialKeyword.COND:
                    obj = Material.Cond(value)
                case Material.MaterialOption.MaterialKeyword.REFI:
                    obj = Material.Refi(value)
                case Material.MaterialOption.MaterialKeyword.REFC:
                    assert False, "Unimplemented"
                case Material.MaterialOption.MaterialKeyword.REFS:
                    assert False, "Unimplemented"

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``MaterialOption`` objects from INP.

            ``from_mcnp`` constructs instances of ``MaterialOption`` from INP
            source strings, so it operates as a class constructor method and
            INP parser helper function. Although defined on the superclass, it
            returns ``MaterialOption`` subclasses.

            Parameters:
                source: INP for material option.

            Returns:
                ``MaterialOption`` object.

            Raises:
                MCNPSyntaxError: TOOFEW_DATUM_MATERIAL, TOOLONG_DATUM_MATERIAL.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL))

            # Processing Keyword
            keyword = Material.MaterialOption.MaterialKeyword.from_mcnp(tokens.popl())

            # Processing Values
            match keyword:
                case Material.MaterialOption.MaterialKeyword.GAS:
                    value = types.cast_fortran_integer(tokens.popl())

                case Material.MaterialOption.MaterialKeyword.ESTEP | Material.MaterialOption.MaterialKeyword.HSTEP | Material.MaterialOption.MaterialKeyword.COND | Material.MaterialOption.MaterialKeyword.REFI:
                    value = types.cast_fortran_real(tokens.popl())

                case Material.MaterialOption.MaterialKeyword.NLIB | Material.MaterialOption.MaterialKeyword.PLIB | Material.MaterialOption.MaterialKeyword.PNLIB | Material.MaterialOption.MaterialKeyword.ELIB | Material.MaterialOption.MaterialKeyword.HLIB | Material.MaterialOption.MaterialKeyword.ALIB | Material.MaterialOption.MaterialKeyword.SLIB | Material.MaterialOption.MaterialKeyword.TLIB | Material.MaterialOption.MaterialKeyword.DLIB:
                    value = tokens.popl()

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_MATERIAL)

            return Material.MaterialOption(keyword, value)

        def to_mcnp(self):
            """
            ``to_mcnp`` generates INP from ``MaterialOption`` objects.

            ``to_mcnp`` creates INP source string from ``MaterialOption``
            objects, so it provides an MCNP endpoint.

            Returns:
                INP string for ``MaterialOption`` object.
            """

            return f"{Material.MaterialOption.MaterialKeyword(self.keyword)}={self.value}"

    class Gas(MaterialOption):
        """
        ``Gas`` represents INP Gas material data card options.

        ``Gas`` inherits attributes from ``MaterialOption``. It represents the
        INP Gas material data card option syntax element.

        Attributes:
            state: Flag for density-effect corection.
        """

        def __init__(self, state: int):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                state: Flag for density-effect corection.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if state is None or state not in {0, 1}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.GAS
            self.value = state
            self.state = state

    class Estep(MaterialOption):
        """
        ``Estep`` represents INP Estep material data card options.

        ``Estep`` inherits attributes from ``MaterialOption``. It represents the
        INP Estep material data card option syntax element.

        Attributes:
            step: Energy step increment.
        """

        def __init__(self, step: float):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                step: Energy step increment.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if step is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.ESTEP
            self.value = step
            self.step = step

    class Hstep(MaterialOption):
        """
        ``Hstep`` represents INP Hstep material data card options.

        ``Hstep`` inherits attributes from ``MaterialOption``. It represents the
        INP Hstep material data card option syntax element.

        Attributes:
            step: Energy step increment.
        """

        def __init__(self, step: float):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                step: Energy step increment.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if step is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.HSTEP
            self.value = step
            self.step = step

    class Nlib(MaterialOption):
        """
        ``Nlib`` represents INP Nlib material data card options.

        ``Nlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Nlib material data card option syntax element.

        Attributes:
            step: Energy step increment.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                step: Energy step increment.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if step is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.NLIB
            self.value = step
            self.abx = step

    class Plib(MaterialOption):
        """
        ``Plib`` represents INP Plib material data card options.

        ``Plib`` inherits attributes from ``MaterialOption``. It represents the
        INP Plib material data card option syntax element.

        Attributes:
            abx: Table identifier default.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                abx: Table identifier default.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if abx is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.PLIB
            self.value = abx
            self.abx = abx

    class Pnlib(MaterialOption):
        """
        ``Pnlib`` represents INP Pnlib material data card options.

        ``Pnlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Pnlib material data card option syntax element.

        Attributes:
            abx: Table identifier default.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                value: Material data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if abx is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.PNLIB
            self.value = abx
            self.abx = abx

    class Elib(MaterialOption):
        """
        ``Elib`` represents INP Elib material data card options.

        ``Elib`` inherits attributes from ``MaterialOption``. It represents the
        INP Elib material data card option syntax element.

        Attributes:
            abx: Table identifier default.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                abx: Table identifier default.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if abx is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.ELIB
            self.value = abx
            self.abx = abx

    class Hlib(MaterialOption):
        """
        ``Hlib`` represents INP Hlib material data card options.

        ``Hlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Hlib material data card option syntax element.

        Attributes:
            abx: Table identifier default.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                abx: Table identifier default.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if abx is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.HLIB
            self.value = abx
            self.abx = abx

    class Alib(MaterialOption):
        """
        ``Alib`` represents INP Alib material data card options.

        ``Alib`` inherits attributes from ``MaterialOption``. It represents the
        INP Alib material data card option syntax element.

        Attributes:
            abx: Table identifier default.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                abx: Table identifier default.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if abx is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.ALIB
            self.value = abx
            self.abx = abx

    class Slib(MaterialOption):
        """
        ``Slib`` represents INP Slib material data card options.

        ``Slib`` inherits attributes from ``MaterialOption``. It represents the
        INP Slib material data card option syntax element.

        Attributes:
            abx: Table identifier default.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                abx: Table identifier default.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if abx is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.SLIB
            self.value = abx
            self.abx = abx

    class Tlib(MaterialOption):
        """
        ``Tlib`` represents INP Tlib material data card options.

        ``Tlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Tlib material data card option syntax element.

        Attributes:
            abx: Table identifier default.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                abx: Table identifier default.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if abx is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.TLIB
            self.value = abx
            self.abx = abx

    class Dlib(MaterialOption):
        """
        ``Dlib`` represents INP Dlib material data card options.

        ``Dlib`` inherits attributes from ``MaterialOption``. It represents the
        INP Dlib material data card option syntax element.

        Attributes:
            abx: Table identifier default.
        """

        def __init__(self, abx: str):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                abx: Table identifier default.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if abx is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.DLIB
            self.value = abx
            self.abx = abx

    class Cond(MaterialOption):
        """
        ``Cond`` represents INP Cond material data card options.

        ``Cond`` inherits attributes from ``MaterialOption``. It represents the
        INP Cond material data card option syntax element.

        Attributes:
            conducation_state: Conduction state of material for ELO3.
        """

        def __init__(self, conducation_state: float):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                conducation_state: Conduction state of material for ELO3.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if conducation_state is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.COND
            self.value = conducation_state
            self.conducation_state = conducation_state

    class Refi(MaterialOption):
        """
        ``Refi`` represents INP Refi material data card options.

        ``Refi`` inherits attributes from ``MaterialOption``. It represents the
        INP Refi material data card option syntax element.

        Attributes:
            index: Constant refractive index.
        """

        def __init__(self, index: float):
            """
            ``__init__`` initializes ``Mat``.

            Parameters:
                index: Constant refractive index.

            Raises:
                MCNPSemanticError: INVALID_DATUM_MATERIAL_VALUE.
            """

            if value is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_MATERIAL_VALUE)

            self.keyword = Material.MaterialOption.MaterialKeyword.REFI
            self.value = value
            self.index = value

    def __init__(self, substances: tuple[types.Zaid], pairs: tuple[MaterialOption], suffix: int):
        """
        ``__init__`` initializes ``Material``.

        Parameters:
            substances: Tuple of substance specification.
            pairs: Tuple of key-value pairs.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in substances:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.paris = pairs
        self.substances = substances

        self.id: final[str] = f"m{suffix}"
        self.mnemonic = Datum.DatumMnemonic.MATERIAL
        self.parameters = tuple(list(substances) + list(pairs))
        self.suffix = suffix


class MaterialNeutronScattering(Datum):
    """
    ``MaterialNeutronScattering`` represents INP thermal neutron scattering
    data cards.

    ``MaterialNeutronScattering`` inherits attributes from ``Datum``. It
    represents the INP thermal neturon scattering data card syntax element.

    Attributes:
        identifiers: Tuple of material identifiers.
        suffix: Data card suffix.
    """

    def __init__(self, identifiers: tuple[str], suffix: int):
        """
        ``__init__`` initializes ``MaterialNeutronScattering``.

        Parameters:
            identifiers: Tuple of material identifiers.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in identifiers:
            if parameter is None or not parmeter:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        self.id: final[str] = f"mt{suffix}"
        self.mnemonic = Datum.DatumMnemonic.THERMAL_NETURON_SCATTERING
        self.parameters = identifiers
        self.suffix = suffix


class MaterialNuclideSubstitution(Datum):
    """
    ``MaterialNuclideSubstitution`` represents INP material nuclide
    substitution data cards.

    ``MaterialNuclideSubstitution`` inherits attributes from ``Datum``. It
    represents the INP material nuclide substitution data card syntax element.

    Attributes:
        zaids: Tuple of ZAID alias.
        suffix: Data card suffix.
        designator: Data card designator.
    """

    def __init__(self, zaids: tuple[types.Zaid], suffix: int, designator: tuple[types.Designator]):
        """
        ``__init__`` initializes ``MaterialNuclideSubstitution``.

        Parameters:
            zaids: Tuple of ZAID alias.
            suffix: Data card suffix.
            designator: Data card designator.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        for particle in designator:
            if particle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        self.id: final[str] = f"mx{suffix}:{designator.to_mcnp()}"
        self.mnemonic = Datum.DatumMnemonic.MATERIAL_NUCLIDE_SUBSTITUTION
        self.parameters = zaids
        self.suffix = suffix
        self.designator = designator

        self.zaids = zaids


class OnTheFlyBroadening(Datum):
    """
    ``OnTheFlyBroadening`` represents INP on-the-fly broadening data cards.

    ``OnTheFlyBroadening`` inherits attributes from ``Datum``. It represents
    the INP on-the-fly boradening data card syntax element.

    Attributes:
        zaids: Tuple of ZAID alias.
    """

    def __init__(self, zaids: tuple[types.Zaid]):
        """
        ``__init__`` initializes ``OnTheFlyBroadening``.

        Parameters:
            zaids: Tuple of ZAID alias.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in zaids:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"otfdb"
        self.mnemonic = Datum.DatumMnemonic.ONTHEFLY_BROADENING
        self.parameters = zaids

        self.zaids = zaids


class TotalFission(Datum):
    """
    ``OnTheFlyBroadening`` represents INP total fission data cards.

    ``OnTheFlyBroadening`` inherits attributes from ``Datum``. It represents
    the INP on-the-fly boradening data card syntax element.

    Attributes:
        has_no: No volume calculation option.
    """

    def __init__(self, has_no: bool):
        """
        ``__init__`` initializes ``TotalFission``.

        Parameters:
           has_no: No volume calculation option.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if has_no is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"totnu"
        self.mnemonic = Datum.DatumMnemonic.TOTAL_FISSION
        self.parameters = (has_no,)

        self.states = has_no


class FissionTurnoff(Datum):
    """
    ``FissionTurnoff`` represents INP fission turnoff data cards.

    ``FissionTurnoff`` inherits attributes from ``Datum``. It represents
    the INP fission turnoff data card syntax element.

    Attributes:
        states: Tuple of fission turnoff settings.
    """

    def __init__(self, states: int):
        """
        ``__init__`` initializes ``FissionTurnoff``.

        Parameters:
            states: Tuple of fission turnoff settings.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in states:
            if parameter is None or parameter not in {0, 1, 2}:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"nonu"
        self.mnemonic = Datum.DatumMnemonic.FISSION_TURNOFF
        self.parameters = states

        self.states = states


class AtomicWeight(Datum):
    """
    ``AtomicWeight`` represents INP atomic weight data cards.

    ``AtomicWeight`` inherits attributes from ``Datum``. It represents
    the INP atomic weight data card syntax element.

    Attributes:
        weight_ratios: Tuple of weight ratios.
    """

    class AtomicWeightValue:
        """
        ``AtomicWeightValue`` represents INP atomic weight data card entries.

        ``AtomicWeightValue`` implements INP material specifications as a
        Python inner class. Its attributes store different mateiral entries,
        and its methods provide entry points and endpoints for working with
        atomic weight entries. ``AtomicWeight`` depends on
        ``AtomicWeightValue`` as a data type.

        Attributes:
            zaid: Atomic weight value Zaid specifier.
            ratio: Atomic weight value weight ratio.
        """

        def __init__(self, zaid: types.Zaid, ratio: float):
            """
            ``__init__`` initializes ``AtomicWeightValue``.
            """

            if zaid is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            if ratio is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            self.zaid: types.Zaid = zaid
            self.ratio: float = ratio

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``AtomicWeightValue`` objects from INP.

            ``from_mcnp`` constructs instances of ``AtomicWeightValue`` from
            INP source strings, so it operates as a class constructor method
            and INP parser helper function.

            Parameters:
                source: INP for atomic weight values.

            Returns:
                ``AtomicWeightValue`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_PARAMETERS.
                MCNPSyntaxError: TOOFEW_DATUM_WEIGHT, TOOLONG_DATUM_WEIGHT.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_WEIGHT))

            zaid = types.Zaid().cast_mcnp_zaid(tokens.popl())
            ratio = types.cast_fortran_real(tokens.popl())

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_WEIGHT)

            return AtomicWeightValue(zaid, ratio)

    def __init__(self, weight_ratios: tuple[AtomicWeightValue]):
        """
        ``__init__`` initializes ``AtomicWeight``.

        Parameters:
            weight_ratios: Tuple of weight ratios.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in weights:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"awtab"
        self.mnemonic = Datum.DatumMnemonic.ATOMIC_WEIGHT
        self.parameters = weight_ratios

        self.weight_ratios = weight_ratios


class CrossSectionFile(Datum):
    """
    ``CrossSectionFile`` represents INP cross-section file data cards.

    ``CrossSectionFile`` inherits attributes from ``Datum``. It represents the
    INP cross-section file data card syntax element.

    Attributes:
        weight_ratios: Tuple of weight ratios.
        suffix: Data card suffix.
    """

    class CrossSectionFileValue:
        """
        ``CrossSectionFileValue`` represents INP cross-section file data card
        entries.

        ``CrossSectionFileValue`` implements INP material specifications as a
        Python inner class. Its attributes store different mateiral entries,
        and its methods provide entry points and endpoints for working with
        cross-section file entries. ``CrossSectionFile`` depends on
        ``CrossSectionFileValue`` as a data type.

        Attributes:
            weight_ratios: Tuple of weight ratios.
        """

        def __init__(self, zaid: types.Zaid, ratio: float):
            """
            ``__init__`` initializes ``CrossSectionFile``.
            """

            if zaid is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            if ratio is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

            self.zaid: types.Zaid = zaid
            self.ratio: float = ratio

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``CrossSectionFileValue`` objects from INP.

            ``from_mcnp`` constructs instances of ``CrossSectionFileValue``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function.

            Parameters:
                source: INP for cross-section file values.

            Returns:
                ``CrossSectionFileValue`` object.

            Raises:
                MCNPSemanticError: INVALID_DATUM_PARAMETERS.
                MCNPSyntaxError: TOOFEW_DATUM_WEIGHT, TOOLONG_DATUM_WEIGHT.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_WEIGHT))

            zaid = types.Zaid().cast_mcnp_zaid(tokens.popl())
            ratio = types.cast_fortran_real(tokens.popl())

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_WEIGHT)

            return AtomicWeightValue(zaid, ratio)

    def __init__(self, weight_ratios: tuple[CrossSectionFileValue], suffix: int):
        """
        ``__init__`` initializes ``CrossSectionFile``.

        Parameters:
            weight_ratios: Tuple of weight ratios.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if weight_ratios is None or not weight_ratios:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for weight_ratio in weight_ratios:
            if weight_ratio is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"xs{suffix}"
        self.mnemonic = Datum.DatumMnemonic.CROSS_SECTION_FILE
        self.parameters = weight_ratios
        self.suffix = suffix

        self.weight_ratios = weight_ratios


class Void(Datum):
    """
    ``Void`` represents INP material void data cards.

    ``Void`` inherits attributes from ``Datum``. It represents the INP material
    void data card syntax element.

    Attributes:
        numbers: Tuple of cell numbers.
    """

    def __init__(self, numbers: tuple[int]):
        """
        ``__init__`` initializes ``Void``.

        Parameters:
            numbers: Tuple of cell numbers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in numbers:
            if parameter is None or not (1 <= parameter <= 99_999_999):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"void"
        self.mnemonic = Datum.DatumMnemonic.VOID
        self.parameters = numbers

        self.numbers = numbers


class MultigroupAdjointTransport(Datum):
    """
    ``MultigroupAdjointTransport`` represents INP multigroup adjoint transport
    option data cards.

    ``MultigroupAdjointTransport`` inherits attributes from ``Datum``. It
    represents the INP multigroup adjoint transport option data card syntax
    element.

    Attributes:
        mcal: Problem kind setting.
        igm: Total number of energy groups for all particles.
        iplt: Indicator of how weight windows are to be used.
        isb: Contols adjoint biasing for adjoint problems.
        icw: Nmae of the refreence cell for generated weight windows.
        fnw: Normalization value for gerneated weight windows.
        rim: Compression limit for gerneted weight windows.
    """

    def __init__(self, mcal: str, igm: int, iplt: int, isb: int, icw: int, fnw: int, rim: int):
        """
        ``__init__`` initializes ``MultigroupAdjointTransport``.

        Parameters:
            mcal: Problem kind setting.
            igm: Total number of energy groups for all particles.
            iplt: Indicator of how weight windows are to be used.
            isb: Contols adjoint biasing for adjoint problems.
            icw: Nmae of the refreence cell for generated weight windows.
            fnw: Normalization value for gerneated weight windows.
            rim: Compression limit for gerneted weight windows.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if mcal is None or not (mcal == "f" or mcal == "a"):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if igm is None or not (igm != 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if iplt is None or not (iplt in {0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if isb is None or not (isb in {0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if icw is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if fnw is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if rim is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"mgopt"
        self.mnemonic = Datum.DatumMnemonic.MULTIGROUP_ADJOINT_TRANSPORT
        self.parameters = (mcal, igm, iplt, isb, icw, fnw, rim)

        self.mcal = mcal
        self.igm = igm
        self.iplt = iplt
        self.isb = isb
        self.icw = icw
        self.fnw = fnw
        self.rim = rim


class DiscreteReactionCrossSection(Datum):
    """
    ``DiscreteReactionCrossSection`` represents INP discrete-reaction cross
    section data cards.

    ``DiscreteReactionCrossSection`` inherits attributes from ``Datum``. It
    represents the INP discrete-reaction cross section data card syntax
    element.

    Attributes:
        zaids: Tuple of ZAID specifiers.
    """

    def __init__(self, zaids: tuple[types.Zaid]):
        """
        ``__init__`` initializes ``DiscreteReactionCrossSection``.

        Parameters:
            zaids: Tuple of ZAID specifiers.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for zaid in zaids:
            if zaid is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"drxs"
        self.mnemonic = Datum.DatumMnemonic.DISCRETE_REACTIONC_CROSS_SECTION
        self.parameters = zaids

        self.zaids = zaids


class ProblemType(Datum):
    """
    ``ProblemType`` represents INP problem type data cards.

    ``ProblemType`` inherits attributes from ``Datum``. It represents the INP
    problem type data card syntax element.

    Attributes:
        particles: Tuple of particle designators.
    """

    def __init__(self, particles: tuple[types.Designator]):
        """
        ``__init__`` initializes ``DiscreteReactionCrossSection``.

        Parameters:
            particles: Tuple of particle designators.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if particles is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for particle in particles:
            if particle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"mode"
        self.mnemonic = Datum.DatumMnemonic.PROBLEM_TYPE
        self.parameters = particles

        self.particles = particles


class ParticlePhysicsOptions(Datum):
    """
    ``ParticlePhysicsOptions`` represents INP particle physics option data
    cards.

    ``ParticlePhysicsOptions`` inherits attributes from ``Datum``. It
    represents the INP problem type data card syntax element.

    Attributes
        designator: Particle designator.
    """

    def __init__(self, designator: types.Designator, parameters: tuple[any]):
        """
        ``__init__`` initializes ``ParticlePhysicsOptions``.

        Parameters:
            designator: Particle designator.
            parameters: Particle physics option data card parameters.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR.
        """

        if designator is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        if parameters is None or not parameters:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        match designator:
            case types.Designator.NEUTRON:
                obj = ParticlePhysicsOptionsNeutron(*parameters)
            case types.Designator.PHOTON:
                obj = ParticlePhysicsOptionsPhoton(*parameters)
            case types.Designator.ELECTRON:
                obj = ParticlePhysicsOptionsElectron(*parameters)
            case types.Designator.PROTON:
                obj = ParticlePhysicsOptionsPhoton(*parameters)
            case _:
                obj = ParticlePhysicsOptionsOther(designator, *parameters)

        self.__dict__ = obj.__dict__
        self.__class__ = obj.__class__


class ParticlePhysicsOptionsNeutron(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsNeutron`` represents INP particle physics
    option data cards with the neutron designator.

    ``ParticlePhysicsOptionsNeutron`` inherits attributes from ``Datum``.
    It represents the INP problem type data card with neutron designator
    syntax element.

    Attributes:
        emax: Upper limit for neutron energy and memory control.
        emcnf: Analog energy limit.
        iunr: Unresolved resonance range control.
        colif: Light-ion and heavy-ion recoil and NCIA control.
        cutn: Table-based physics cutoff and memory reduction control.
        ngam: Secondary photon production control.
        i_int_model: Treatment of nuclear reactions control.
        i_els_model: Treatment of nuclear elastic scattering control.
    """

    def __init__(
        self, emax: float, emcnf: float, iunr: int, colif: float, cutn: float, ngam: int, i_int_model: int, i_els_model: int
    ):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsNeutron``.

        Parameters:
            emax: Upper limit for neutron energy and memory control.
            emcnf: Analog energy limit.
            iunr: Unresolved resonance range control.
            colif: Light-ion and heavy-ion recoil and NCIA control.
            cutn: Table-based physics cutoff and memory reduction control.
            ngam: Secondary photon production control.
            i_int_model: Treatment of nuclear reactions control.
            i_els_model: Treatment of nuclear elastic scattering control.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if emax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if emcnf is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if iunr is None or not (iurn in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if colif is None or not (
            coilf in {0, 3, 5} or 0.001 < coilf < 1.001 or 1.001 < coilf < 2.001 or 3.001 < coilf < 4.001
        ):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if cutn is None or not (cutn >= 0 or cutn == -1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ngam is None or not (ngam in {0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_int_model is None or not (i_int_model in {-1, 0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_els_model is None or not (i_els_model in {-1, 0}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"phys:n"
        self.mnemonic = Datum.DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (emax, emcnf, iunr, colif, cutn, ngam, i_int_model, i_els_model)
        self.designator = types.Designator.NEUTRON

        self.emax = emax
        self.emcnf = emcnf
        self.iunr = iunr
        self.colif = colif
        self.cutn = cutn
        self.ngam = ngam
        self.i_int_model = i_int_model
        self.i_els_model = i_els_model


class ParticlePhysicsOptionsPhoton(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsPhoton`` represents INP particle physics option
    data cards with the photon designator.

    ``ParticlePhysicsOptionsPhoton`` inherits attributes from ``Datum``. It
    represents the INP problem type data card with photon designator
    syntax element.

    Attributes:
        emcpf: Energy limit for photon physics treatment.
        ides: Generation of electrions by photons controls.
        nocoh: Coherent Thomson scattering controls.
        ispn: Photonuclear particle production controls.
        nodop: Photon Doppler energy broadening controls.
        fism: Slection of photofission method controls.
    """

    def __init__(self, emcpf: float, ides: int, nocoh: int, ispn: int, nodop: int, fism: int):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsPhoton``.

        Parameters:
            emcpf: Energy limit for photon physics treatment.
            ides: Generation of electrions by photons controls.
            nocoh: Coherent Thomson scattering controls.
            ispn: Photonuclear particle production controls.
            nodop: Photon Doppler energy broadening controls.
            fism: Slection of photofission method controls.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if emcpf is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ides is None or not (ides in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nocoh is None or not (nocoh in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ispn is None or not (ispn in {-1, 0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nodop is None or not (nodop in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if fism is None or not (fism in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"phys:p"
        self.mnemonic = Datum.DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (emcpf, ides, nocoh, ispn, nodop, fism)
        self.designator = types.Designator.PHOTON

        self.emcpf = emcpf
        self.ides = ides
        self.nocoh = nocoh
        self.ispn = ispn
        self.nodop = nodop
        self.fism = fism


class ParticlePhysicsOptionsElectron(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsElectron`` represents INP particle physics
    option data cards with the electron designator.

    ``ParticlePhysicsOptionsElectron`` inherits attributes from ``Datum``.
    It represents the INP problem type data card with electron designator
    syntax element.

    Attributes:
        emax: Limit for electron energy.
        ides: Production of electrons by photons controls.
        iphot: Production of photons by electrons controls.
        ibad: Bremsstrahlung angular distribtuion method controls.
        istrg: Electron continuous-energy slowing down treatment controls.
        bnum: Production of bremsstrahlung photons controls.
        xnum: Smapling of electron-induced x-rays controls.
        rnok: Creation of knock-on electrons controls.
        enum: Generation of photon-induced electrons controls.
        numb: Bremsstrahlung production on each electron sub step.
        i_mcs_model: Choice of Coulomb scattering model controls.
        efac: Stopping power energy spacing controls.
        electron_method_boundary: Start of single-event transport controls.
        ckvnum: Cerenkov photon emission controls.
    """

    def __init__(
        self,
        emax: float,
        ides: int,
        ibad: int,
        istrg: int,
        bnum: float,
        xnum: float,
        rnok: float,
        enum: float,
        numb: float,
        i_mcs_model: int,
        efac: float,
        electron_method_boundary: float,
        ckvnum: float,
    ):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsElectron``.

        Parameters:
            emax: Limit for electron energy.
            ides: Production of electrons by photons controls.
            iphot: Production of photons by electrons controls.
            ibad: Bremsstrahlung angular distribtuion method controls.
            istrg: Electron continuous-energy slowing down treatment controls.
            bnum: Production of bremsstrahlung photons controls.
            xnum: Smapling of electron-induced x-rays controls.
            rnok: Creation of knock-on electrons controls.
            enum: Generation of photon-induced electrons controls.
            numb: Bremsstrahlung production on each electron sub step.
            i_mcs_model: Choice of Coulomb scattering model controls.
            efac: Stopping power energy spacing controls.
            electron_method_boundary: Start of single-event transport controls.
            ckvnum: Cerenkov photon emission controls.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if emax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ides is None or not (ides in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ibad is None or not (ibad in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if istrg is None or not (istrg in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if bnum is None or not (bnum >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if xnum is None or not (xnum >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if rnok is None or not (rnok >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if enum is None or not (enum >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if numb is None or not (numb >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_mcs_model is None or not (i_mcs_model in {0, -1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if electron_method_boundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"phys:e"
        self.mnemonic = Datum.DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (
            emax,
            ides,
            iphot,
            ibad,
            istrg,
            bnum,
            xnum,
            rnok,
            enum,
            numb,
            i_mcs_model,
            efac,
            electron_method_boundary,
            ckvnum,
        )
        self.designator = types.Designator.ELECTRON

        self.emax = emax
        self.ides = ides
        self.iphot = iphot
        self.ibad = ibad
        self.istrg = istrg
        self.bnum = bnum
        self.xnum = xnum
        self.rnok = rnok
        self.enum = enum
        self.numb = numb
        self.i_mcs_model = i_mcs_model
        self.efac = efac
        self.electron_method_boundary = electron_method_boundary
        self.ckvnum = ckvnum


class ParticlePhysicsOptionsProton(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsProton`` represents INP particle physics option
    data cards with the proton designator.

    ``ParticlePhysicsOptionsProton`` inherits attributes from ``Datum``.
    It represents the INP problem type data card with proton designator syntax
    element.

    Attributes:
        emax: Proton energy limit.
        ean: Analog energy limit.
        tabl: Table-based physics cutoff.
        istrg: Charged-particle straggling controls.
        recl: Light ion recoil control.
        i_mcs_model: Choice of Coulomb scattering model controls.
        i_int_model: Treamtment of nuclear interactions controls.
        i_els_model: Treatment of nuclear elastic scattering.
        efac: Stopping power energy spacing controls.
        ckvnum: Cerenkov photon emission controls.
        drp: Lower energy delta-ray cutoff.
    """

    def __init__(
        self,
        emax: float,
        ean: float,
        tabl: float,
        istrg: int,
        recl: float,
        i_mcs_model: int,
        i_int_model: int,
        i_els_model: int,
        efac: float,
        ckvnum: float,
        drp: float,
    ):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsProton``.

        Parameters:
            emax: Proton energy limit.
            ean: Analog energy limit.
            tabl: Table-based physics cutoff.
            istrg: Charged-particle straggling controls.
            recl: Light ion recoil control.
            i_mcs_model: Choice of Coulomb scattering model controls.
            i_int_model: Treamtment of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering.
            efac: Stopping power energy spacing controls.
            ckvnum: Cerenkov photon emission controls.
            drp: Lower energy delta-ray cutoff.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if emax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ean is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if tabl is None or not (tabl == -1 or tabl >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if istrg is None or not (istrg in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if recl is None or not (0 <= recl <= 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_mcs_model is None or not (i_mcs_model in {-1, 0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_int_model is None or not (i_int_model in {-1, 0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_els_model is None or not (i_els_model in {-1, 0}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if drp is None or not (drp == -1 or drp >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"phys:h"
        self.mnemonic = Datum.DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (emax, ean, tabl, istrg, recl, i_mcs_model, i_int_model, i_els_model, efac, ckvnum, drp)
        self.designator = types.Designator.PROTON

        self.emax = emax
        self.ean = ean
        self.tabl = tabl
        self.istrg = istrg
        self.recl = recl
        self.i_mcs_model = i_mcs_model
        self.i_int_model = i_int_model
        self.i_els_model = i_els_model
        self.efac = efac
        self.ckvnum = ckvnum
        self.drp = drp


class ParticlePhysicsOptionsOther(ParticlePhysicsOptions):
    """
    ``ParticlePhysicsOptionsProton`` represents INP particle physics option
    data cards with designators other than neutron, photon, electron, and
    proton.

    ``ParticlePhysicsOptionsProton`` inherits attributes from ``Datum``.
    It represents the INP problem type data card with designators other than
    neutron, photon, electron, and proton syntax element.

    Attributes:
        emax: Upper energy limit.
        istrg: Charged-particle straggling controls.
        xmunum: Selection of muonic x-ray data controls.
        xmugam: Probability of emitting k-shell photon.
        i_mcs_model: Choice of Coulomb scattering model controls.
        i_int_model: Treamtment of nuclear interactions controls.
        i_els_model: Treatment of nuclear elastic scattering.
        efac: Stopping power energy spacing controls.
        ckvnum: Cerenkov photon emission controls.
        drp: Lower energy delta-ray cutoff.
    """

    def __init__(
        self,
        designator: types.Designator,
        emax: float,
        istrg: int,
        xmunum: int,
        xmugam: float,
        i_mcs_model: int,
        i_int_model: int,
        i_els_model: int,
        efac: float,
        ckvnum: float,
        drp: float,
    ):
        """
        ``__init__`` initializes ``ParticlePhysicsOptionsOther``.

        Parameters:
            designator: Particle designator.
            emax: Upper energy limit.
            istrg: Charged-particle straggling controls.
            xmunum: Selection of muonic x-ray data controls.
            xmugam: Probability of emitting k-shell photon.
            i_mcs_model: Choice of Coulomb scattering model controls.
            i_int_model: Treamtment of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering.
            efac: Stopping power energy spacing controls.
            ckvnum: Cerenkov photon emission controls.
            drp: Lower energy delta-ray cutoff.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR.
        """

        if designator is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        if emax is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if istrg is None or not (istrg in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if xmunum is None or not (xmunum in {-1, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if xmugam is None or not (0 <= xmugam <= 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_mcs_model is None or not (i_mcs_model in {-1, 0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_int_model is None or not (i_int_model in {-1, 0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if i_els_model is None or not (i_els_model in {-1, 0}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if drp is None or not (drp == -1 or drp >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id = f"phys:{designator.to_mcnp()}"
        self.mnemonic = Datum.DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
        self.parameters = (emax, istrg, xmunum, xmugam, i_mcs_model, i_int_model, i_els_model, efac, ckvnum, drp)
        self.designator = designator

        self.emax = emax
        self.istrg = istrg
        self.xmunum = xmunum
        self.xmugam = xmugam
        self.i_mcs_model = i_mcs_model
        self.i_int_model = i_int_model
        self.i_els_model = i_els_model
        self.efac = efac
        self.ckvnum = ckvnum
        self.drp = drp


class ActivationControl(Datum):
    """
    ``ActivationControl`` represents INP activation control data cards.

    ``ActivationControl`` inherits attributes from ``Datum``. It represents the
    INP activation control data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
    """

    class ActivationControlOption:
        """
        ``ActivationControlOption`` represents INP activation control data card
        options.

        ``ActivationControlOption`` implements INP activation control data card
        options. Its attributes store keywords and values, and its methods
        provide entry and endpoints for working with INP activation control
        data card options. It represents the generic INP activation control
        data card option syntax element, so ``ActivationControl`` depends on
        ``ActivationControlOption`` as a generic data structure and superclass.

        Attributes:
            keyword: Activation control data card option keyword.
            value: Activation control data card option value.
        """

        class ActivationControlKeyword(StrEnum):
            """
            ``ActivationControlKeyword`` represents INP activation control data
            card keywords.

            ``ActivationControlKeyword`` implements INP activation control data
            card keywords as a Python inner class. It enumerates MCNP keywords
            and provides methods for casting strings to
            ``ActivationControlKeyword`` instances. It represents the INP
            activation control data card keyword syntax element, so
            ``ActivationControl`` and ``ActivationControlOption`` depend on
            ``ActivationControlKeyword`` as an enum.
            """

            FISSION = "fission"
            NON_FISSION = "nonfiss"
            DELAYED_NEUTRON = "dn"
            DELAYED_GAMMA = "dg"
            THRESH = "thresh"
            DNBAIS = "dnbais"
            NAP = "nap"
            DNEB = "dneb"
            DGEB = "degb"
            PECUT = "pecut"
            HLCUT = "hlcut"
            SAMPLE = "sample"

            @staticmethod
            def from_mcnp(source: str):
                """
                ``from_mcnp`` generates ``ActivationControlKeyword`` objects
                from INP.

                ``from_mcnp`` constructs instances of
                ``ActivationControlKeyword`` from INP source strings, so it
                operates as a class constructor method and INP parser helper function.

                Parameters:
                    source: INP for activation control option keyword.

                Returns:
                    ``ActivationControlKeyword`` object.

                Raises:
                    MCNPSemanticError: INVALID_DATUM_ACTIVATION_KEYWORD.
                """

                source = _parser.Preprocessor.process_inp(source)

                # Processing Keyword
                if source not in [enum.value for enum in ActivationControl.ActivationControlOption.ActivationControlKeyword]:
                    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_KEYWORD)

                return ActivationControl.ActivationControlOption.ActivationControlKeyword(source)

        def __init__(self, keyword: ActivationControlKeyword, value: any):
            """
            ``__init__`` initializes ``ActivationControlOption``.

            Parameters:
                keyword: Activation control data card option keyword.
                value: Activation control data card option value.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_KEYWORD.
            """

            if keyword is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_KEYWORD)

            match keyword:
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.FISSION:
                    obj = ActivationControl.Fission(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.NON_FISSION:
                    obj = ActivationControl.NonFission(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.DELAYED_NEUTRON:
                    obj = ActivationControl.DelayedNeutron(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.DELAYED_GAMMA:
                    obj = ActivationControl.DelayedGamma(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.THRESH:
                    obj = ActivationControl.Thresh(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.DNBAIS:
                    obj = ActivationControl.Dnbais(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.NAP:
                    obj = ActivationControl.Nap(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.PECUT:
                    obj = ActivationControl.Pecut(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.HLCUT:
                    obj = ActivationControl.Hlcut(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.SAMPLE:
                    obj = ActivationControl.Sample(value)
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.DNEB:
                    assert False, "Unimplemented"
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.DGEB:
                    assert False, "Unimplemented"

            self.__dict__ = obj.__dict__
            self.__class__ = obj.__class__

        @staticmethod
        def from_mcnp(source: str):
            """
            ``from_mcnp`` generates ``ActivationControlOption`` objects from
            INP.

            ``from_mcnp`` constructs instances of ``ActivationControlOption``
            from INP source strings, so it operates as a class constructor
            method and INP parser helper function. Although defined on the
            superclass, it returns ``ActivationControlOption`` subclasses.

            Parameters:
                source: INP for activation option.

            Returns:
                ``ActivationControlOption`` object.

            Raises:
                MCNPSyntaxError: TOOFEW_DATUM_ACTIVATION.
                MCNPSyntaxError: TOOLONG_DATUM_ACTIVATION.
            """

            source = _parser.Preprocessor.process_inp(source)
            tokens = _parser.Parser(source.split("="), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL))

            # Processing Keyword
            keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.from_mcnp(tokens.popl())

            # Processing Values
            match keyword:
                case ActivationControl.ActivationControlOption.ActivationControlKeyword.FISSION | ActivationControl.ActivationControlOption.ActivationControlKeyword.NON_FISSION | ActivationControl.ActivationControlOption.ActivationControlKeyword.DELAYED_NEUTRON | ActivationControl.ActivationControlOption.ActivationControlKeyword.DELAYED_GAMMA | ActivationControl.ActivationControlOption.ActivationControlKeyword.SAMPLE:
                    value = tokens.popl()

                case ActivationControl.ActivationControlOption.ActivationControlKeyword.THRESH | ActivationControl.ActivationControlOption.ActivationControlKeyword.PECUT:
                    value = types.cast_fortran_real(tokens.popl())

                case ActivationControl.ActivationControlOption.ActivationControlKeyword.DNABIS | ActivationControl.ActivationControlOption.ActivationControlKeyword.NAP | ActivationControl.ActivationControlOption.ActivationControlKeyword.HLCUT:
                    value = types.cast_fortran_integer(tokens.popl())

                case ActivationControl.ActivationControlOption.ActivationControlKeyword.DNEB | ActivationControl.ActivationControlOption.ActivationControlKeyword.DGEB:
                    assert False, "Unimplemented"

            if tokens:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_ACTIVATION)

            return ActivationControl.ActivationControlOption(keyword, value)

        def to_mcnp(self):
            """
            ``to_mcnp`` generates INP from ``ActivationOption`` objects.

            ``to_mcnp`` creates INP source string from ``ActivationOption``
            objects, so it provides an MCNP endpoint.

            Returns:
                INP string for ``ActivationOption`` object.
            """

            return f"{ActivationControl.ActivationControlOption.ActivationControlKeyword(self.keyword)}={self.value}"

    class Fission(ActivationControlOption):
        """
        ``Fission`` represents INP Fission activation control data card
        options.

        ``Fission`` inherits attributes from ``ActivationControlOption``. It
        represents the INP Fission material data card option syntax element.

        Attributes:
            particle: Type of delayed particles to be produced.
        """

        def __init__(self, particle: str):
            """
            ``__init__`` initializes ``Fission``.

            Parameters:
                particle: Delayed particle(s) to be produced.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if particle is None or not (particles in {"none", "n,p,e,f,a", "all"}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.FISSION
            self.value = particle
            self.particle = particle

    class NonFission(ActivationControlOption):
        """
        ``NonFission`` represents INP NonFission activation control data card
        options.

        ``NonFission`` inherits attributes from ``ActivationControlOption``. It
        represents the INP NonFission material data card option syntax element.

        Attributes:
            particle: Type of delayed particles to be produced.
        """

        def __init__(self, particle: str):
            """
            ``__init__`` initializes ``NonFission``.

            Parameters:
                particle: Type of delayed particles to be produced.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if particle is None or not (particles in {"none", "n,p,e,f,a", "all"}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.NON_FISSION
            self.value = particle
            self.particle = particle

    class DelayedNeutron(ActivationControlOption):
        """
        ``DelayedNeutron`` represents INP DelayedNeutron activation control
        data card options.

        ``DelayedNeutron`` inherits attributes from
        ``ActivationControlOption``. It represents the INP DelayedNeutron
        material data card option syntax element.

        Attributes:
            source: Delayed neutron data source.
        """

        def __init__(self, source: str):
            """
            ``__init__`` initializes ``DelayedNeutron``.

            Parameters:
                source: Delayed neutron data source.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if state is None or not (state in {"model", "library", "both", "prompt"}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.DELAYED_NEUTRON
            self.value = source
            self.source = source

    class DelayedGamma(ActivationControlOption):
        """
        ``DelayedGamma`` represents INP DelayedGamma activation control data
        card options.

        ``DelayedGamma`` inherits attributes from ``ActivationControlOption``.
        It represents the INP DelayedGamma material data card option syntax
        element.

        Attributes:
            source: Delayed gamma data source.
        """

        def __init__(self, source: str):
            """
            ``__init__`` initializes ``DelayedGamma``.

            Parameters:
                source: Delayed gamma data source.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if source is None or not (source in {"lines", "mg", "none"}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.DELAYED_GAMMA
            self.value = source
            self.source = source

    class Thresh(ActivationControlOption):
        """
        ``Thresh`` represents INP Thresh activation control data card options.

        ``Thresh`` inherits attributes from ``ActivationControlOption``. It
        represents the INP Thresh material data card option syntax element.

        Attributes:
            fraction: Fraction of highest-amplitude discrete delayed-gamma.
        """

        def __init__(self, fraction: float):
            """
            ``__init__`` initializes ``Thresh``.

            Parameters:
                fraction: Fraction of highest-amplitude discrete delayed-gamma.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if fraction is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.THRESH
            self.value = fraction
            self.fraction = fraction

    class Dnbais(ActivationControlOption):
        """
        ``Dnbais`` represents INP Dnbais activation control data card options.

        ``Dnbais`` inherits attributes from ``ActivationControlOption``. It
        represents the INP Dnbais material data card option syntax element.

        Attributes:
            count: Maximum number of delayed neutron per interaction.
        """

        def __init__(self, count: int):
            """
            ``__init__`` initializes ``Dnbais``.

            Parameters:
                count: Maximum number of delayed neutron per interaction.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if count is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.DNBAIS
            self.value = count
            self.count = count

    class Nap(ActivationControlOption):
        """
        ``Nap`` represents INP Nap activation control data card options.

        ``Nap`` inherits attributes from ``ActivationControlOption``. It
        represents the INP Nap material data card option syntax element.

        Attributes:
            count: Number of acitvation product for distributions.
        """

        def __init__(self, count: int):
            """
            ``__init__`` initializes ``Nap``.

            Parameters:
                count: Number of acitvation product for distributions.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if count is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.NAP
            self.value = count
            self.count = count

    class Pecut(ActivationControlOption):
        """
        ``Pecut`` represents INP Pecut activation control data card options.

        ``Pecut`` inherits attributes from ``ActivationControlOption``. It
        represents the INP Pecut material data card option syntax element.

        Attributes:
            cutoff: Delayed-gamma energy cutoff.
        """

        def __init__(self, cutoff: float):
            """
            ``__init__`` initializes ``Pecut``.

            Parameters:
                cutoff: Delayed-gamma energy cutoff.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if state is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.PECUT
            self.value = cutoff
            self.cutoff = cutoff

    class Hlcut(ActivationControlOption):
        """
        ``Hlcut`` represents INP Hlcut activation control data card options.

        ``Hlcut`` inherits attributes from ``ActivationControlOption``. It
        represents the INP Hlcut material data card option syntax element.

        Attributes:
            threshold: Spontaneous-decay half-life threshold.
        """

        def __init__(self, threshold: int):
            """
            ``__init__`` initializes ``Hlcut``.

            Parameters:
                threshold: Spontaneous-decay half-life threshold.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if threshold is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.HLCUT
            self.value = threshold
            self.threshold = threshold

    class Sample(ActivationControlOption):
        """
        ``Sample`` represents INP Sample activation control data card options.

        ``Sample`` inherits attributes from ``ActivationControlOption``. It
        represents the INP Sample material data card option syntax element.

        Attributes:
            state: Flag for correlated or uncorrelated.
        """

        def __init__(self, state: str):
            """
            ``__init__`` initializes ``Sample``.

            Parameters:
                state: Flag for correlated or uncorrelated.

            Raises:
                MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
            """

            if state is None or not (state in {"correlate", "nonfiss_cor"}):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ACTIVATION_VALUE)

            self.keyword = ActivationControl.ActivationControlOption.ActivationControlKeyword.SAMPLE
            self.value = state
            self.state = state

    def __init__(self, pairs: tuple[ActivationControlOption]):
        """
        ``__init__`` initializes ``ActivationControl``.

        Parameters:
            pairs: Tuple of key-value pairs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None or not pairs:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for pair in pairs:
            if pair is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"act"
        self.mnemonic = Datum.DatumMnemonic.ACTIVATION_CONTROL
        self.parameters = pairs

        self.paris = pairs


class TimeEnergyWeightCutoffs(Datum):
    """
    ``TimeEnergyWeightCutoffs`` represents INP time, energy, and weight cutoffs
    data cards.

    ``TimeEnergyWeightCutoffs`` inherits attributes from ``Datum``. It
    represents the INP time, energy, and weight cutoffs data card syntax
    element.

    Attributes:
        designator: Particle designator.
        time: Time cutoff.
        energy: Lower energy cutoff.
        weight1: Weight cutoff #1.
        weight2: Weight cutoff #2.
        source: Minimum source weight.
    """

    def __init__(
        self, designator: types.Designator, time: float, energy: float, weight1: float, weight2: float, source: float
    ):
        """
        ``__init__`` initializes ``TimeEnergyWeightCutoffs``.

        Parameters:
            designator: Particle designator.
            time: Time cutoff.
            energy: Lower energy cutoff.
            weight1: Weight cutoff #1.
            weight2: Weight cutoff #2.
            source: Minimum source weight.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR.
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if designator is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        if time is None or not (time > 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if energy is None or not (energy > 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if weight1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if weight2 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if source is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"cut:{designator.to_mcnp()}"
        self.mnemonic = Datum.DatumMnemonic.TIME_ENERGY_WEIGHT_CUTOFFS
        self.parameters = (time, energy, weight1, weight2, source)
        self.designator = designator

        self.time = time
        self.energy = energy
        self.weight1 = weight1
        self.weight2 = weight2
        self.source = source


class CellEnergyCutoff(Datum):
    """
    ``CellEnergyCutoff`` represents INP cell-by-cell energy cutoffs data cards.

    ``CellEnergyCutoff`` inherits attributes from ``Datum``. It represents the
    INP cell-by-cell energy cutoffs data card syntax element.

    Attributes:
        designator: Particle designator.
        cutoffs: Lower energy cutoff of cells.
    """

    def __init__(self, designator: types.Designator, cutoffs: tuple[float]):
        """
        ``__init__`` initializes ``CellEnergyCutoff``.

        Parameters:
            designator: Particle designator.
            cutoffs: Lower energy cutoff of cells.
        """

        if designator is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        if cutoffs is None or not cutoffs:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for cutoff in cutoffs:
            if cutoff is None or not (cutoff > 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"elpt:{designator.to_mcnp()}"
        self.mnemonic = Datum.DatumMnemonic.CELL_ENERGY_CUTOFF
        self.parameters = cutoffs
        self.designator = designator

        self.cutoffs = cutoffs


class FreeGasThermalTemperature(Datum):
    """
    ``FreeGasThermalTemperature`` represents INP free-gas thermal temperature
    data cards.

    ``FreeGasThermalTemperature`` inherits attributes from ``Datum``. It
    represents the INP free-gas thermal temperature data card syntax element.

    Attributes:
        suffix: Index of time on the thermal time.
        temperatures: Temperatures of cells at given time indexes.
    """

    def __init__(self, suffix: int, temperatures: float):
        """
        ``__init__`` initializes ``FreeGasThermalTemperature``.

        Parameters:
            suffix: Index of time on the thermal time.
            temperatures: Temperatures of cells at given time indexes.
        """

        if suffix is None or not (0 <= suffix <= 99):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        if temperatures is None or not temperatures:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for temperature in temperatures:
            if temperature is None or not (temperature > 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"tmp{suffix}"
        self.mnemonic = Datum.DatumMnemonic.FREE_GAS_THERMAL_TEMPERATURE
        self.parameters = temperatures
        self.suffix = suffix

        self.temperatures = temperatures


class ThermalTimes(Datum):
    """
    ``ThermalTimes`` represents INP thermal times data cards.

    ``ThermalTimes`` inherits attributes from ``Datum``. It represents the INP
    thermal times data card syntax element.

    Attributes:
        times: Times in shakes.
    """

    def __init__(self, times: tuple[int]):
        """
        ``__init__`` initializes ``FreeGasThermalTemperature``.

        Parameters:
            times: Times in shakes.
        """

        if times is None or not times:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for time in times:
            if time is None or not (0 <= i <= 99):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"thtme"
        self.mnemonic = Datum.DatumMnemonic.THERMAL_TIMES
        self.parameters = times

        self.times = times


class ModelPhysicsControl(Datum):
    """
    ``ModelPhysicsControl`` represents INP model physics control data cards.

    ``ModelPhysicsControl`` inherits attributes from ``Datum``. It represents
    the INP model physics control data card syntax element.

    Attributes:
        setting: On/Off.
    """

    def __init__(self, setting: str):
        """
        ``__init__`` initializes ``ModelPhysicsControl``.

        Parameters:
            setting: On/Off.
        """

        if setting is None or not (setting in {"yes", "no"}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"mphys"
        self.mnemonic = Datum.DatumMnemonic.MODEL_PHYSICS_CONTROL
        self.parameters = (setting,)

        self.setting = setting


class Lca(Datum):
    """
    ``Lca`` represents INP model physics LCA data cards.

    ``Lca`` inherits attributes from ``Datum``. It represents the INP model
    physics LCA data card syntax element.

    Attributes:
        ielas: Elastic scattering controls.
        ipreq: Pre-equilibrium model controls.
        iexisa: Model choice controls.
        ichoic: ISABEL intranuclear cascade modifier controls.
        jcoul: Coulomb barrier for incident charged particles controls.
        nexite: Nuclear recoil energy to get excitation energy.
        npidk: Pion interaction control.
        noact: Particle transport options.
        icem: Choose alternative physics model.
        ilaq: Choose light ion and nucleon physics modules.
        nevtype: Choose number of evaporation particles modeled by GEM2.
    """

    def __init__(
        self,
        ielas: int,
        ipreq: int,
        iexisa: int,
        ichoic: str,
        jcoul: int,
        nexite: int,
        npidk: int,
        noact: int,
        icem: int,
        ilaq: int,
        nevtype: float,
    ):
        """
        ``__init__`` initializes ``Lca``.

        Parameters:
            ielas: Elastic scattering controls.
            ipreq: Pre-equilibrium model controls.
            iexisa: Model choice controls.
            ichoic: ISABEL intranuclear cascade modifier controls.
            jcoul: Coulomb barrier for incident charged particles controls.
            nexite: Nuclear recoil energy to get excitation energy.
            npidk: Pion interaction control.
            noact: Particle transport options.
            icem: Choose alternative physics model.
            ilaq: Choose light ion and nucleon physics modules.
            nevtype: Choose number of evaporation particles modeled by GEM2.
        """

        if ielas is None or not (ielas in {0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ipreq is None or not (ipreq in {0, 1, 2, 3}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if iexisa is None or not (iexisa in {0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ichoic is None or not (re.match(r"(0|1|-2)([0-9])([0-5])([1-6])".ichoic)):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if jcoul is None or not (jcoul in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nexite is None or not (nexite in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if npidk is None or not (npidk in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if noact is None or not (noact in {-2, -1, 0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if icem is None or not (icem in {0, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ilaq is None or not (ilaq in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nevtype is None or not (nevtype >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"lca"
        self.mnemonic = Datum.DatumMnemonic.LCA
        self.parameters = (ielas, ipreq, iexisa, ichoic, jcoul, nexite, npidk, noact, icem, ilaq, nevtype)

        self.ielas = ielas
        self.ipreq = ipreq
        self.iexisa = iexisa
        self.ichoic = ichoic
        self.jcoul = jcoul
        self.nexite = nexite
        self.npidk = npidk
        self.noact = noact
        self.icem = icem
        self.ilaq = ilaq
        self.nevtype = nevtype


class Lcb(Datum):
    """
    ``Lcb`` represents INP model physics LCB data cards.

    ``Lcb`` inherits attributes from ``Datum``. It represents the INP model
    physics LCB data card syntax element.

    Attributes:
        flebn1: Kinetic energy #1.
        flebn2: Kinetic energy #2.
        flebn3: Kinetic energy #3.
        flebn4: Kinetic energy #4.
        flebn5: Kinetic energy #5.
        flebn6: Kinetic energy #6.
        ctofe: Cutoff kinetic energy.
        flim0: Maximum correction allowed for mass-energy balacing.
    """

    def __init__(
        self,
        flebn1: float,
        flebn2: float,
        flebn3: float,
        flebn4: float,
        flebn5: float,
        flebn6: float,
        ctofe: float,
        flim0: float,
    ):
        """
        ``__init__`` initializes ``Lcb``.

        Parameters:
            flebn1: Kinetic energy #1.
            flebn2: Kinetic energy #2.
            flebn3: Kinetic energy #3.
            flebn4: Kinetic energy #4.
            flebn5: Kinetic energy #5.
            flebn6: Kinetic energy #6.
            ctofe: Cutoff kinetic energy.
            flim0: Maximum correction allowed for mass-energy balacing.
        """

        if flebn1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn2 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn3 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn4 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn5 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flebn6 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ctofe is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if flim0 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"lcb"
        self.mnemonic = Datum.DatumMnemonic.LCB
        self.parameters = (flebn1, flebn2, flebn3, flebn4, flebn5, flebn6, ctofe, flim0)

        self.flebn1 = flebn1
        self.flebn2 = flebn2
        self.flebn3 = flebn3
        self.flebn4 = flebn4
        self.flebn5 = flebn5
        self.flebn6 = flebn6
        self.ctofe = ctofe
        self.flim0 = flim0


class Lcc(Datum):
    """
    ``Lcc`` represents INP model physics LCC data cards.

    ``Lcc`` inherits attributes from ``Datum``. It represents the INP model
    physics LCC data card syntax element.

    Attributes:
        atincl: Rescaling factor of the cascade duration.
        v0incl: Potential depth.
        xfoisaincl: Maximum impact parameter for Pauli blokcing controls.
        npaulincl: Pauli blocking parameter.
        nosurfincl: Diffuse nuclear surface based on density controls.
        ecutincl: Use Bertini model below this energy.
        ebankincl: Wrtie no INCL bank particles.
        ebankabla: Write not ABLA bank particles.
    """

    def __init__(
        self,
        atincl: float,
        v0incl: float,
        xfoisaincl: float,
        npaulincl: int,
        nosurfincl: int,
        ecutincl: float,
        ebankincl: float,
        ebankabla: float,
    ):
        """
        ``__init__`` initializes ``Lcc``.

        Parameters:
            atincl: Rescaling factor of the cascade duration.
            v0incl: Potential depth.
            xfoisaincl: Maximum impact parameter for Pauli blokcing controls.
            npaulincl: Pauli blocking parameter.
            nosurfincl: Diffuse nuclear surface based on density controls.
            ecutincl: Use Bertini model below this energy.
            ebankincl: Wrtie no INCL bank particles.
            ebankabla: Write not ABLA bank particles.
        """

        if atincl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if v0incl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if xfoisaincl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if npaulincl is None or not (npaulincl in {1, 0, -1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nosurfincl is None or not (nosurfincl in {-2, -1, 0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ecutincl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ebankincl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ebankabla is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"lcc"
        self.mnemonic = Datum.DatumMnemonic.LCB
        self.parameters = (atincl, v0incl, xfoisaincl, npaulincl, nosurfincl, ecutincl, ebankincl, ebankabla)

        self.atincl = atincl
        self.v0incl = v0incl
        self.xfoisaincl = xfoisaincl
        self.npaulincl = npaulincl
        self.nosurfincl = nosurfincl
        self.ecutincl = ecutincl
        self.ebankincl = ebankincl
        self.ebankabla = ebankabla


class Lea(Datum):
    """
    ``Lea`` represents INP model physics LEA data cards.

    ``Lea`` inherits attributes from ``Datum``. It represents the INP model
    physics LEA data card syntax element.

    Attributes:
        ipht: Generation of de-excitation phontes controls.
        icc: Level of physics for PHT physics definitions.
        nobalc: Mass-energy balancing in cascade controls.
        nobale: Mass-energy balancing in evaporation controls.
        ifbrk: Fermi-breakup model nuclide range controls.
        ilvden: Level-density model controls.
        ievap: Evaporation and fission models controls.
        nofis: Fission controls.
    """

    def __init__(
        self,
        ipht: int,
        icc: int,
        nobalc: int,
        nobale: int,
        ifbrk: int,
        ilvden: int,
        ievap: int,
        nofis: int,
    ):
        """
        ``__init__`` initializes ``Lea``.

        Parameters:
            ipht: Generation of de-excitation phontes controls.
            icc: Level of physics for PHT physics definitions.
            nobalc: Mass-energy balancing in cascade controls.
            nobale: Mass-energy balancing in evaporation controls.
            ifbrk: Fermi-breakup model nuclide range controls.
            ilvden: Level-density model controls.
            ievap: Evaporation and fission models controls.
            nofis: Fission controls.
        """

        if ipht is None or not (ipht in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if icc is None or not (icc in {0, 1, 2, 3, 4}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nobalc is None or not (nobalc in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nobale is None or not (nobale in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ifbrk is None or not (ifbrk in {0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ilvden is None or not (ilvden in {-1, 0, 1}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if ievap is None or not (ievap in {0, -1, 1, 2}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if nofis is None or not (nofis in {1, 0}):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = f"lea"
        self.mnemonic = Datum.DatumMnemonic.LEA
        self.parameters = (ipht, icc, nobalc, nobale, ifbrk, ilvden, ievap, nofis)

        self.ipht = ipht
        self.icc = icc
        self.nobalc = nobalc
        self.nobale = nobale
        self.ifbrk = ifbrk
        self.ilvden = ilvden
        self.ievap = ievap
        self.nofis = nofis


class _Placeholder(Datum):
    def __init__(self, mnemonic: Datum.DatumMnemonic, parameters: tuple[any]):
        self.id = mnemonic
        self.mnemonic = mnemonic
        self.parameters = parameters


class Nps(Datum):
    """
    ``Nps`` represents INP nps data cards.

    ``Nps`` inherits attributes from ``Datum``. It represents the INP model
    physics nps data card syntax element.

    Attributes:
        npp: Total number of histories to run.
        npsmg: Number of histroy with direct source contributions.
    """

    def __init__(self, npp: int, npsmg: int):
        """
        ``__init__`` initializes ``Nps``.

        Parameters:
            npp: Total number of histories to run.
            npsmg: Number of histroy with direct source contributions.
        """

        if npp is None or not (npp > 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if npsmg is None or not (npsmg > 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.id: final[str] = "nps"
        self.mnemonic: final[Datum.DatumMnemonic] = Datum.DatumMnemonic.HISTORY_CUTOFF
        self.parameters: final[tuple] = (npp, npsmg)

        self.npp: final[int] = npp
        self.npsmg: final[int] = npsmg
