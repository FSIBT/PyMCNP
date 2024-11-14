import re

from .datum import DatumMnemonic, _Placeholder
from .history_cutoff import HistoryCutoff
from .source import SourceDefinition, SourceDefinitionOption, SourceDefinitionKeyword
from .volume import Volume
from .area import Area
from .transformation import Transformation
from .universe import Universe
from .lattice import Lattice
from .fill import Fill
from .stochastic_geometry import StochasticGeometry
from .deterministic_materials import DeterministicMaterials
from .weight_window import WeightWindow
from .embedded_geometry import EmbeddedGeometry
from .embedded_control import EmbeddedControl
from .embedded_energy_boundaries import EmbeddedEnergyBoundaries
from .embedded_energy_multipliers import EmbeddedEnergyMultipliers
from .embedded_time_boundaries import EmbeddedTimeBoundaries
from .embedded_time_multipliers import EmbeddedTimeMultipliers
from .embedded_dose_boundaries import EmbeddedDoseBoundaries
from .embedded_dose_multipliers import EmbeddedDoseMultipliers
from .material import Material, MaterialKeyword, MaterialValue, MaterialOption
from .material_neutron_scattering import MaterialNeutronScattering
from .material_nuclides_substition import MaterialNuclideSubstitution
from .on_the_fly_broadening import OnTheFlyBroadening
from .total_fisssion import TotalFission
from .fission_turnoff import FissionTurnoff
from .atomic_weight import AtomicWeight
from .cross_section_file import CrossSectionFile
from .void import Void
from .multigroup_adjoing_transport import MultigroupAdjointTransport
from .discrete_reaction_cross_section import DiscreteReactionCrossSection
from .problem_type import ProblemType
from .particle_physics_options import ParticlePhysicsOptions
from .activation_control import ActivationControl
from .time_energy_weight_cutoffs import TimeEnergyWeightCutoffs
from .cell_energy_cutoff import CellEnergyCutoff
from .free_gas_thermal_temperature import FreeGasThermalTemperature
from .thermal_times import ThermalTimes
from .model_physics_control import ModelPhysicsControl
from .lca import Lca
from .lcb import Lcb
from .lcc import Lcc
from .lea import Lea
from .random import Random, RandomKeyword, RandomOption


from ...utils import errors
from ...utils import _parser

from ...utils import types


