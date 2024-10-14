"""
``test_datum`` tests the ``pymcnp.inp.datum`` module.
"""


import pytest
import hypothesis as hy
import hypothesis.strategies as st

import _config
import test_types
from pymcnp.files.inp.datum import Datum
from pymcnp.files.utils import errors
from pymcnp.files.utils import types


@st.composite
def datum_mnemonic(draw, valid) -> str:
    """
    ``datum_mnemonic`` generates ``DatumMnemonic`` parameters.

    Parameters:
        valid: Validity setting.

    Returns:
        Valid/Invalid ``DatumMnemonic`` parameters.
    """

    MNEMONICS = {
        "vol",
        "area",
        "tr",
        "*tr",
        "u",
        "lat",
        "fill",
        "*fill",
        "uran",
        "dm",
        "dawwg",
        "embed",
        "embee",
        "embeb",
        "embem",
        "embtb",
        "embtm",
        "embde",
        "embdf",
        "m",
        "mt",
        "mx",
        "otfdb",
        "totnu",
        "nonu",
        "awtab",
        "xs",
        "void",
        "mgopt",
        "drxs",
        "mode",
        "phys",
        "act",
        "cut",
        "elpt",
        "tmp",
        "thtme",
        "mphys",
        "lca",
        "lcb",
        "lcc",
        "lea",
        "leb",
        "fmult",
        "tropt",
        "unc",
        "cosyp",
        "cosy",
        "bfld",
        "bflcl",
        "field",
        "sdef",
        "si",
        "sp",
        "sb",
        "ds",
        "sc",
        "ssw",
        "ssr",
        "kcode",
        "ksrc",
        "kopts",
        "hsrc",
        "burn",
        "source",
        "srdx",
        "f",
        "*f",
        "fip",
        "fir",
        "fic",
        "fc",
        "e",
        "t",
        "c",
        "*c",
        "fq",
        "em",
        "de",
        "df",
        "em",
        "tm",
        "cm",
        "cf",
        "sf",
        "fs",
        "sd",
        "fu",
        "tallyx",
        "ft",
        "tf",
        "notrn",
        "pert",
        "kpert",
        "ksen",
        "tmesh",
        "fmesh",
        "spdtl",
        "imp",
        "var",
        "wwe",
        "wwt",
        "wwn",
        "wwp",
        "wwg",
        "wwge",
        "wwgt",
        "mesh",
        "esplt",
        "tsplt",
        "ext",
        "vect",
        "fcl",
        "dxt",
        "dd",
        "pd",
        "dxc",
        "bbrem",
        "pikmt",
        "spabi",
        "pwt",
        "nps",
        "ctme",
        "stop",
        "print",
        "talnp",
        "prdmp",
        "ptrac",
        "mplot",
        "histp",
        "rand",
        "dbcn",
        "lost",
        "idum",
        "rdum",
        "za",
        "zb",
        "zc",
        "zd",
        "files",
    }

    if valid:
        return draw(st.samplefrom(MNEMONICS))
    else:
        return draw(st.text().filter(lambda s: s.lower() not in MNEMONICS))


def format_datum_mnemonic(mnemonic: str):
    """
    ``format_datum_mnemonic``
    """

    return mnemonic


