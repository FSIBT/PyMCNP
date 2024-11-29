"""
Contains classes representing INP data card mnemonics.
"""

from . import _card
from ..utils import errors
from ..utils import _parser


class DataMnemonic(_card.CardMnemonic):
    """
    Represents INP data card mnemonics.

    ``DataMnemonic`` implements ``_card.CardMnemonic``.
    """

    # Fully Implemented
    AREA = 'area'
    TR = 'tr'
    U = 'u'
    LAT = 'lat'
    FILL = 'fill'
    URAN = 'uran'
    DM = 'dm'
    EMBED = 'embed'
    EMBEE = 'embee'
    EMBEB = 'embeb'
    EMBEM = 'embem'
    EMBTB = 'embtb'
    EMBTM = 'embtm'
    EMBDB = 'embdb'
    EMBDF = 'embdf'
    M = 'm'
    MT = 'mt'
    OTFDB = 'otfdb'
    NONU = 'nonu'
    AWTAB = 'awtab'
    XS = 'xs'
    VOID = 'void'
    MGOPT = 'mgopt'
    DRXS = 'drxs'
    MODE = 'mode'
    ACT = 'act'
    CUT = 'cut'
    ELPT = 'elpt'
    THTME = 'thtme'
    LCA = 'lca'
    LCB = 'lcb'
    LCC = 'lcc'
    LEA = 'lea'
    LEB = 'leb'
    FMULT = 'fmult'
    TROPT = 'tropt'
    UNC = 'unc'
    COSYP = 'cosyp'
    COSY = 'cosy'
    BFLD = 'bfld'
    BFLCL = 'bflcl'
    SDEF = 'sdef'
    SC = 'sc'
    SSR = 'ssr'
    KCODE = 'kcode'
    KSRC = 'ksrc'
    KOPTS = 'kopts'
    HSRC = 'hsrc'
    NPS = 'nps'
    RAND = 'rand'

    # I'm Working on It! :)
    VOLUME = 'vol'
    TRANSFORMATION_ANGLE = '*tr'
    FILL_ANGLE = 'fill'
    DETERMINISTIC_WEIGHT_WINDOW = 'dawwg'
    MATERIAL_NUCLIDE_SUBSTITUTION = 'mx'
    TOTAL_FISSION = 'totnu'
    PARTICLE_PHYSICS_OPTIONS = 'phys'
    FREE_GAS_THERMAL_TEMPERATURE = 'tmp'
    CELL_ENERGY_CUTOFFS = 'elpt'
    MODEL_PHYSICS_CONTROL = 'mphys'
    GRAVITATIONAL_FIELD = 'field'
    SOURCE_INFORMATION = 'si'
    SOURCE_PROBABILITY = 'sp'
    SOURCE_BIAS = 'sb'
    DEPENDENT_SOURCE_DISTRIBUTION = 'ds'
    SURFACE_SOURCE_WRITE = 'ssw'
    DEPLETION_BURNUP = 'burn'
    SOURCE = 'source'
    SRCDX = 'srdx'
    STANDARD_TALLIES = 'f'
    STANDARD_TALLIES_ANGLE = '*f'
    FIP = 'fip'
    FIR = 'fir'
    FIC = 'fic'
    TALLY_COMMENT = 'fc'
    TALLY_ENERGY = 'e'
    TALLY_TIME = 't'
    TALLY_COSINE = 'c'
    TALLY_COSINE_ANGLE = '*c'
    PRINT_HIERARCHY = 'fq'
    TALLY_MULTIPLIER = 'fm'
    DOSE_ENERGY = 'de'
    DOSE_FUNCTION = 'df'
    ENERGY_MULTIPLIER = 'em'
    TIME_MULTIPLIER = 'tm'
    COSINE_MULTIPLIER = 'cm'
    CELL_FLAGGING = 'cf'
    SURFACE_FLAGGING = 'sf'
    TALLY_SEGMENT = 'fs'
    SEGMENT_DIVISOR = 'sd'
    SPECIAL_TALLY = 'fu'
    TALLYX_SUBROUTINE = 'tallyx'
    SPECIAL_TREATMENTS_TALLIES = 'ft'
    TALLY_FLUCTUATION = 'tf'
    DIRECT_ONLY_CONTRIBUTIONS = 'notrn'
    TALLY_PERTUBATION = 'pert'
    REACTIVITY_PERTUBATIONS = 'kpert'
    SENSITIVITY_COEFFICENTS = 'ksen'
    SUPERIMPOSED_MESH_TALLY_A = 'tmesh'
    SUPERIMPOSED_MESH_TALLY_B = 'fmesh'
    LATTICE_SPEED_TALLY_ENHANCEMENT = 'spdtl'
    IMPORTANCE = 'imp'
    VARIANCE_REDUCATION_CONTROL = 'var'
    WEIGHT_WINDOW_ENERGIES = 'wwe'
    WEIGHT_WINDOW_TIMES = 'wwt'
    WEIGHT_WINDOW_BOUNDS = 'wwn'
    WEIGHT_WINDOW_PARAMETER = 'wwp'
    WEIGHT_WINDOW_GENERATION = 'wwg'
    WEIGHT_WINDOW_GENERATION_ENERGIES = 'wwge'
    WEIGHT_WINDOW_GENERATION_TIMES = 'wwgt'
    SUPERIMPOSED_IMPORTANCE_MESH = 'mesh'
    ENERGY_SPLITTING = 'esplt'
    TIME_SPLITTING = 'tsplt'
    EXPONENTIAL_TRANSFORM = 'ext'
    VECTOR_INPUT = 'vect'
    FORCED_COLLISION = 'fcl'
    DXTRAN_SPHERE = 'dxt'
    DETECTOR_DIAGNOSTICS = 'dd'
    DETECTOR_CONTRIBUTION = 'pd'
    DXTRAN_CONTRIBUTION = 'dxc'
    BREMSSTRAHLUNG_BIASING = 'bbrem'
    PHOTON_PRODUDCTION_BIASING = 'pikmt'
    SECONDARY_PARTICLE_BIASING = 'spabi'
    PHOTON_WEIGHT = 'pwt'
    COMPUTER_TIME_CUTOFF = 'ctme'
    PERCISION_CUTOFF = 'stop'
    OUPUT_PRINT_TABLES = 'print'
    NEGATE_PRINTING_TALLIES = 'talnp'
    PRINT_DUMP_CYCLES = 'prdmp'
    PARTICLE_TRACK_OUTPUT = 'ptrac'
    PLOT_TALLIES_WHITE_RUNNING = 'mplot'
    CREATE_LAHET = 'histp'
    DEBUG_INFORMATION = 'dbcn'
    LOST_PARTICLE_CONTROL = 'lost'
    INTEGER_ARRAY = 'idum'
    FLOATINGPOINT_ARRAY = 'rdum'
    ZA = 'za'
    ZB = 'zb'
    ZC = 'zc'
    ZD = 'zd'
    FILE = 'files'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates PyMCNP ``DataMnemonic`` from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``DataMnemonic``.

        Returns:
            ``DataMnemonic``.

        Raises:
            McnpError: INVALID_DATUM_MNEMONIC.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return DataMnemonic(source)
        except ValueError:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_MNEMONIC)