def create_datum_from_mcnp(source: str, line: types.McnpInteger = None):
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

    source = _parser.Preprocessor.process_inp(source)
    source, comments = _parser.Preprocessor.process_inp_comments(source)
    tokens = _parser.Parser(
        re.split(r' |:|=', source),
        errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM),
    )

    # Processing Mnemonic
    mnemonic = re.search(r'^[a-zA-z*]+', tokens.peekl())
    mnemonic = mnemonic.group() if mnemonic else ''
    mnemonic = DatumMnemonic.from_mcnp(mnemonic)

    # Processing Suffix & Parameters
    suffix = None
    designator = None
    match mnemonic:
        case DatumMnemonic.VOLUME:
            tokens.popl()
            if tokens.peekl() == 'no':
                tokens.popl()
                has_no = True
            else:
                has_no = False
            volumes = tuple(types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = Volume(volumes, has_no=has_no)

        case DatumMnemonic.AREA:
            tokens.popl()
            areas = tuple(types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = Area(areas)

        case DatumMnemonic.TRANSFORMATION:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])
            entries = tuple(types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            N = len(entries)
            displacement = tuple(entries[:3])
            if N <= 3:
                one = types.McnpReal.from_mcnp('1')
                zero = types.McnpReal.from_mcnp('0')
                rotation = (
                    tuple((one, zero, zero)),
                    tuple((zero, one, zero)),
                    tuple((zero, zero, one)),
                )
            else:
                rotation = (
                    tuple(entries[3:6]),
                    tuple(entries[6:9]),
                    tuple(entries[9:12]),
                )
            if N == 13 or N == 4:
                system = int(float(entries[-1]))
            else:
                system = 1

            datum = Transformation(displacement, rotation, system, suffix)

        case DatumMnemonic.UNIVERSE:
            tokens.popl()
            universes = tuple(
                types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))
            )

            datum = Universe(universes)

        case DatumMnemonic.LATTICE:
            tokens.popl()
            lattices = tuple(
                types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))
            )

            datum = Lattice(lattices)

        case DatumMnemonic.FILL:
            tokens.popl()
            fills = tuple(types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = Fill(fills)

        case DatumMnemonic.STOCHASTIC_GEOMETRY:
            tokens.popl()
            transformations = tuple(
                StochasticGeometry.StochasticGeometryValue(
                    types.fortran_integer(tokens.popl()),
                    types.fortran_real(tokens.popl()),
                    types.fortran_real(tokens.popl()),
                    types.fortran_real(tokens.popl()),
                )
                for _ in range(0, len(tokens), 4)
            )

            datum = StochasticGeometry(transformations)

        case DatumMnemonic.DETERMINISTIC_MATERIALS:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])
            zaids = tuple(types.Zaid.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = DeterministicMaterials(zaids)

        case DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW:
            tokens.popl()
            pairs = tuple(
                WeightWindow.WeightWindowOption.from_mcnp(tokens.popl())
                for _ in range(0, len(tokens))
            )

            datum = WeightWindow(pairs)

        case DatumMnemonic.EMBEDDED_GEOMETRY:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])
            pairs = tuple()
            while tokens:
                keyword = tokens.popl()
                values = tuple()
                while tokens:
                    try:
                        EmbeddedGeometry.EmbeddedGeometryOption.from_mcnp(tokens.peekl())
                        break
                    except Exception:
                        values.append(tokens.popl())
                        pass
                pairs.append(
                    EmbeddedGeometry.EmbeddedGeometryOption.from_mcnp(
                        f"{keyword}={' '.join(values)}"
                    )
                )

            datum = EmbeddedGeometry(pairs, suffix)

        case DatumMnemonic.EMBEDDED_CONTROL:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])
            designator = types.Designator.from_mcnp(tokens.popl())
            pairs = tuple()
            while tokens:
                keyword = tokens.popl()
                values = tuple()
                while tokens:
                    try:
                        EmbeddedControl.EmbeddedControlOption.from_mcnp(tokens.peekl())
                        break
                    except Exception:
                        values.append(tokens.popl())
                        pass
                pairs.append(
                    EmbeddedControl.EmbeddedControlOption.from_mcnp(f"{keyword}={' '.join(values)}")
                )

            datum = EmbeddedControl(pairs, suffix, designator)

        case DatumMnemonic.EMBEDDED_ENERGY_BOUNDARIES:
            if len(tokens) < 1:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

            suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])
            energies = tuple(types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = EmbeddedEnergyBoundaries(energies, suffix)

        case DatumMnemonic.EMBEDDED_ENERGY_MULTIPLIERS:
            if len(tokens) < 1:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

            suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])
            multipliers = tuple(
                [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]
            )

            datum = EmbeddedEnergyMultipliers(multipliers, suffix)

        case DatumMnemonic.EMBEDDED_TIME_BOUNDARIES:
            if len(tokens) < 1:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM)

            suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])
            times = tuple(types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = EmbeddedTimeBoundaries(times, suffix)

        case DatumMnemonic.EMBEDDED_TIME_MULTIPLIERS:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])
            multipliers = tuple(
                [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]
            )

            datum = EmbeddedTimeMultipliers(multipliers, suffix)

        case DatumMnemonic.EMBEDDED_DOSE_BOUNDARIES:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])
            doses = tuple(types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = EmbeddedDoseBoundaries(doses, suffix)

        case DatumMnemonic.EMBEDDED_DOSE_MULTIPLIERS:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])
            multipliers = tuple(
                [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]
            )

            datum = EmbeddedDoseMultipliers(multipliers, suffix)

        case DatumMnemonic.MATERIAL:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[1:])

            substances = []
            while tokens:
                try:
                    MaterialKeyword.from_mcnp(tokens.peekl())
                    break
                except Exception:
                    substances.append(
                        MaterialValue(
                            types.Zaid.from_mcnp(tokens.popl()),
                            types.McnpReal.from_mcnp(tokens.popl()),
                        )
                    )
                    pass

            options = []
            while tokens:
                keyword = tokens.popl()
                values = []
                while tokens:
                    try:
                        MaterialKeyword.from_mcnp(tokens.peekl())
                        break
                    except Exception:
                        values.append(tokens.popl())
                        pass
                options.append(MaterialOption.from_mcnp(f"{keyword}={' '.join(values)}"))

            datum = Material(substances, options, suffix)

        case DatumMnemonic.MATERIAL_NEUTRON_SCATTERING:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])
            identifiers = tuple(tokens.popl() for _ in range(0, len(tokens)))

            datum = MaterialNeutronScattering(identifiers, suffix)

        case DatumMnemonic.MATERIAL_NUCLIDE_SUBSTITUTION:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])
            designator = types.Designator.from_mcnp(tokens.popl())
            zaids = tuple(types.Zaid.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = MaterialNuclideSubstitution(zaids, suffix, designator)

        case DatumMnemonic.ON_THE_FLY_BROADENING:
            tokens.popl()
            zaids = tuple(types.Zaid.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = OnTheFlyBroadening(zaids)

        case DatumMnemonic.TOTAL_FISSION:
            tokens.popl()

            if tokens:
                if tokens.popl() != 'no':
                    raise errors.MCNPSyntaxError(errors.MCNPSytnaxCodes.KEYWORD_DATUM_TOTNU_NO)

                datum = TotalFission(True)
            else:
                datum = TotalFission(False)

        case DatumMnemonic.FISSION_TURNOFF:
            tokens.popl()
            states = tuple(
                types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))
            )

            datum = FissionTurnoff(states)

        case DatumMnemonic.ATOMIC_WEIGHT:
            tokens.popl()
            weight_ratios = tuple(
                AtomicWeight.AtomicWeightValue.from_mcnp(f'{tokens.popl()} {tokens.popl()}')
            )

            datum = AtomicWeight(weight_ratios)

        case DatumMnemonic.CROSS_SECTION_FILE:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])
            weight_ratios = tuple(
                CrossSectionFile.CrossSectionFileValue.from_mcnp(f'{tokens.popl()} {tokens.popl()}')
            )

            datum = CrossSectionFile(weight_ratios, suffix)

        case DatumMnemonic.VOID:
            tokens.popl()
            numbers = tuple(
                types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))
            )

            datum = Void(numbers)

        case DatumMnemonic.MULTIGROUP_ADJOINT_TRANSPORT:
            tokens.popl()
            mcal = tokens.popl()
            igm = types.McnpInteger.from_mcnp(tokens.popl())
            iplt = types.McnpInteger.from_mcnp(tokens.popl())
            isb = types.McnpInteger.from_mcnp(tokens.popl())
            icw = types.McnpInteger.from_mcnp(tokens.popl())
            fnw = types.McnpInteger.from_mcnp(tokens.popl())
            rim = types.McnpInteger.from_mcnp(tokens.popl())

            datum = MultigroupAdjointTransport(mcal, igm, iplt, isb, icw, fnw, rim)

        case DatumMnemonic.DISCRETE_REACTION_CROSS_SECTION:
            tokens.popl()
            zaids = tuple(types.Zaid.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = DiscreteReactionCrossSection(zaids)

        case DatumMnemonic.PROBLEM_TYPE:
            tokens.popl()
            particles = tuple(
                types.Designator.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))
            )

            datum = ProblemType(particles)

        case DatumMnemonic.PARTICLE_PHYSICS_OPTIONS:
            tokens.popl()
            designator = types.Designator.from_mcnp(tokens.popl())

            if len(designator.particles) != 1:
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOMANY_DATUM_PHYS)

            match designator.particles[0]:
                case types.Designator.Particle.NEUTRON:
                    emax = types.McnpReal.from_mcnp(tokens.popl())
                    emcnf = types.McnpReal.from_mcnp(tokens.popl())
                    iunr = types.McnpInteger.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    colif = types.McnpReal.from_mcnp(tokens.popl())
                    cutn = types.McnpReal.from_mcnp(tokens.popl())
                    ngam = types.McnpInteger.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    i_int_model = types.McnpInteger.from_mcnp(tokens.popl())
                    i_els_model = types.McnpInteger.from_mcnp(tokens.popl())

                    parameters = (
                        emax,
                        emcnf,
                        iunr,
                        colif,
                        cutn,
                        ngam,
                        i_int_model,
                        i_els_model,
                    )

                case types.Designator.Particle.PHOTON:
                    emcpf = types.McnpReal.from_mcnp(tokens.popl())
                    ides = types.McnpInteger.from_mcnp(tokens.popl())
                    nocoh = types.McnpInteger.from_mcnp(tokens.popl())
                    ispn = types.McnpInteger.from_mcnp(tokens.popl())
                    nodop = types.McnpInteger.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    fism = types.McnpInteger.from_mcnp(tokens.popl())

                    parameters = (emcpf, ides, nocoh, ispn, nodop, fism)

                case types.Designator.Particle.ELECTRON:
                    emax = types.McnpReal.from_mcnp(tokens.popl())
                    ides = types.McnpInteger.from_mcnp(tokens.popl())
                    ibad = types.McnpInteger.from_mcnp(tokens.popl())
                    istrg = types.McnpInteger.from_mcnp(tokens.popl())
                    bnum = types.McnpReal.from_mcnp(tokens.popl())
                    xnum = types.McnpReal.from_mcnp(tokens.popl())
                    rnok = types.McnpReal.from_mcnp(tokens.popl())
                    enum = types.McnpReal.from_mcnp(tokens.popl())
                    numb = types.McnpReal.from_mcnp(tokens.popl())
                    i_mcs_model = types.McnpInteger.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    efac = types.McnpReal.from_mcnp(tokens.popl())
                    electron_method_boundary = types.McnpReal.from_mcnp(tokens.popl())
                    ckvnum = types.McnpReal.from_mcnp(tokens.popl())

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

                case types.Designator.Particle.PROTON:
                    emax = types.McnpReal.from_mcnp(tokens.popl())
                    ean = types.McnpReal.from_mcnp(tokens.popl())
                    tabl = types.McnpReal.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    istrg = types.McnpInteger.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    recl = types.McnpReal.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    i_mcs_model = types.McnpInteger.from_mcnp(tokens.popl())
                    i_int_model = types.McnpInteger.from_mcnp(tokens.popl())
                    i_els_model = types.McnpInteger.from_mcnp(tokens.popl())
                    efac = types.McnpReal.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    ckvnum = types.McnpReal.from_mcnp(tokens.popl())
                    drp = types.McnpReal.from_mcnp(tokens.popl())

                    parameters = (
                        emax,
                        ean,
                        tabl,
                        istrg,
                        recl,
                        i_mcs_model,
                        i_int_model,
                        i_els_model,
                        efac,
                        ckvnum,
                        drp,
                    )

                case _:
                    emax = types.McnpReal.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    istrg = types.McnpInteger.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    xmunum = types.McnpInteger.from_mcnp(tokens.popl())
                    xmugam = types.McnpReal.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    i_mcs_model = types.McnpInteger.from_mcnp(tokens.popl())
                    i_int_model = types.McnpInteger.from_mcnp(tokens.popl())
                    i_els_model = types.McnpInteger.from_mcnp(tokens.popl())
                    efac = types.McnpReal.from_mcnp(tokens.popl())
                    if tokens.popl() != 'j':
                        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
                    ckvnum = types.McnpReal.from_mcnp(tokens.popl())
                    drp = types.McnpReal.from_mcnp(tokens.popl())

                    parameters = (
                        emax,
                        istrg,
                        xmunum,
                        xmugam,
                        i_mcs_model,
                        i_int_model,
                        i_els_model,
                        efac,
                        ckvnum,
                        drp,
                    )

            datum = ParticlePhysicsOptions(designator, parameters)

        case DatumMnemonic.ACTIVATION_CONTROL:
            tokens.popl()
            pairs = tuple()
            while tokens:
                keyword = tokens.popl()
                values = tuple()
                while tokens:
                    try:
                        ActivationControl.ActivationControlOption.from_mcnp(tokens.peekl())
                        break
                    except Exception:
                        values.append(tokens.popl())
                        pass
                pairs.append(
                    ActivationControl.ActivationControlOption.from_mcnp(
                        f"{keyword}={' '.join(values)}"
                    )
                )

            datum = ActivationControl(pairs)

        case DatumMnemonic.TIME_ENERGY_WEIGHT_CUTOFFS:
            tokens.popl()
            designator = types.Designator.from_mcnp(tokens.popl())

            t = types.McnpReal.from_mcnp(tokens.popl())
            e = types.McnpReal.from_mcnp(tokens.popl()) if tokens else None
            weight1 = types.McnpReal.from_mcnp(tokens.popl()) if tokens else None
            weight2 = types.McnpReal.from_mcnp(tokens.popl()) if tokens else None
            source = types.McnpReal.from_mcnp(tokens.popl()) if tokens else None

            datum = TimeEnergyWeightCutoffs(designator, t, e, weight1, weight2, source)

        case DatumMnemonic.CELL_ENERGY_CUTOFFS:
            tokens.popl()
            designator = types.Designator.from_mcnp(tokens.popl())
            cutoffs = types.McnpReal.from_mcnp(tokens.popl())

            datum = CellEnergyCutoff(designator, cutoffs)

        case DatumMnemonic.FREE_GAS_THERMAL_TEMPERATURE:
            suffix = types.McnpInteger.from_mcnp(tokens.popl()[3:])
            temperatures = tuple(
                types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))
            )

            datum = FreeGasThermalTemperature(suffix, temperatures)

        case DatumMnemonic.THERMAL_TIMES:
            tokens.popl()
            times = tuple(types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens)))

            datum = ThermalTimes(times)

        case DatumMnemonic.MODEL_PHYSICS_CONTROL:
            tokens.popl()
            if tokens:
                ModelPhysicsControl(tokens.popl())
            else:
                datum = ModelPhysicsControl('off')

        case DatumMnemonic.LCA:
            tokens.popl()
            ielas = types.McnpInteger.from_mcnp(tokens.popl())
            ipreq = types.McnpInteger.from_mcnp(tokens.popl())
            iexisa = types.McnpInteger.from_mcnp(tokens.popl())
            ichoic = tokens.popl()
            jcoul = types.McnpInteger.from_mcnp(tokens.popl())
            nexite = types.McnpInteger.from_mcnp(tokens.popl())
            npidk = types.McnpInteger.from_mcnp(tokens.popl())
            noact = types.McnpInteger.from_mcnp(tokens.popl())
            icem = types.McnpInteger.from_mcnp(tokens.popl())
            ilaq = types.McnpInteger.from_mcnp(tokens.popl())
            nevtype = types.McnpReal.from_mcnp(tokens.popl())

            datum = Lca(
                ielas,
                ipreq,
                iexisa,
                ichoic,
                jcoul,
                nexite,
                npidk,
                noact,
                icem,
                ilaq,
                nevtype,
            )

        case DatumMnemonic.LCB:
            tokens.popl()
            lebn1 = types.McnpReal.from_mcnp(tokens.popl())
            flebn2 = types.McnpReal.from_mcnp(tokens.popl())
            flebn3 = types.McnpReal.from_mcnp(tokens.popl())
            flebn4 = types.McnpReal.from_mcnp(tokens.popl())
            flebn5 = types.McnpReal.from_mcnp(tokens.popl())
            flebn6 = types.McnpReal.from_mcnp(tokens.popl())
            ctofe = types.McnpReal.from_mcnp(tokens.popl())
            flim0 = types.McnpReal.from_mcnp(tokens.popl())

            datum = Lcb(lebn1, flebn2, flebn3, flebn4, flebn5, flebn6, ctofe, flim0)

        case DatumMnemonic.LCC:
            tokens.popl()
            atincl = types.McnpReal.from_mcnp(tokens.popl())
            v0incl = types.McnpReal.from_mcnp(tokens.popl())
            xfoisaincl = types.McnpReal.from_mcnp(tokens.popl())
            npaulincl = types.McnpReal.from_mcnp(tokens.popl())
            nosurfincl = types.McnpReal.from_mcnp(tokens.popl())
            if tokens.popl() != 'j':
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
            if tokens.popl() != 'j':
                raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_PHYS_J)
            ecutincl = types.McnpReal.from_mcnp(tokens.popl())
            ebankincl = types.McnpReal.from_mcnp(tokens.popl())
            ebankabla = types.McnpReal.from_mcnp(tokens.popl())

            datum = Lcc(
                atincl,
                v0incl,
                xfoisaincl,
                npaulincl,
                nosurfincl,
                ecutincl,
                ebankincl,
                ebankabla,
            )

        case DatumMnemonic.LEA:
            tokens.popl()
            ipht = types.McnpInteger.from_mcnp(tokens.popl())
            icc = types.McnpInteger.from_mcnp(tokens.popl())
            nobalc = types.McnpInteger.from_mcnp(tokens.popl())
            nobale = types.McnpInteger.from_mcnp(tokens.popl())
            ifbrk = types.McnpInteger.from_mcnp(tokens.popl())
            ilvden = types.McnpInteger.from_mcnp(tokens.popl())
            ievap = types.McnpInteger.from_mcnp(tokens.popl())
            nofis = types.McnpInteger.from_mcnp(tokens.popl())

            datum = Lea(ipht, icc, nobalc, nobale, ifbrk, ilvden, ievap, nofis)

        case DatumMnemonic.HISTORY_CUTOFF:
            tokens.popl()
            npp = types.McnpInteger.from_mcnp(tokens.popl())
            npsmg = types.McnpInteger.from_mcnp(tokens.popl()) if tokens else None

            datum = HistoryCutoff(npp, npsmg)

        case DatumMnemonic.RANDOM:
            tokens.popl()
            pairs = []
            while tokens:
                keyword = tokens.popl()
                values = []
                while tokens:
                    try:
                        try_keyword = re.search(r'([*]?[A-Za-z]+)', tokens.peekl()).group()
                        RandomKeyword.from_mcnp(try_keyword)
                        break
                    except Exception:
                        values.append(tokens.popl())
                        pass

                option = RandomOption.from_mcnp(f"{keyword}={' '.join(values)}")
                pairs.append(option)
            pairs = tuple(pairs)

            datum = Random(pairs)
        case DatumMnemonic.GENERAL_SOURCE_DEFINITION:
            tokens.popl()
            pairs = []
            while tokens:
                keyword = tokens.popl()
                values = []
                while tokens:
                    try:
                        try_keyword = re.search(r'([*]?[A-Za-z]+)', tokens.peekl()).group()
                        SourceDefinitionKeyword.from_mcnp(try_keyword)
                        break
                    except Exception:
                        values.append(tokens.popl())
                        pass

                option = SourceDefinitionOption.from_mcnp(f"{keyword}={' '.join(values)}")
                pairs.append(option)
            pairs = tuple(pairs)

            datum = SourceDefinition(pairs)

        case _:
            datum = _Placeholder(mnemonic, [tokens.popl() for _ in range(0, len(tokens))])

    if tokens:
        raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM)

    datum.comment = comments

    return datum