class Test_DatumMnemonic:
    """
    ``Test_DatumMnemonic`` tests ``DatumMnemonic``.
    """

    class Test_Init:
        """
        ``Test_Init`` tests ``DatumMnemonic.__init__``.
        """

        def test_valid(self):
            """
            ``test_valid`` checks valid inputs work.
            """

            assert Datum.DatumMnemonic("vol") == Datum.DatumMnemonic.VOLUME
            assert Datum.DatumMnemonic("area") == Datum.DatumMnemonic.AREA
            assert Datum.DatumMnemonic("tr") == Datum.DatumMnemonic.TRANSFORMATION
            assert Datum.DatumMnemonic("*tr") == Datum.DatumMnemonic.TRANSFORMATION_ANGLE
            assert Datum.DatumMnemonic("u") == Datum.DatumMnemonic.UNIVERSE
            assert Datum.DatumMnemonic("lat") == Datum.DatumMnemonic.LATTICE
            assert Datum.DatumMnemonic("fill") == Datum.DatumMnemonic.FILL
            assert Datum.DatumMnemonic("*fill") == Datum.DatumMnemonic.FILL_ANGLE
            assert Datum.DatumMnemonic("uran") == Datum.DatumMnemonic.STOCHASTIC_GEOMETRY
            assert Datum.DatumMnemonic("dm") == Datum.DatumMnemonic.DETERMINISTIC_MATERIALS
            assert Datum.DatumMnemonic("dawwg") == Datum.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW
            assert Datum.DatumMnemonic("embed") == Datum.DatumMnemonic.EMBEDDED_GEOMETRY
            assert Datum.DatumMnemonic("embee") == Datum.DatumMnemonic.EMBEDDED_CONTROL
            assert Datum.DatumMnemonic("embeb") == Datum.DatumMnemonic.EMBEDDED_ENERGY_BOUNDARIES
            assert Datum.DatumMnemonic("embem") == Datum.DatumMnemonic.EMBEDDED_ENERGY_MULTIPLIERS
            assert Datum.DatumMnemonic("embtb") == Datum.DatumMnemonic.EMBEDDED_TIME_BOUNDARIES
            assert Datum.DatumMnemonic("embtm") == Datum.DatumMnemonic.EMBEDDED_TIME_MULTIPLIERS
            assert Datum.DatumMnemonic("embde") == Datum.DatumMnemonic.EMBEDDED_DOSE_BOUNDARIES
            assert Datum.DatumMnemonic("embdf") == Datum.DatumMnemonic.EMBEDDED_DOSE_MULTIPLIERS
            assert Datum.DatumMnemonic("m") == Datum.DatumMnemonic.MATERIAL
            assert Datum.DatumMnemonic("mt") == Datum.DatumMnemonic.MATERIAL_NEUTRON_SCATTERING
            assert Datum.DatumMnemonic("mx") == Datum.DatumMnemonic.MATERIAL_NUCLIDE_SUBSTITUTION
            assert Datum.DatumMnemonic("otfdb") == Datum.DatumMnemonic.ON_THE_FLY_BROADENING
            assert Datum.DatumMnemonic("totnu") == Datum.DatumMnemonic.TOTAL_FISSION
            assert Datum.DatumMnemonic("nonu") == Datum.DatumMnemonic.FISSION_TURNOFF
            assert Datum.DatumMnemonic("awtab") == Datum.DatumMnemonic.ATOMIC_WEIGHT
            assert Datum.DatumMnemonic("xs") == Datum.DatumMnemonic.CROSS_SECTION_FILE
            assert Datum.DatumMnemonic("void") == Datum.DatumMnemonic.VOID
            assert Datum.DatumMnemonic("mgopt") == Datum.DatumMnemonic.MULTIGROUP_ADJOINT_TRANSPORT
            assert Datum.DatumMnemonic("drxs") == Datum.DatumMnemonic.DISCRETE_REACTION_CROSS_SECTION
            assert Datum.DatumMnemonic("mode") == Datum.DatumMnemonic.PROBLEM_TYPE
            assert Datum.DatumMnemonic("phys") == Datum.DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
            assert Datum.DatumMnemonic("act") == Datum.DatumMnemonic.ACTIVATION_CONTROL
            assert Datum.DatumMnemonic("cut") == Datum.DatumMnemonic.TIME_ENERGY_WEIGHT_CUTOFFS
            assert Datum.DatumMnemonic("elpt") == Datum.DatumMnemonic.CELL_ENERGY_CUTOFFS
            assert Datum.DatumMnemonic("tmp") == Datum.DatumMnemonic.FREE_GAS_THERMAL_TEMPERATURE
            assert Datum.DatumMnemonic("thtme") == Datum.DatumMnemonic.THERMAL_TIMES
            assert Datum.DatumMnemonic("mphys") == Datum.DatumMnemonic.MODEL_PHYSICS_CONTROL
            assert Datum.DatumMnemonic("lca") == Datum.DatumMnemonic.LCA
            assert Datum.DatumMnemonic("lcb") == Datum.DatumMnemonic.LCB
            assert Datum.DatumMnemonic("lcc") == Datum.DatumMnemonic.LCC
            assert Datum.DatumMnemonic("lea") == Datum.DatumMnemonic.LEA
            assert Datum.DatumMnemonic("leb") == Datum.DatumMnemonic.LEB
            assert Datum.DatumMnemonic("fmult") == Datum.DatumMnemonic.MULTIPLICITY_CONSTANTS
            assert Datum.DatumMnemonic("tropt") == Datum.DatumMnemonic.TRANSPORT_OPTIONS
            assert Datum.DatumMnemonic("unc") == Datum.DatumMnemonic.UNCOLLIDED_SECONDARIES
            assert Datum.DatumMnemonic("cosyp") == Datum.DatumMnemonic.COSYP
            assert Datum.DatumMnemonic("cosy") == Datum.DatumMnemonic.COSY
            assert Datum.DatumMnemonic("bfld") == Datum.DatumMnemonic.BFLD
            assert Datum.DatumMnemonic("bflcl") == Datum.DatumMnemonic.BFLCL
            assert Datum.DatumMnemonic("field") == Datum.DatumMnemonic.GRAVITATIONAL_FIELD
            assert Datum.DatumMnemonic("sdef") == Datum.DatumMnemonic.GENERAL_SOURCE_DEFINITION
            assert Datum.DatumMnemonic("si") == Datum.DatumMnemonic.SOURCE_INFORMATION
            assert Datum.DatumMnemonic("sp") == Datum.DatumMnemonic.SOURCE_PROBABILITY
            assert Datum.DatumMnemonic("sb") == Datum.DatumMnemonic.SOURCE_BIAS
            assert Datum.DatumMnemonic("ds") == Datum.DatumMnemonic.DEPENDENT_SOURCE_DISTRIBUTION
            assert Datum.DatumMnemonic("sc") == Datum.DatumMnemonic.SOURCE_COMMENT
            assert Datum.DatumMnemonic("ssw") == Datum.DatumMnemonic.SURFACE_SOURCE_WRITE
            assert Datum.DatumMnemonic("ssr") == Datum.DatumMnemonic.SURFACE_SOURCE_READ
            assert Datum.DatumMnemonic("kcode") == Datum.DatumMnemonic.CRITICALITY_SOURCE
            assert Datum.DatumMnemonic("ksrc") == Datum.DatumMnemonic.CRITICALITY_SOURCE_POINTS
            assert Datum.DatumMnemonic("kopts") == Datum.DatumMnemonic.CRITICALITY_CALCULIATION_OPTIONS
            assert Datum.DatumMnemonic("hsrc") == Datum.DatumMnemonic.ENTROPY_SOURCE_DISTRIBUTION
            assert Datum.DatumMnemonic("burn") == Datum.DatumMnemonic.DEPLETION_BURNUP
            assert Datum.DatumMnemonic("source") == Datum.DatumMnemonic.SOURCE
            assert Datum.DatumMnemonic("srdx") == Datum.DatumMnemonic.SRCDX
            assert Datum.DatumMnemonic("f") == Datum.DatumMnemonic.STANDARD_TALLIES
            assert Datum.DatumMnemonic("*f") == Datum.DatumMnemonic.STANDARD_TALLIES_ANGLE
            assert Datum.DatumMnemonic("fip") == Datum.DatumMnemonic.FIP
            assert Datum.DatumMnemonic("fir") == Datum.DatumMnemonic.FIR
            assert Datum.DatumMnemonic("fic") == Datum.DatumMnemonic.FIC
            assert Datum.DatumMnemonic("fc") == Datum.DatumMnemonic.TALLY_COMMENT
            assert Datum.DatumMnemonic("e") == Datum.DatumMnemonic.TALLY_ENERGY
            assert Datum.DatumMnemonic("t") == Datum.DatumMnemonic.TALLY_TIME
            assert Datum.DatumMnemonic("c") == Datum.DatumMnemonic.TALLY_COSINE
            assert Datum.DatumMnemonic("*c") == Datum.DatumMnemonic.TALLY_COSINE_ANGLE
            assert Datum.DatumMnemonic("fq") == Datum.DatumMnemonic.PRINT_HIERARCHY
            assert Datum.DatumMnemonic("em") == Datum.DatumMnemonic.TALLY_MULTIPLIER
            assert Datum.DatumMnemonic("de") == Datum.DatumMnemonic.DOSE_ENERGY
            assert Datum.DatumMnemonic("df") == Datum.DatumMnemonic.DOSE_FUNCTION
            assert Datum.DatumMnemonic("em") == Datum.DatumMnemonic.ENERGY_MULTIPLIER
            assert Datum.DatumMnemonic("tm") == Datum.DatumMnemonic.TIME_MULTIPLIER
            assert Datum.DatumMnemonic("cm") == Datum.DatumMnemonic.COSINE_MULTIPLIER
            assert Datum.DatumMnemonic("cf") == Datum.DatumMnemonic.CELL_FLAGGING
            assert Datum.DatumMnemonic("sf") == Datum.DatumMnemonic.SURFACE_FLAGGING
            assert Datum.DatumMnemonic("fs") == Datum.DatumMnemonic.TALLY_SEGMENT
            assert Datum.DatumMnemonic("sd") == Datum.DatumMnemonic.SEGMENT_DIVISOR
            assert Datum.DatumMnemonic("fu") == Datum.DatumMnemonic.SPECIAL_TALLY
            assert Datum.DatumMnemonic("tallyx") == Datum.DatumMnemonic.TALLYX_SUBROUTINE
            assert Datum.DatumMnemonic("ft") == Datum.DatumMnemonic.SPECIAL_TREATMENTS_TALLIES
            assert Datum.DatumMnemonic("tf") == Datum.DatumMnemonic.TALLY_FLUCTUATION
            assert Datum.DatumMnemonic("notrn") == Datum.DatumMnemonic.DIRECT_ONLY_CONTRIBUTIONS
            assert Datum.DatumMnemonic("pert") == Datum.DatumMnemonic.TALLY_PERTUBATION
            assert Datum.DatumMnemonic("kpert") == Datum.DatumMnemonic.REACTIVITY_PERTUBATIONS
            assert Datum.DatumMnemonic("ksen") == Datum.DatumMnemonic.SENSITIVITY_COEFFICENTS
            assert Datum.DatumMnemonic("tmesh") == Datum.DatumMnemonic.SUPERIMPOSED_MESH_TALLY_A
            assert Datum.DatumMnemonic("fmesh") == Datum.DatumMnemonic.SUPERIMPOSED_MESH_TALLY_B
            assert Datum.DatumMnemonic("spdtl") == Datum.DatumMnemonic.LATTICE_SPEED_TALLY_ENHANCEMENT
            assert Datum.DatumMnemonic("imp") == Datum.DatumMnemonic.IMPORTANCE
            assert Datum.DatumMnemonic("var") == Datum.DatumMnemonic.VARIANCE_REDUCATION_CONTROL
            assert Datum.DatumMnemonic("wwe") == Datum.DatumMnemonic.WEIGHT_WINDOW_ENERGIES
            assert Datum.DatumMnemonic("wwt") == Datum.DatumMnemonic.WEIGHT_WINDOW_TIMES
            assert Datum.DatumMnemonic("wwn") == Datum.DatumMnemonic.WEIGHT_WINDOW_BOUNDS
            assert Datum.DatumMnemonic("wwp") == Datum.DatumMnemonic.WEIGHT_WINDOW_PARAMETER
            assert Datum.DatumMnemonic("wwg") == Datum.DatumMnemonic.WEIGHT_WINDOW_GENERATION
            assert Datum.DatumMnemonic("wwge") == Datum.DatumMnemonic.WEIGHT_WINDOW_GENERATION_ENERGIES
            assert Datum.DatumMnemonic("wwgt") == Datum.DatumMnemonic.WEIGHT_WINDOW_GENERATION_TIMES
            assert Datum.DatumMnemonic("mesh") == Datum.DatumMnemonic.SUPERIMPOSED_IMPORTANCE_MESH
            assert Datum.DatumMnemonic("esplt") == Datum.DatumMnemonic.ENERGY_SPLITTING
            assert Datum.DatumMnemonic("tsplt") == Datum.DatumMnemonic.TIME_SPLITTING
            assert Datum.DatumMnemonic("ext") == Datum.DatumMnemonic.EXPONENTIAL_TRANSFORM
            assert Datum.DatumMnemonic("vect") == Datum.DatumMnemonic.VECTOR_INPUT
            assert Datum.DatumMnemonic("fcl") == Datum.DatumMnemonic.FORCED_COLLISION
            assert Datum.DatumMnemonic("dxt") == Datum.DatumMnemonic.DXTRAN_SPHERE
            assert Datum.DatumMnemonic("dd") == Datum.DatumMnemonic.DETECTOR_DIAGNOSTICS
            assert Datum.DatumMnemonic("pd") == Datum.DatumMnemonic.DETECTOR_CONTRIBUTION
            assert Datum.DatumMnemonic("dxc") == Datum.DatumMnemonic.DXTRAN_CONTRIBUTION
            assert Datum.DatumMnemonic("bbrem") == Datum.DatumMnemonic.BREMSSTRAHLUNG_BIASING
            assert Datum.DatumMnemonic("pikmt") == Datum.DatumMnemonic.PHOTON_PRODUDCTION_BIASING
            assert Datum.DatumMnemonic("spabi") == Datum.DatumMnemonic.SECONDARY_PARTICLE_BIASING
            assert Datum.DatumMnemonic("pwt") == Datum.DatumMnemonic.PHOTON_WEIGHT
            assert Datum.DatumMnemonic("nps") == Datum.DatumMnemonic.HISTORY_CUTOFF
            assert Datum.DatumMnemonic("ctme") == Datum.DatumMnemonic.COMPUTER_TIME_CUTOFF
            assert Datum.DatumMnemonic("stop") == Datum.DatumMnemonic.PERCISION_CUTOFF
            assert Datum.DatumMnemonic("print") == Datum.DatumMnemonic.OUPUT_PRINT_TABLES
            assert Datum.DatumMnemonic("talnp") == Datum.DatumMnemonic.NEGATE_PRINTING_TALLIES
            assert Datum.DatumMnemonic("prdmp") == Datum.DatumMnemonic.PRINT_DUMP_CYCLES
            assert Datum.DatumMnemonic("ptrac") == Datum.DatumMnemonic.PARTICLE_TRACK_OUTPUT
            assert Datum.DatumMnemonic("mplot") == Datum.DatumMnemonic.PLOT_TALLIES_WHITE_RUNNING
            assert Datum.DatumMnemonic("histp") == Datum.DatumMnemonic.CREATE_LAHET
            assert Datum.DatumMnemonic("rand") == Datum.DatumMnemonic.RANDOM
            assert Datum.DatumMnemonic("dbcn") == Datum.DatumMnemonic.DEBUG_INFORMATION
            assert Datum.DatumMnemonic("lost") == Datum.DatumMnemonic.LOST_PARTICLE_CONTROL
            assert Datum.DatumMnemonic("idum") == Datum.DatumMnemonic.INTEGER_ARRAY
            assert Datum.DatumMnemonic("rdum") == Datum.DatumMnemonic.FLOATINGPOINT_ARRAY
            assert Datum.DatumMnemonic("za") == Datum.DatumMnemonic.ZA
            assert Datum.DatumMnemonic("zb") == Datum.DatumMnemonic.ZB
            assert Datum.DatumMnemonic("zc") == Datum.DatumMnemonic.ZC
            assert Datum.DatumMnemonic("zd") == Datum.DatumMnemonic.ZD
            assert Datum.DatumMnemonic("files") == Datum.DatumMnemonic.FILE

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(mnemonic=datum_mnemonic(False))
        def test_invalid(self, mnemonic: str):
            """
            ``test_invalid`` checks invalid inputs raise error.
            """

            with pytest.raises(ValueError) as err:
                Datum.DatumMnemonic(mnemonic)

    class Test_FromMncp:
        """
        ``Test_FromMncp`` tests ``DatumMnemonic.from_mcnp``.
        """

        def test_valid(self):
            """
            ``test_valid`` checks valid inputs work.
            """

            assert Datum.DatumMnemonic.from_mcnp("vol") == Datum.DatumMnemonic.VOLUME
            assert Datum.DatumMnemonic.from_mcnp("area") == Datum.DatumMnemonic.AREA
            assert Datum.DatumMnemonic.from_mcnp("tr") == Datum.DatumMnemonic.TRANSFORMATION
            assert Datum.DatumMnemonic.from_mcnp("*tr") == Datum.DatumMnemonic.TRANSFORMATION_ANGLE
            assert Datum.DatumMnemonic.from_mcnp("u") == Datum.DatumMnemonic.UNIVERSE
            assert Datum.DatumMnemonic.from_mcnp("lat") == Datum.DatumMnemonic.LATTICE
            assert Datum.DatumMnemonic.from_mcnp("fill") == Datum.DatumMnemonic.FILL
            assert Datum.DatumMnemonic.from_mcnp("*fill") == Datum.DatumMnemonic.FILL_ANGLE
            assert Datum.DatumMnemonic.from_mcnp("uran") == Datum.DatumMnemonic.STOCHASTIC_GEOMETRY
            assert Datum.DatumMnemonic.from_mcnp("dm") == Datum.DatumMnemonic.DETERMINISTIC_MATERIALS
            assert Datum.DatumMnemonic.from_mcnp("dawwg") == Datum.DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW
            assert Datum.DatumMnemonic.from_mcnp("embed") == Datum.DatumMnemonic.EMBEDDED_GEOMETRY
            assert Datum.DatumMnemonic.from_mcnp("embee") == Datum.DatumMnemonic.EMBEDDED_CONTROL
            assert Datum.DatumMnemonic.from_mcnp("embeb") == Datum.DatumMnemonic.EMBEDDED_ENERGY_BOUNDARIES
            assert Datum.DatumMnemonic.from_mcnp("embem") == Datum.DatumMnemonic.EMBEDDED_ENERGY_MULTIPLIERS
            assert Datum.DatumMnemonic.from_mcnp("embtb") == Datum.DatumMnemonic.EMBEDDED_TIME_BOUNDARIES
            assert Datum.DatumMnemonic.from_mcnp("embtm") == Datum.DatumMnemonic.EMBEDDED_TIME_MULTIPLIERS
            assert Datum.DatumMnemonic.from_mcnp("embde") == Datum.DatumMnemonic.EMBEDDED_DOSE_BOUNDARIES
            assert Datum.DatumMnemonic.from_mcnp("embdf") == Datum.DatumMnemonic.EMBEDDED_DOSE_MULTIPLIERS
            assert Datum.DatumMnemonic.from_mcnp("m") == Datum.DatumMnemonic.MATERIAL
            assert Datum.DatumMnemonic.from_mcnp("mt") == Datum.DatumMnemonic.MATERIAL_NEUTRON_SCATTERING
            assert Datum.DatumMnemonic.from_mcnp("mx") == Datum.DatumMnemonic.MATERIAL_NUCLIDE_SUBSTITUTION
            assert Datum.DatumMnemonic.from_mcnp("otfdb") == Datum.DatumMnemonic.ON_THE_FLY_BROADENING
            assert Datum.DatumMnemonic.from_mcnp("totnu") == Datum.DatumMnemonic.TOTAL_FISSION
            assert Datum.DatumMnemonic.from_mcnp("nonu") == Datum.DatumMnemonic.FISSION_TURNOFF
            assert Datum.DatumMnemonic.from_mcnp("awtab") == Datum.DatumMnemonic.ATOMIC_WEIGHT
            assert Datum.DatumMnemonic.from_mcnp("xs") == Datum.DatumMnemonic.CROSS_SECTION_FILE
            assert Datum.DatumMnemonic.from_mcnp("void") == Datum.DatumMnemonic.VOID
            assert Datum.DatumMnemonic.from_mcnp("mgopt") == Datum.DatumMnemonic.MULTIGROUP_ADJOINT_TRANSPORT
            assert Datum.DatumMnemonic.from_mcnp("drxs") == Datum.DatumMnemonic.DISCRETE_REACTION_CROSS_SECTION
            assert Datum.DatumMnemonic.from_mcnp("mode") == Datum.DatumMnemonic.PROBLEM_TYPE
            assert Datum.DatumMnemonic.from_mcnp("phys") == Datum.DatumMnemonic.PARTICLE_PHYSICS_OPTIONS
            assert Datum.DatumMnemonic.from_mcnp("act") == Datum.DatumMnemonic.ACTIVATION_CONTROL
            assert Datum.DatumMnemonic.from_mcnp("cut") == Datum.DatumMnemonic.TIME_ENERGY_WEIGHT_CUTOFFS
            assert Datum.DatumMnemonic.from_mcnp("elpt") == Datum.DatumMnemonic.CELL_ENERGY_CUTOFFS
            assert Datum.DatumMnemonic.from_mcnp("tmp") == Datum.DatumMnemonic.FREE_GAS_THERMAL_TEMPERATURE
            assert Datum.DatumMnemonic.from_mcnp("thtme") == Datum.DatumMnemonic.THERMAL_TIMES
            assert Datum.DatumMnemonic.from_mcnp("mphys") == Datum.DatumMnemonic.MODEL_PHYSICS_CONTROL
            assert Datum.DatumMnemonic.from_mcnp("lca") == Datum.DatumMnemonic.LCA
            assert Datum.DatumMnemonic.from_mcnp("lcb") == Datum.DatumMnemonic.LCB
            assert Datum.DatumMnemonic.from_mcnp("lcc") == Datum.DatumMnemonic.LCC
            assert Datum.DatumMnemonic.from_mcnp("lea") == Datum.DatumMnemonic.LEA
            assert Datum.DatumMnemonic.from_mcnp("leb") == Datum.DatumMnemonic.LEB
            assert Datum.DatumMnemonic.from_mcnp("fmult") == Datum.DatumMnemonic.MULTIPLICITY_CONSTANTS
            assert Datum.DatumMnemonic.from_mcnp("tropt") == Datum.DatumMnemonic.TRANSPORT_OPTIONS
            assert Datum.DatumMnemonic.from_mcnp("unc") == Datum.DatumMnemonic.UNCOLLIDED_SECONDARIES
            assert Datum.DatumMnemonic.from_mcnp("cosyp") == Datum.DatumMnemonic.COSYP
            assert Datum.DatumMnemonic.from_mcnp("cosy") == Datum.DatumMnemonic.COSY
            assert Datum.DatumMnemonic.from_mcnp("bfld") == Datum.DatumMnemonic.BFLD
            assert Datum.DatumMnemonic.from_mcnp("bflcl") == Datum.DatumMnemonic.BFLCL
            assert Datum.DatumMnemonic.from_mcnp("field") == Datum.DatumMnemonic.GRAVITATIONAL_FIELD
            assert Datum.DatumMnemonic.from_mcnp("sdef") == Datum.DatumMnemonic.GENERAL_SOURCE_DEFINITION
            assert Datum.DatumMnemonic.from_mcnp("si") == Datum.DatumMnemonic.SOURCE_INFORMATION
            assert Datum.DatumMnemonic.from_mcnp("sp") == Datum.DatumMnemonic.SOURCE_PROBABILITY
            assert Datum.DatumMnemonic.from_mcnp("sb") == Datum.DatumMnemonic.SOURCE_BIAS
            assert Datum.DatumMnemonic.from_mcnp("ds") == Datum.DatumMnemonic.DEPENDENT_SOURCE_DISTRIBUTION
            assert Datum.DatumMnemonic.from_mcnp("sc") == Datum.DatumMnemonic.SOURCE_COMMENT
            assert Datum.DatumMnemonic.from_mcnp("ssw") == Datum.DatumMnemonic.SURFACE_SOURCE_WRITE
            assert Datum.DatumMnemonic.from_mcnp("ssr") == Datum.DatumMnemonic.SURFACE_SOURCE_READ
            assert Datum.DatumMnemonic.from_mcnp("kcode") == Datum.DatumMnemonic.CRITICALITY_SOURCE
            assert Datum.DatumMnemonic.from_mcnp("ksrc") == Datum.DatumMnemonic.CRITICALITY_SOURCE_POINTS
            assert Datum.DatumMnemonic.from_mcnp("kopts") == Datum.DatumMnemonic.CRITICALITY_CALCULIATION_OPTIONS
            assert Datum.DatumMnemonic.from_mcnp("hsrc") == Datum.DatumMnemonic.ENTROPY_SOURCE_DISTRIBUTION
            assert Datum.DatumMnemonic.from_mcnp("burn") == Datum.DatumMnemonic.DEPLETION_BURNUP
            assert Datum.DatumMnemonic.from_mcnp("source") == Datum.DatumMnemonic.SOURCE
            assert Datum.DatumMnemonic.from_mcnp("srdx") == Datum.DatumMnemonic.SRCDX
            assert Datum.DatumMnemonic.from_mcnp("f") == Datum.DatumMnemonic.STANDARD_TALLIES
            assert Datum.DatumMnemonic.from_mcnp("*f") == Datum.DatumMnemonic.STANDARD_TALLIES_ANGLE
            assert Datum.DatumMnemonic.from_mcnp("fip") == Datum.DatumMnemonic.FIP
            assert Datum.DatumMnemonic.from_mcnp("fir") == Datum.DatumMnemonic.FIR
            assert Datum.DatumMnemonic.from_mcnp("fic") == Datum.DatumMnemonic.FIC
            assert Datum.DatumMnemonic.from_mcnp("fc") == Datum.DatumMnemonic.TALLY_COMMENT
            assert Datum.DatumMnemonic.from_mcnp("e") == Datum.DatumMnemonic.TALLY_ENERGY
            assert Datum.DatumMnemonic.from_mcnp("t") == Datum.DatumMnemonic.TALLY_TIME
            assert Datum.DatumMnemonic.from_mcnp("c") == Datum.DatumMnemonic.TALLY_COSINE
            assert Datum.DatumMnemonic.from_mcnp("*c") == Datum.DatumMnemonic.TALLY_COSINE_ANGLE
            assert Datum.DatumMnemonic.from_mcnp("fq") == Datum.DatumMnemonic.PRINT_HIERARCHY
            assert Datum.DatumMnemonic.from_mcnp("em") == Datum.DatumMnemonic.TALLY_MULTIPLIER
            assert Datum.DatumMnemonic.from_mcnp("de") == Datum.DatumMnemonic.DOSE_ENERGY
            assert Datum.DatumMnemonic.from_mcnp("df") == Datum.DatumMnemonic.DOSE_FUNCTION
            assert Datum.DatumMnemonic.from_mcnp("em") == Datum.DatumMnemonic.ENERGY_MULTIPLIER
            assert Datum.DatumMnemonic.from_mcnp("tm") == Datum.DatumMnemonic.TIME_MULTIPLIER
            assert Datum.DatumMnemonic.from_mcnp("cm") == Datum.DatumMnemonic.COSINE_MULTIPLIER
            assert Datum.DatumMnemonic.from_mcnp("cf") == Datum.DatumMnemonic.CELL_FLAGGING
            assert Datum.DatumMnemonic.from_mcnp("sf") == Datum.DatumMnemonic.SURFACE_FLAGGING
            assert Datum.DatumMnemonic.from_mcnp("fs") == Datum.DatumMnemonic.TALLY_SEGMENT
            assert Datum.DatumMnemonic.from_mcnp("sd") == Datum.DatumMnemonic.SEGMENT_DIVISOR
            assert Datum.DatumMnemonic.from_mcnp("fu") == Datum.DatumMnemonic.SPECIAL_TALLY
            assert Datum.DatumMnemonic.from_mcnp("tallyx") == Datum.DatumMnemonic.TALLYX_SUBROUTINE
            assert Datum.DatumMnemonic.from_mcnp("ft") == Datum.DatumMnemonic.SPECIAL_TREATMENTS_TALLIES
            assert Datum.DatumMnemonic.from_mcnp("tf") == Datum.DatumMnemonic.TALLY_FLUCTUATION
            assert Datum.DatumMnemonic.from_mcnp("notrn") == Datum.DatumMnemonic.DIRECT_ONLY_CONTRIBUTIONS
            assert Datum.DatumMnemonic.from_mcnp("pert") == Datum.DatumMnemonic.TALLY_PERTUBATION
            assert Datum.DatumMnemonic.from_mcnp("kpert") == Datum.DatumMnemonic.REACTIVITY_PERTUBATIONS
            assert Datum.DatumMnemonic.from_mcnp("ksen") == Datum.DatumMnemonic.SENSITIVITY_COEFFICENTS
            assert Datum.DatumMnemonic.from_mcnp("tmesh") == Datum.DatumMnemonic.SUPERIMPOSED_MESH_TALLY_A
            assert Datum.DatumMnemonic.from_mcnp("fmesh") == Datum.DatumMnemonic.SUPERIMPOSED_MESH_TALLY_B
            assert Datum.DatumMnemonic.from_mcnp("spdtl") == Datum.DatumMnemonic.LATTICE_SPEED_TALLY_ENHANCEMENT
            assert Datum.DatumMnemonic.from_mcnp("imp") == Datum.DatumMnemonic.IMPORTANCE
            assert Datum.DatumMnemonic.from_mcnp("var") == Datum.DatumMnemonic.VARIANCE_REDUCATION_CONTROL
            assert Datum.DatumMnemonic.from_mcnp("wwe") == Datum.DatumMnemonic.WEIGHT_WINDOW_ENERGIES
            assert Datum.DatumMnemonic.from_mcnp("wwt") == Datum.DatumMnemonic.WEIGHT_WINDOW_TIMES
            assert Datum.DatumMnemonic.from_mcnp("wwn") == Datum.DatumMnemonic.WEIGHT_WINDOW_BOUNDS
            assert Datum.DatumMnemonic.from_mcnp("wwp") == Datum.DatumMnemonic.WEIGHT_WINDOW_PARAMETER
            assert Datum.DatumMnemonic.from_mcnp("wwg") == Datum.DatumMnemonic.WEIGHT_WINDOW_GENERATION
            assert Datum.DatumMnemonic.from_mcnp("wwge") == Datum.DatumMnemonic.WEIGHT_WINDOW_GENERATION_ENERGIES
            assert Datum.DatumMnemonic.from_mcnp("wwgt") == Datum.DatumMnemonic.WEIGHT_WINDOW_GENERATION_TIMES
            assert Datum.DatumMnemonic.from_mcnp("mesh") == Datum.DatumMnemonic.SUPERIMPOSED_IMPORTANCE_MESH
            assert Datum.DatumMnemonic.from_mcnp("esplt") == Datum.DatumMnemonic.ENERGY_SPLITTING
            assert Datum.DatumMnemonic.from_mcnp("tsplt") == Datum.DatumMnemonic.TIME_SPLITTING
            assert Datum.DatumMnemonic.from_mcnp("ext") == Datum.DatumMnemonic.EXPONENTIAL_TRANSFORM
            assert Datum.DatumMnemonic.from_mcnp("vect") == Datum.DatumMnemonic.VECTOR_INPUT
            assert Datum.DatumMnemonic.from_mcnp("fcl") == Datum.DatumMnemonic.FORCED_COLLISION
            assert Datum.DatumMnemonic.from_mcnp("dxt") == Datum.DatumMnemonic.DXTRAN_SPHERE
            assert Datum.DatumMnemonic.from_mcnp("dd") == Datum.DatumMnemonic.DETECTOR_DIAGNOSTICS
            assert Datum.DatumMnemonic.from_mcnp("pd") == Datum.DatumMnemonic.DETECTOR_CONTRIBUTION
            assert Datum.DatumMnemonic.from_mcnp("dxc") == Datum.DatumMnemonic.DXTRAN_CONTRIBUTION
            assert Datum.DatumMnemonic.from_mcnp("bbrem") == Datum.DatumMnemonic.BREMSSTRAHLUNG_BIASING
            assert Datum.DatumMnemonic.from_mcnp("pikmt") == Datum.DatumMnemonic.PHOTON_PRODUDCTION_BIASING
            assert Datum.DatumMnemonic.from_mcnp("spabi") == Datum.DatumMnemonic.SECONDARY_PARTICLE_BIASING
            assert Datum.DatumMnemonic.from_mcnp("pwt") == Datum.DatumMnemonic.PHOTON_WEIGHT
            assert Datum.DatumMnemonic.from_mcnp("nps") == Datum.DatumMnemonic.HISTORY_CUTOFF
            assert Datum.DatumMnemonic.from_mcnp("ctme") == Datum.DatumMnemonic.COMPUTER_TIME_CUTOFF
            assert Datum.DatumMnemonic.from_mcnp("stop") == Datum.DatumMnemonic.PERCISION_CUTOFF
            assert Datum.DatumMnemonic.from_mcnp("print") == Datum.DatumMnemonic.OUPUT_PRINT_TABLES
            assert Datum.DatumMnemonic.from_mcnp("talnp") == Datum.DatumMnemonic.NEGATE_PRINTING_TALLIES
            assert Datum.DatumMnemonic.from_mcnp("prdmp") == Datum.DatumMnemonic.PRINT_DUMP_CYCLES
            assert Datum.DatumMnemonic.from_mcnp("ptrac") == Datum.DatumMnemonic.PARTICLE_TRACK_OUTPUT
            assert Datum.DatumMnemonic.from_mcnp("mplot") == Datum.DatumMnemonic.PLOT_TALLIES_WHITE_RUNNING
            assert Datum.DatumMnemonic.from_mcnp("histp") == Datum.DatumMnemonic.CREATE_LAHET
            assert Datum.DatumMnemonic.from_mcnp("rand") == Datum.DatumMnemonic.RANDOM
            assert Datum.DatumMnemonic.from_mcnp("dbcn") == Datum.DatumMnemonic.DEBUG_INFORMATION
            assert Datum.DatumMnemonic.from_mcnp("lost") == Datum.DatumMnemonic.LOST_PARTICLE_CONTROL
            assert Datum.DatumMnemonic.from_mcnp("idum") == Datum.DatumMnemonic.INTEGER_ARRAY
            assert Datum.DatumMnemonic.from_mcnp("rdum") == Datum.DatumMnemonic.FLOATINGPOINT_ARRAY
            assert Datum.DatumMnemonic.from_mcnp("za") == Datum.DatumMnemonic.ZA
            assert Datum.DatumMnemonic.from_mcnp("zb") == Datum.DatumMnemonic.ZB
            assert Datum.DatumMnemonic.from_mcnp("zc") == Datum.DatumMnemonic.ZC
            assert Datum.DatumMnemonic.from_mcnp("zd") == Datum.DatumMnemonic.ZD
            assert Datum.DatumMnemonic.from_mcnp("files") == Datum.DatumMnemonic.FILE

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(mnemonic=datum_mnemonic(False))
        def test_invalid(self, mnemonic: str):
            """
            ``test_invalid`` checks invalid inputs raise error.
            """

            with pytest.raises(errors.MCNPSemanticError) as err:
                Datum.DatumMnemonic.from_mcnp(mnemonic)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC
