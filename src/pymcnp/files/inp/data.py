"""
Contains classes representing INP data cards.
"""

import re
from typing import Final, Union  # noqa

from . import _card
from ..utils import types  # noqa
from ..utils import errors
from ..utils import _parser
from ..utils import _elements  # noqa


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


class DataKeyword(_card.CardKeyword):
    """
    Represents INP data card option keywords.

    ``DataKeyword`` extends the ``_card.CawrdKeyword`` abstract class.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError


class DataOption(_card.CardOption):
    """
    Represents INP data cards options.

    ``DataOption`` extends the ``_card.CardOption`` abstract class.

    Attributes:
        keyword: Data card option keyword.
        value: Data card option value.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError


class DataEntry(_card.CardEntry):
    """
    Represents INP data card entry.

    ``DataEntry`` extends the ``_card.CardEntry`` abstract class.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError


class Data(_card.Card):
    """
    Represents INP data cards.

    ``Data`` extends the ``_card.Card`` abstract class.

    Attributes:
        ident: Card identifier.
        line_number: Card line number.
        comment: Card inline comment.
        mnemonic: Data card mnemonics.
        parameters: Data card parameters.
    """

    GEOMETRY_MNEMONICS: Final[tuple[DataMnemonic]] = (
        DataMnemonic.VOLUME,
        DataMnemonic.AREA,
        DataMnemonic.TR,
        # DataMnemonic.TRANSFORMATION_ANGLE,
        DataMnemonic.U,
        DataMnemonic.LAT,
        DataMnemonic.FILL,
        # DataMnemonic.FILL_ANGLE,
        DataMnemonic.URAN,
        DataMnemonic.DM,
        DataMnemonic.DETERMINISTIC_WEIGHT_WINDOW,
        DataMnemonic.EMBED,
        DataMnemonic.EMBEE,
        DataMnemonic.EMBEB,
        DataMnemonic.EMBEM,
        DataMnemonic.EMBTB,
        DataMnemonic.EMBTM,
        DataMnemonic.EMBDB,
        DataMnemonic.EMBDF,
    )

    MATERIAL_MNEMONICS: Final[tuple[DataMnemonic]] = (
        DataMnemonic.M,
        DataMnemonic.MT,
        DataMnemonic.MATERIAL_NUCLIDE_SUBSTITUTION,
        DataMnemonic.OTFDB,
        DataMnemonic.TOTAL_FISSION,
        DataMnemonic.NONU,
        DataMnemonic.AWTAB,
        DataMnemonic.XS,
        DataMnemonic.VOID,
        DataMnemonic.MGOPT,
        DataMnemonic.DRXS,
    )

    PHYSICS_MNEMONICS: Final[tuple[DataMnemonic]] = (
        DataMnemonic.MODE,
        DataMnemonic.PARTICLE_PHYSICS_OPTIONS,
        DataMnemonic.ACT,
        DataMnemonic.CUT,
        DataMnemonic.ELPT,
        DataMnemonic.FREE_GAS_THERMAL_TEMPERATURE,
        DataMnemonic.THTME,
        DataMnemonic.MODEL_PHYSICS_CONTROL,
        DataMnemonic.LCA,
        DataMnemonic.LCB,
        DataMnemonic.LCC,
        DataMnemonic.LEA,
        DataMnemonic.LEB,
        DataMnemonic.FMULT,
        DataMnemonic.TROPT,
        DataMnemonic.UNC,
        DataMnemonic.COSYP,
        DataMnemonic.COSY,
        DataMnemonic.BFLD,
        DataMnemonic.BFLCL,
        DataMnemonic.GRAVITATIONAL_FIELD,
    )

    SOURCE_MNEMONICS: Final[tuple[DataMnemonic]] = (
        DataMnemonic.SDEF,
        DataMnemonic.SOURCE_INFORMATION,
        DataMnemonic.SOURCE_PROBABILITY,
        DataMnemonic.SOURCE_BIAS,
        DataMnemonic.DEPENDENT_SOURCE_DISTRIBUTION,
        DataMnemonic.SC,
        DataMnemonic.SURFACE_SOURCE_WRITE,
        DataMnemonic.SSR,
        DataMnemonic.KCODE,
        DataMnemonic.KSRC,
        DataMnemonic.KOPTS,
        DataMnemonic.HSRC,
        DataMnemonic.DEPLETION_BURNUP,
        DataMnemonic.SOURCE,
        DataMnemonic.SRCDX,
    )

    TALLY_MNEMONICS: Final[tuple[DataMnemonic]] = (
        DataMnemonic.STANDARD_TALLIES,
        DataMnemonic.STANDARD_TALLIES_ANGLE,
        DataMnemonic.FIP,
        DataMnemonic.FIR,
        DataMnemonic.FIC,
        DataMnemonic.TALLY_COMMENT,
        DataMnemonic.TALLY_ENERGY,
        DataMnemonic.TALLY_TIME,
        DataMnemonic.TALLY_COSINE,
        DataMnemonic.TALLY_COSINE_ANGLE,
        DataMnemonic.PRINT_HIERARCHY,
        DataMnemonic.TALLY_MULTIPLIER,
        DataMnemonic.DOSE_ENERGY,
        DataMnemonic.DOSE_FUNCTION,
        DataMnemonic.ENERGY_MULTIPLIER,
        DataMnemonic.TIME_MULTIPLIER,
        DataMnemonic.COSINE_MULTIPLIER,
        DataMnemonic.CELL_FLAGGING,
        DataMnemonic.SURFACE_FLAGGING,
        DataMnemonic.TALLY_SEGMENT,
        DataMnemonic.SEGMENT_DIVISOR,
        DataMnemonic.SPECIAL_TALLY,
        DataMnemonic.TALLYX_SUBROUTINE,
        DataMnemonic.SPECIAL_TREATMENTS_TALLIES,
        DataMnemonic.TALLY_FLUCTUATION,
        DataMnemonic.DIRECT_ONLY_CONTRIBUTIONS,
        DataMnemonic.TALLY_PERTUBATION,
        DataMnemonic.REACTIVITY_PERTUBATIONS,
        DataMnemonic.SENSITIVITY_COEFFICENTS,
        DataMnemonic.SUPERIMPOSED_MESH_TALLY_A,
        DataMnemonic.SUPERIMPOSED_MESH_TALLY_B,
        DataMnemonic.LATTICE_SPEED_TALLY_ENHANCEMENT,
    )

    VARIENCE_MNEMONICS: Final[tuple[DataMnemonic]] = (
        DataMnemonic.IMPORTANCE,
        DataMnemonic.VARIANCE_REDUCATION_CONTROL,
        DataMnemonic.WEIGHT_WINDOW_ENERGIES,
        DataMnemonic.WEIGHT_WINDOW_TIMES,
        DataMnemonic.WEIGHT_WINDOW_BOUNDS,
        DataMnemonic.WEIGHT_WINDOW_PARAMETER,
        DataMnemonic.WEIGHT_WINDOW_GENERATION,
        DataMnemonic.WEIGHT_WINDOW_GENERATION_ENERGIES,
        DataMnemonic.WEIGHT_WINDOW_GENERATION_TIMES,
        DataMnemonic.SUPERIMPOSED_IMPORTANCE_MESH,
        DataMnemonic.ENERGY_SPLITTING,
        DataMnemonic.TIME_SPLITTING,
        DataMnemonic.EXPONENTIAL_TRANSFORM,
        DataMnemonic.VECTOR_INPUT,
        DataMnemonic.FORCED_COLLISION,
        DataMnemonic.DXTRAN_SPHERE,
        DataMnemonic.DETECTOR_DIAGNOSTICS,
        DataMnemonic.DETECTOR_CONTRIBUTION,
        DataMnemonic.DXTRAN_CONTRIBUTION,
        DataMnemonic.BREMSSTRAHLUNG_BIASING,
        DataMnemonic.PHOTON_PRODUDCTION_BIASING,
        DataMnemonic.SECONDARY_PARTICLE_BIASING,
        DataMnemonic.PHOTON_WEIGHT,
    )

    MICELLANEOUS_MNEMONICS: Final[tuple[DataMnemonic]] = (
        DataMnemonic.NPS,
        DataMnemonic.COMPUTER_TIME_CUTOFF,
        DataMnemonic.PERCISION_CUTOFF,
        DataMnemonic.OUPUT_PRINT_TABLES,
        DataMnemonic.NEGATE_PRINTING_TALLIES,
        DataMnemonic.PRINT_DUMP_CYCLES,
        DataMnemonic.PARTICLE_TRACK_OUTPUT,
        DataMnemonic.PLOT_TALLIES_WHITE_RUNNING,
        DataMnemonic.CREATE_LAHET,
        DataMnemonic.RAND,
        DataMnemonic.DEBUG_INFORMATION,
        DataMnemonic.LOST_PARTICLE_CONTROL,
        DataMnemonic.INTEGER_ARRAY,
        DataMnemonic.FLOATINGPOINT_ARRAY,
        DataMnemonic.ZA,
        DataMnemonic.ZB,
        DataMnemonic.ZC,
        DataMnemonic.ZD,
        DataMnemonic.FILE,
    )

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        raise NotImplementedError


class _Placeholder(Data):
    """Placeholder for F8, FT8, etc."""

    def __init__(self, mnemonic: DataMnemonic, parameters: tuple[any]):
        self.ident = mnemonic
        self.mnemonic = mnemonic
        self.parameters = parameters

    @staticmethod
    def from_mcnp(source: str):
        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            re.split(r' |=', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        mnemonic = tokens.popl()
        parameters = tuple([tokens.popl() for _ in range(0, len(tokens))])

        data = _Placeholder(mnemonic, parameters)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        return f"{self.mnemonic} {' '.join(self.parameters)}"
