"""
Contains classes representing INP data cards.
"""

import re
from typing import Final, Union  # noqa

from . import _card
from . import _factory
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


_DataAreaFactory = _factory.DataFactory(
    'area',
    False,
    False,
    [
        _factory.AttributeFactory('areas', 'tuple[types.McnpReal]', 'Tuple of surface areas', ''),
    ],
    [],
    [],
)

_DataTrFactory = _factory.DataFactory(
    'tr',
    True,
    False,
    [
        _factory.AttributeFactory(
            'displacement', 'TrDisplacementEntry', 'Tuple for displacement vector', ''
        ),
        _factory.AttributeFactory('rotation', 'TrRotationEntry', 'Tuple for rotation matrix', ''),
        _factory.AttributeFactory(
            'system',
            'types.McnpInteger',
            'Coordinate system setting',
            'system == -1 or system == 1',
        ),
    ],
    [
        _factory.DataEntryFactory(
            'TrDisplacement',
            [
                _factory.AttributeFactory(
                    'x', 'types.McnpReal', 'Displacement vector x component', ''
                ),
                _factory.AttributeFactory(
                    'y', 'types.McnpReal', 'Displacement vector y component', ''
                ),
                _factory.AttributeFactory(
                    'z', 'types.McnpReal', 'Displacement vector z component', ''
                ),
            ],
        ),
        _factory.DataEntryFactory(
            'TrRotation',
            [
                _factory.AttributeFactory(
                    'xx', 'types.McnpReal', "Rotation matrix xx' component", ''
                ),
                _factory.AttributeFactory(
                    'xy', 'types.McnpReal', "Rotation matrix xy' component", ''
                ),
                _factory.AttributeFactory(
                    'xz', 'types.McnpReal', "Rotation matrix xz' component", ''
                ),
                _factory.AttributeFactory(
                    'yx', 'types.McnpReal', "Rotation matrix yx' component", ''
                ),
                _factory.AttributeFactory(
                    'yy', 'types.McnpReal', "Rotation matrix yy' component", ''
                ),
                _factory.AttributeFactory(
                    'yz', 'types.McnpReal', "Rotation matrix yz' component", ''
                ),
                _factory.AttributeFactory(
                    'zx', 'types.McnpReal', "Rotation matrix zx' component", ''
                ),
                _factory.AttributeFactory(
                    'zy', 'types.McnpReal', "Rotation matrix zy' component", ''
                ),
                _factory.AttributeFactory(
                    'zz', 'types.McnpReal', "Rotation matrix zz' component", ''
                ),
            ],
        ),
    ],
    [],
)

_DataUFactory = _factory.DataFactory(
    'u',
    False,
    False,
    [
        _factory.AttributeFactory(
            'numbers',
            'tuple[types.McnpInteger]',
            'Tuple of cell numbers',
            '1 <= entry <= 99_999_999',
        ),
    ],
    [],
    [],
)

_DataLatFactory = _factory.DataFactory(
    'lat',
    False,
    False,
    [
        _factory.AttributeFactory(
            'types',
            'tuple[types.McnpInteger]',
            'Tuple of lattice types',
            'entry == 1 or entry == 2',
        ),
    ],
    [],
    [],
)

_DataFillFactory = _factory.DataFactory(
    'fill',
    False,
    False,
    [
        _factory.AttributeFactory(
            'numbers',
            'tuple[types.McnpInteger]',
            'Tuple of universe numbers',
            '0 <= entry <= 99_999_999',
        ),
    ],
    [],
    [],
)

_DataUranFactory = _factory.DataFactory(
    'uran',
    False,
    False,
    [
        _factory.AttributeFactory(
            'transformations', 'tuple[UranEntry]', 'Tuple of stochastic transformations', ''
        ),
    ],
    [
        _factory.DataEntryFactory(
            'uran',
            [
                _factory.AttributeFactory(
                    'number',
                    'types.McnpInteger',
                    'Universe number for transformation',
                    '0 <= entry <= 99_999_999',
                ),
                _factory.AttributeFactory(
                    'maximum_x', 'types.McnpReal', 'Maximum displacement in the x direction', ''
                ),
                _factory.AttributeFactory(
                    'maximum_y', 'types.McnpReal', 'Maximum displacement in the y direction', ''
                ),
                _factory.AttributeFactory(
                    'maximum_z', 'types.McnpReal', 'Maximum displacement in the z direction', ''
                ),
            ],
        )
    ],
    [],
)

_DataDmFactory = _factory.DataFactory(
    'dm',
    False,
    False,
    [
        _factory.AttributeFactory('zaids', 'tuple[types.Zaid]', 'Tuple of ZAID aliases', ''),
    ],
    [],
    [],
)

_DataEmbedFactory = _factory.DataFactory(
    'embed',
    False,
    False,
    [],
    [],
    [
        _factory.DataOptionFactory(
            'background',
            _factory.AttributeFactory(
                'number',
                'types.McnpInteger',
                'Background pseudo-cell number',
                '1 <= number <= 99_999_999',
            ),
        ),
        _factory.DataOptionFactory(
            'meshgeo',
            _factory.AttributeFactory(
                'form',
                'str',
                'Format specification of the embedded mesh input file',
                'form in {"lnk3dnt", "abaqu", "mcnpum"}',
            ),
        ),
        _factory.DataOptionFactory(
            'mgeoin',
            _factory.AttributeFactory(
                'filename', 'str', 'Name of the input file containing the mesh description', ''
            ),
        ),
        _factory.DataOptionFactory(
            'meeout',
            _factory.AttributeFactory(
                'filename', 'str', 'Name assigned to EEOUT, the elemental edit output file', ''
            ),
        ),
        _factory.DataOptionFactory(
            'meein',
            _factory.AttributeFactory(
                'filename', 'str', 'Name of the EEOUT results file to read', ''
            ),
        ),
        _factory.DataOptionFactory(
            'calcvols',
            _factory.AttributeFactory(
                'setting',
                'str',
                'Yes/no calculate the inferred geometry cell information',
                'setting in {"yes", "no"}',
            ),
        ),
        _factory.DataOptionFactory(
            'debug',
            _factory.AttributeFactory(
                'parameter', 'str', 'Debug parameter', 'parameter in {"echomesh"}'
            ),
        ),
        _factory.DataOptionFactory(
            'filetype',
            _factory.AttributeFactory(
                'kind',
                'str',
                'File type for the elemental edit output file',
                'type in {"ascii", "binary"}',
            ),
        ),
        _factory.DataOptionFactory(
            'gmvfile',
            _factory.AttributeFactory('filename', 'str', 'Name of the GMV output file', ''),
        ),
        _factory.DataOptionFactory(
            'length',
            _factory.AttributeFactory(
                'factor',
                'types.McnpReal',
                'Conversion factor to centimeters for all mesh dimentions',
                'factor > 0',
            ),
        ),
        _factory.DataOptionFactory(
            'mcnpumfile',
            _factory.AttributeFactory('filename', 'str', 'Name of the MCNPUM output file', ''),
        ),
    ],
)

_DataEmbeeFactory = _factory.DataFactory(
    'embee',
    True,
    True,
    [],
    [],
    [
        _factory.DataOptionFactory(
            'embed',
            _factory.AttributeFactory(
                'number',
                'types.McnpInteger',
                'Embedded mesh universe number',
                '0 <= number <= 99_999_999',
            ),
        ),
        _factory.DataOptionFactory(
            'energy',
            _factory.AttributeFactory(
                'factor',
                'types.McnpReal',
                'Multiplicative conversion factor for energy-related output',
                'factor > 0',
            ),
        ),
        _factory.DataOptionFactory(
            'time',
            _factory.AttributeFactory(
                'factor',
                'types.McnpReal',
                'Multiplicative conversion factor for time-related output',
                'factor > 0',
            ),
        ),
        _factory.DataOptionFactory(
            'atom',
            _factory.AttributeFactory(
                'setting', 'str', 'Flag to multiply by atom density', 'setting in {"yes", "no"}'
            ),
        ),
        _factory.DataOptionFactory(
            'factor',
            _factory.AttributeFactory('constant', 'types.McnpReal', 'Multiplicative constant', ''),
        ),
        _factory.DataOptionFactory(
            'mat',
            _factory.AttributeFactory(
                'number', 'types.McnpInteger', 'Material number', '0 <= number <= 99_999_999'
            ),
        ),
        _factory.DataOptionFactory(
            'mtype',
            _factory.AttributeFactory(
                'kind',
                'str',
                'Multiplier type',
                'type in {"flux", "isotropic", "population", "reaction", "source", "track"}',
            ),
        ),
    ],
)

_DataEmbebFactory = _factory.DataFactory(
    'embeb',
    True,
    False,
    [
        _factory.AttributeFactory(
            'bounds', 'tuple[types.McnpReal]', 'Tuple of upper energy bounds', ''
        ),
    ],
    [],
    [],
)

_DataEmbemFactory = _factory.DataFactory(
    'embem',
    True,
    False,
    [
        _factory.AttributeFactory(
            'multipliers', 'tuple[types.McnpReal]', 'Tuple of energy multipliers', ''
        ),
    ],
    [],
    [],
)

_DataEmbtbFactory = _factory.DataFactory(
    'embtb',
    True,
    False,
    [
        _factory.AttributeFactory(
            'bounds', 'tuple[types.McnpReal]', 'Tuple of upper time bounds', ''
        ),
    ],
    [],
    [],
)

_DataEmbtmFactory = _factory.DataFactory(
    'embtm',
    True,
    False,
    [
        _factory.AttributeFactory(
            'multipliers', 'tuple[types.McnpReal]', 'Tuple of time multipliers', ''
        ),
    ],
    [],
    [],
)

_DataEmbdbFactory = _factory.DataFactory(
    'embdb',
    True,
    False,
    [
        _factory.AttributeFactory(
            'bounds', 'tuple[types.McnpReal]', 'Tuple of upper dose energy bounds', ''
        ),
    ],
    [],
    [],
)

_DataEmbdfFactory = _factory.DataFactory(
    'embdf',
    True,
    False,
    [
        _factory.AttributeFactory(
            'multipliers', 'tuple[types.McnpReal]', 'Tuple of dose energy multipliers', ''
        ),
    ],
    [],
    [],
)

_DataMFactory = _factory.DataFactory(
    'm',
    True,
    False,
    [
        _factory.AttributeFactory(
            'substances', 'tuple[MEntry]', 'Tuple of material constituents', ''
        ),
    ],
    [
        _factory.DataEntryFactory(
            'm',
            [
                _factory.AttributeFactory('zaid', 'types.Zaid', 'Substance ZAID alias', ''),
                _factory.AttributeFactory(
                    'fraction', 'types.McnpReal', 'Substance fraction', '-1 >= fraction <= 1'
                ),
            ],
        )
    ],
    [
        _factory.DataOptionFactory(
            'gas',
            _factory.AttributeFactory(
                'setting',
                'str',
                'Flag for density-effect correction to electron stopping power',
                'setting in {"yes", "no"}',
            ),
        ),
        _factory.DataOptionFactory(
            'estep',
            _factory.AttributeFactory(
                'step',
                'types.McnpInteger',
                'Number of electron sub-step per energy step',
                'step >= 0',
            ),
        ),
        _factory.DataOptionFactory(
            'hstep',
            _factory.AttributeFactory(
                'step',
                'types.McnpInteger',
                'Number of proton sub-step per energy step',
                'step >= 0',
            ),
        ),
        _factory.DataOptionFactory(
            'nlib',
            _factory.AttributeFactory('abx', 'str', 'Default neutron table identifier', ''),
        ),
        _factory.DataOptionFactory(
            'plib',
            _factory.AttributeFactory('abx', 'str', 'Default photoatomic table identifier', ''),
        ),
        _factory.DataOptionFactory(
            'pnlib',
            _factory.AttributeFactory('abx', 'str', 'Default photonuclear table identifier', ''),
        ),
        _factory.DataOptionFactory(
            'elib',
            _factory.AttributeFactory('abx', 'str', 'Default electron table identifier', ''),
        ),
        _factory.DataOptionFactory(
            'hlib',
            _factory.AttributeFactory('abx', 'str', 'Default proton table identifier', ''),
        ),
        _factory.DataOptionFactory(
            'alib',
            _factory.AttributeFactory('abx', 'str', 'Default alpha table identifier', ''),
        ),
        _factory.DataOptionFactory(
            'slib',
            _factory.AttributeFactory('abx', 'str', 'Default helion table identifier', ''),
        ),
        _factory.DataOptionFactory(
            'tlib',
            _factory.AttributeFactory('abx', 'str', 'Default triton table identifier', ''),
        ),
        _factory.DataOptionFactory(
            'dlib',
            _factory.AttributeFactory('abx', 'str', 'Default deuteron table identifier', ''),
        ),
        _factory.DataOptionFactory(
            'cond',
            _factory.AttributeFactory(
                'setting',
                'types.McnpReal',
                'Conduction state for EL03 electron-transport evaluation',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'refi',
            _factory.AttributeFactory(
                'refractive_index', 'types.McnpReal', 'Refractive index constant', ''
            ),
        ),
        _factory.DataOptionFactory(
            'refc',
            _factory.AttributeFactory(
                'coefficents', 'tuple[types.McnpReal]', 'Cauchy coefficents', ''
            ),
        ),
        _factory.DataOptionFactory(
            'refs',
            _factory.AttributeFactory(
                'coefficents', 'tuple[types.McnpReal]', 'Sellmeier coefficents', ''
            ),
        ),
    ],
)

_DataMtFactory = _factory.DataFactory(
    'mt',
    True,
    False,
    [
        _factory.AttributeFactory('identifier', 'str', 'Corresponding S(α,β) identifier', ''),
    ],
    [],
    [],
)

_DataOtfdbFactory = _factory.DataFactory(
    'otfdb',
    False,
    False,
    [
        _factory.AttributeFactory(
            'zaids', 'tuple[types.Zaid]', 'Identifiers for the broadening tables', ''
        ),
    ],
    [],
    [],
)

_DataNonuFactory = _factory.DataFactory(
    'nonu',
    False,
    False,
    [
        _factory.AttributeFactory(
            'settings',
            'tuple[types.McnpInteger]',
            'Tuple of fission settings',
            'entry == 0 or entry == 1 or entry == 2',
        ),
    ],
    [],
    [],
)

_DataAwtabFactory = _factory.DataFactory(
    'awtab',
    False,
    False,
    [
        _factory.AttributeFactory(
            'weight_ratios', 'tuple[AwtabEntry]', 'Tuple of atomic weight ratios', ''
        ),
    ],
    [
        _factory.DataEntryFactory(
            'awtab',
            [
                _factory.AttributeFactory('zaid', 'types.Zaid', 'Zaid alias for nuclide', ''),
                _factory.AttributeFactory(
                    'weight_ratio', 'types.McnpReal', 'Atomic weight ratios', 'weight_ratio > 0'
                ),
            ],
        ),
    ],
    [],
)

_DataXsFactory = _factory.DataFactory(
    'xs',
    True,
    False,
    [
        _factory.AttributeFactory(
            'weight_ratios', 'tuple[XsEntry]', 'Tuple of atomic weight ratios', ''
        ),
    ],
    [
        _factory.DataEntryFactory(
            'xs',
            [
                _factory.AttributeFactory('zaid', 'types.Zaid', 'Zaid alias for nuclide', ''),
                _factory.AttributeFactory(
                    'weight_ratio', 'types.McnpReal', 'Atomic weight ratios', 'weight_ratio > 0'
                ),
            ],
        ),
    ],
    [],
)

_DataVoidFactory = _factory.DataFactory(
    'void',
    False,
    False,
    [
        _factory.AttributeFactory(
            'numbers',
            'tuple[types.McnpInteger]',
            'Tuple of cell numbers',
            '1 <= entry <= 99_999_999',
        ),
    ],
    [],
    [],
)

_DataMgoptFactory = _factory.DataFactory(
    'mgopt',
    False,
    False,
    [
        _factory.AttributeFactory('mcal', 'str', 'Problem type setting', 'mcal in {"f", "a"}'),
        _factory.AttributeFactory(
            'igm',
            'types.McnpInteger',
            'Total number of energy groups for all kinds of particle',
            'igm >= 0',
        ),
        _factory.AttributeFactory(
            'iplt',
            'types.McnpInteger',
            'Weight windows usage indicator',
            'iplt == 0 or iplt == 1 or iplt == 2',
        ),
        _factory.AttributeFactory(
            'iab',
            'types.McnpInteger',
            'Adjoint biasing for adjoint problems contorls',
            'iab == 0 or iab == 1 or iab == 2',
        ),
        _factory.AttributeFactory(
            'icw',
            'types.McnpInteger',
            'Name of the reference cell for generated weight windows',
            '',
        ),
        _factory.AttributeFactory(
            'fnw', 'types.McnpReal', 'Normalization value for generated weight windows', ''
        ),
        _factory.AttributeFactory(
            'rim', 'types.McnpReal', 'Generated weight windows compression limit', ''
        ),
    ],
    [],
    [],
)

_DataDrxsFactory = _factory.DataFactory(
    'drxs',
    False,
    False,
    [
        _factory.AttributeFactory('zaids', 'tuple[types.Zaid]', 'Tuple of ZAID aliases', ''),
    ],
    [],
    [],
)

_DataModeFactory = _factory.DataFactory(
    'mode',
    False,
    False,
    [
        _factory.AttributeFactory(
            'particles', 'tuple[types.Designator]', 'Tuple of particle designators', ''
        ),
    ],
    [],
    [],
)

_DataActFactory = _factory.DataFactory(
    'act',
    False,
    False,
    [],
    [],
    [
        _factory.DataOptionFactory(
            'fission',
            _factory.AttributeFactory(
                'kind',
                'str',
                'Type of delayed particle(s) to be produced from residuals created by fission',
                'type in {"none", "n,p,e,f,a", "all"}',
            ),
        ),
        _factory.DataOptionFactory(
            'nonfiss',
            _factory.AttributeFactory(
                'kind',
                'str',
                'Type of delayed particle(s) to be produced by simple multi-particle reaction',
                'type in {"none", "n,p,e,f,a", "all"}',
            ),
        ),
        _factory.DataOptionFactory(
            'dn',
            _factory.AttributeFactory(
                'source',
                'str',
                'Delayed neutron data source',
                'source in {"model", "library", "both", "prompt"}',
            ),
        ),
        _factory.DataOptionFactory(
            'dg',
            _factory.AttributeFactory(
                'source', 'str', 'Delayed gamma data source', 'source in {"line", "mg", "none"}'
            ),
        ),
        _factory.DataOptionFactory(
            'thresh',
            _factory.AttributeFactory(
                'fraction',
                'types.McnpReal',
                'Fraction of highest-amplitude discrete delayed-gamma lines retained',
                '0 <= fraction <= 1',
            ),
        ),
        _factory.DataOptionFactory(
            'dnbais',
            _factory.AttributeFactory(
                'count',
                'types.McnpInteger',
                'Maximum number of neutrons generated per reaction',
                '0 <= count <= 10',
            ),
        ),
        _factory.DataOptionFactory(
            'nap',
            _factory.AttributeFactory(
                'count', 'types.McnpInteger', 'Number of activation products', '0 <= count'
            ),
        ),
        _factory.DataOptionFactory(
            'pecut',
            _factory.AttributeFactory(
                'cutoff', 'types.McnpReal', 'Delayed-gamma energy cutoff', ''
            ),
        ),
        _factory.DataOptionFactory(
            'hlcut',
            _factory.AttributeFactory(
                'cutoff', 'types.McnpReal', 'Spontaneous-decay half-life threshold', ''
            ),
        ),
        _factory.DataOptionFactory(
            'sample',
            _factory.AttributeFactory(
                'setting',
                'str',
                'Flag for correlated or uncorrelated',
                'setting in {"correlate", "nonfiss_cor"}',
            ),
        ),
    ],
)

_DataCutFactory = _factory.DataFactory(
    'cut',
    False,
    True,
    [
        _factory.AttributeFactory('time_cutoff', 'types.McnpReal', 'Time cutoff in shakes', ''),
        _factory.AttributeFactory('energy_cutoff', 'types.McnpReal', 'Lower energy cutoff', ''),
        _factory.AttributeFactory('weight_cutoff1', 'types.McnpReal', 'Weight cutoff #1', ''),
        _factory.AttributeFactory('weight_cutoff2', 'types.McnpReal', 'Weight cutoff #2', ''),
        _factory.AttributeFactory('source_weight', 'types.McnpReal', 'Minimum source weight', ''),
    ],
    [],
    [],
)

_DataElptFactory = _factory.DataFactory(
    'elpt',
    False,
    True,
    [
        _factory.AttributeFactory(
            'cutoffs', 'tuple[types.McnpReal]', 'Tuple of cell lower energy cutoffs', ''
        ),
    ],
    [],
    [],
)

_DataThtmeFactory = _factory.DataFactory(
    'thtme',
    False,
    False,
    [
        _factory.AttributeFactory(
            'times',
            'tuple[types.McnpReal]',
            'Tuple of times when thermal temperatures are specified',
            'entry <= 99',
        ),
    ],
    [],
    [],
)

_DataLcaFactory = _factory.DataFactory(
    'lca',
    False,
    False,
    [
        _factory.AttributeFactory(
            'ielas',
            'types.McnpInteger',
            'Elastic scattering controls',
            'ielas == 0 or ielas == 1 or ielas == 2',
        ),
        _factory.AttributeFactory(
            'ipreg',
            'types.McnpInteger',
            'pre-equilibrium model',
            'ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3',
        ),
        _factory.AttributeFactory(
            'iexisa',
            'types.McnpInteger',
            'Model choice controls',
            'iexisa == 0 or iexisa == 1 or iexisa == 2',
        ),
        _factory.AttributeFactory(
            'ichoic', 'types.McnpInteger', 'ISABEL intranuclear cascade model control', ''
        ),
        _factory.AttributeFactory(
            'jcoul',
            'types.McnpInteger',
            'Coulomb barrier for incident charged particle controls',
            'jcoul == 0 or jcoul == 1',
        ),
        _factory.AttributeFactory(
            'nexite',
            'types.McnpInteger',
            'Subtract nuclear recoil energy to get excitation energy',
            'nexite == 0 or nexite == 1',
        ),
        _factory.AttributeFactory(
            'npidk',
            'types.McnpInteger',
            'Cutoff interact/terminate control',
            'npidk == 0 or npidk == 1',
        ),
        _factory.AttributeFactory(
            'noact',
            'types.McnpInteger',
            'Particle transport settings',
            'noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2',
        ),
        _factory.AttributeFactory(
            'icem',
            'types.McnpInteger',
            'Choose alternative physics model',
            'icem == 0 or icem == 1 or icem == 2',
        ),
        _factory.AttributeFactory(
            'ilaq',
            'types.McnpInteger',
            'Choose light ion and nucleon physics modules',
            'ilaq == 0 or ilaq == 1',
        ),
        _factory.AttributeFactory(
            'nevtype',
            'types.McnpInteger',
            'Choose number of evaporation particles for GEM2',
            '',
        ),
    ],
    [],
    [],
)

_DataLcbFactory = _factory.DataFactory(
    'lcb',
    False,
    False,
    [
        _factory.AttributeFactory(
            'flenb1', 'types.McnpReal', 'Kinetic energy for nucleons CEM/Bertini/INCL', ''
        ),
        _factory.AttributeFactory(
            'flenb2', 'types.McnpReal', 'Kinetic energy for nucleons LAQGSM03.03', ''
        ),
        _factory.AttributeFactory(
            'flenb3', 'types.McnpReal', 'Kinetic energy for pions CEM/Bertini/INCL', ''
        ),
        _factory.AttributeFactory(
            'flenb4', 'types.McnpReal', 'Kinetic energy for pions LAQGSM03.03', ''
        ),
        _factory.AttributeFactory(
            'flenb5', 'types.McnpReal', 'Kinetic energy for nucleons ISABEL', ''
        ),
        _factory.AttributeFactory(
            'flenb6', 'types.McnpReal', 'Kinetic energy for appropriate model', ''
        ),
        _factory.AttributeFactory(
            'cotfe', 'types.McnpReal', 'Cutoff kinetic energy for particle escape', ''
        ),
        _factory.AttributeFactory(
            'film0',
            'types.McnpReal',
            'Maximum correction allowed for masss-energy balancing',
            '',
        ),
    ],
    [],
    [],
)

_DataLccFactory = _factory.DataFactory(
    'lcc',
    False,
    False,
    [
        _factory.AttributeFactory(
            'stincl', 'types.McnpReal', 'Rescaling factor of the cascade duration', ''
        ),
        _factory.AttributeFactory('v0incl', 'types.McnpReal', 'Potential depth', ''),
        _factory.AttributeFactory(
            'xfoisaincl', 'types.McnpReal', 'Maximum impact parameter for Pauli blocking', ''
        ),
        _factory.AttributeFactory(
            'npaulincl',
            'types.McnpInteger',
            'Pauli blocking parameter setting',
            'npaulincl == 0 or npaulincl == -1 or npaulincl == 1',
        ),
        _factory.AttributeFactory(
            'nosurfincl',
            'types.McnpInteger',
            'Difuse nuclear surface based on Wood-Saxon density setting',
            'xfoisaincl == -2 or xfoisaincl == -1 or xfoisaincl == 0 or xfoisaincl == 1',
        ),
        _factory.AttributeFactory(
            'ecutincl', 'types.McnpReal', 'Bertini model energy below this energy', ''
        ),
        _factory.AttributeFactory(
            'ebankincl', 'types.McnpReal', 'INCL bank particles below this energy', ''
        ),
        _factory.AttributeFactory(
            'ebankabia', 'types.McnpReal', 'ABLA bank particles below this energy', ''
        ),
    ],
    [],
    [],
)

_DataLaeFactory = _factory.DataFactory(
    'lae',
    False,
    False,
    [
        _factory.AttributeFactory(
            'ipht',
            'types.McnpInteger',
            'Generation of de-excitation photons setting',
            'ipht.value in {0, 1}',
        ),
        _factory.AttributeFactory(
            'icc',
            'types.McnpInteger',
            'Level of physics for PHT physics setting',
            'icc.value in {0, 1, 2, 3, 4}',
        ),
        _factory.AttributeFactory(
            'nobalc',
            'types.McnpInteger',
            'Mass-energy balancing in cascade setting',
            'nobalc.value in {0, 1}',
        ),
        _factory.AttributeFactory(
            'nobale',
            'types.McnpInteger',
            'Mass-energy balancing in evaporation setting',
            'nobale.value in {0, 1}',
        ),
        _factory.AttributeFactory(
            'ifbrk',
            'types.McnpInteger',
            'Mass-energy balancing in Fermi-breakup setting',
            'ifbrk.value in {0, 1}',
        ),
        _factory.AttributeFactory(
            'ilvden',
            'types.McnpInteger',
            'Level-density model setting',
            'ilvden.value in {0, 1, -1}',
        ),
        _factory.AttributeFactory(
            'ievap',
            'types.McnpInteger',
            'Evaporation and fission model setting',
            'ievap.value in {0, 1, -1, 2}',
        ),
        _factory.AttributeFactory(
            'nofis', 'types.McnpInteger', 'Fission setting', 'nofis.value in {0, 1}'
        ),
    ],
    [],
    [],
)

_DataLebFactory = _factory.DataFactory(
    'leb',
    False,
    False,
    [
        _factory.AttributeFactory(
            'yzere',
            'types.McnpReal',
            'Y0 parameter in level-density formula for Z≤70',
            'yzere > 0',
        ),
        _factory.AttributeFactory(
            'bzere',
            'types.McnpReal',
            'B0 parameter in level-density formula for Z≤70',
            'bzere > 0',
        ),
        _factory.AttributeFactory(
            'yzero',
            'types.McnpReal',
            'Y0 parameter in level-density formula for Z≥71',
            'yzero > 0',
        ),
        _factory.AttributeFactory(
            'bzero',
            'types.McnpReal',
            'B0 parameter in level-density formula for Z≥70',
            'bzero > 0',
        ),
    ],
    [],
    [],
)

_DataFmultFactory = _factory.DataFactory(
    'fmult',
    False,
    False,
    [
        _factory.AttributeFactory('zaid', 'types.Zaid', 'Nuclide for which data are entered', ''),
    ],
    [],
    [
        _factory.DataOptionFactory(
            'sfnu',
            _factory.AttributeFactory(
                'nu', 'types.McnpReal', 'V bar for sampling spontaneous fission', ''
            ),
        ),
        _factory.DataOptionFactory(
            'width',
            _factory.AttributeFactory(
                'width', 'types.McnpReal', 'Width for sampling spontaneous fission', ''
            ),
        ),
        _factory.DataOptionFactory(
            'sfyield',
            _factory.AttributeFactory(
                'fission_yield', 'types.McnpReal', 'Spontaneous fission yield', ''
            ),
        ),
        _factory.DataOptionFactory(
            'method',
            _factory.AttributeFactory(
                'setting',
                'types.McnpInteger',
                'Gaussian sampling algorithm setting',
                'setting.value in {0, 1, 3, 5, 6, 7}',
            ),
        ),
        _factory.DataOptionFactory(
            'shift',
            _factory.AttributeFactory(
                'setting',
                'types.McnpInteger',
                'Shift method setting',
                'setting.value in {0, 1, 2, 3, 4}',
            ),
        ),
    ],
)

_DataTroptFactory = _factory.DataFactory(
    'tropt',
    False,
    False,
    [],
    [],
    [
        _factory.DataOptionFactory(
            'mcscat',
            _factory.AttributeFactory(
                'setting',
                'str',
                'Multiple coulomb scattering setting',
                'setting in {"off", "fnal1", "gaussian", "fnal2"}',
            ),
        ),
        _factory.DataOptionFactory(
            'eloss',
            _factory.AttributeFactory(
                'setting',
                'str',
                'Slowing down energy losses setting',
                'setting in {"off", "strag1", "csda"}',
            ),
        ),
        _factory.DataOptionFactory(
            'nreact',
            _factory.AttributeFactory(
                'setting',
                'str',
                'Nuclear reactions setting',
                'setting in {"off", "on", "atten", "remove"}',
            ),
        ),
        _factory.DataOptionFactory(
            'nescat',
            _factory.AttributeFactory(
                'setting',
                'str',
                'Nuclear elastic scattering setting',
                'setting in {"off", "on"}',
            ),
        ),
    ],
)

_DataUncFactory = _factory.DataFactory(
    'unc',
    False,
    True,
    [
        _factory.AttributeFactory(
            'settings',
            'tuple[types.McnpInteger]',
            'Tuple of uncollided secondary settings',
            'entry.value in {0, 1}',
        ),
    ],
    [],
    [],
)

_DataCosypFactory = _factory.DataFactory(
    'cosyp',
    False,
    False,
    [
        _factory.AttributeFactory(
            'prefix', 'types.McnpInteger', 'Prefix number of the COSY map files', ''
        ),
        _factory.AttributeFactory(
            'axsh', 'types.McnpInteger', 'Horiztonal axis orientation', 'axsh.value in {1, 2, 3}'
        ),
        _factory.AttributeFactory(
            'axsv', 'types.McnpInteger', 'Vertical axis orientation', 'axsv.value in {1, 2, 3}'
        ),
        _factory.AttributeFactory(
            'emaps', 'tuple[types.McnpReal]', 'Tuple of operating beam energies', ''
        ),
    ],
    [],
    [],
)

_DataCosyFactory = _factory.DataFactory(
    'cosy',
    False,
    False,
    [
        _factory.AttributeFactory(
            'numbers', 'tuple[types.McnpInteger]', 'Tuple of COSY map numbers', ''
        ),
    ],
    [],
    [],
)

_DataBfldFactory = _factory.DataFactory(
    'bfld',
    True,
    False,
    [
        _factory.AttributeFactory(
            'kind', 'str', 'Magnetic field type', 'type in {"const", "quad", "quadff"}'
        ),
    ],
    [],
    [
        _factory.DataOptionFactory(
            'field',
            _factory.AttributeFactory(
                'strength_gradient', 'types.McnpReal', 'Magnetic field strength/gradient', ''
            ),
        ),
        _factory.DataOptionFactory(
            'vec',
            _factory.AttributeFactory(
                'vector',
                'tuple[types.McnpReal]',
                'Direction of mangentic field or plane corresponding to the x-axis of the quadrapole',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'maxdeflc',
            _factory.AttributeFactory('angle', 'types.McnpReal', 'Maximum deflection angles', ''),
        ),
        _factory.DataOptionFactory(
            'maxstep',
            _factory.AttributeFactory('size', 'types.McnpReal', 'Maximum step size', ''),
        ),
        _factory.DataOptionFactory(
            'axs',
            _factory.AttributeFactory(
                'vector',
                'tuple[types.McnpReal]',
                'Direction of the cosines of the quadropole beam axis',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'ffedges',
            _factory.AttributeFactory(
                'numbers',
                'tuple[types.McnpReal]',
                'Surface numbers to apply field fringe edges',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'refpnt',
            _factory.AttributeFactory(
                'point', 'tuple[types.McnpReal]', 'Point anywhere on the quadrapole beam', ''
            ),
        ),
    ],
)

_DataBflclFactory = _factory.DataFactory(
    'bflcl',
    False,
    False,
    [
        _factory.AttributeFactory(
            'numbers', 'tuple[types.McnpInteger]', 'Tuple of BFLD map numbers', ''
        ),
    ],
    [],
    [],
)

_DataSdefFactory = _factory.DataFactory(
    'sdef',
    False,
    False,
    [],
    [],
    [
        _factory.DataOptionFactory(
            'cel',
            _factory.AttributeFactory(
                'number', 'types.McnpInteger', 'Cell number', '0 <= number <= 99_999_999'
            ),
        ),
        _factory.DataOptionFactory(
            'sur',
            _factory.AttributeFactory(
                'number', 'types.McnpInteger', 'Surface number', '0 <= number <= 99_999_999'
            ),
        ),
        _factory.DataOptionFactory(
            'erg',
            _factory.AttributeFactory('energy', 'types.McnpReal', 'Kinetic energy', ''),
        ),
        _factory.DataOptionFactory(
            'tme',
            _factory.AttributeFactory(
                'time',
                'Union[types.McnpReal, types.EmbeddedDistributionNumber]',
                'Time in shakes',
                'time >= 0',
            ),
        ),
        _factory.DataOptionFactory(
            'dir',
            _factory.AttributeFactory(
                'cosine', 'types.McnpReal', 'Cosine of the angle between VEC and particle', ''
            ),
        ),
        _factory.DataOptionFactory(
            'vec',
            _factory.AttributeFactory(
                'vector', 'tuple[types.McnpReal]', 'Reference vector for DIR', ''
            ),
        ),
        _factory.DataOptionFactory(
            'nrm',
            _factory.AttributeFactory(
                'sign', 'types.McnpInteger', 'Sign of the surface normal', ''
            ),
        ),
        _factory.DataOptionFactory(
            'pos',
            _factory.AttributeFactory(
                'vector',
                'tuple[types.McnpReal]',
                'Reference point for position sampling in vector notation',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'rad',
            _factory.AttributeFactory(
                'radial_distance',
                'types.McnpReal',
                'Radial distance fo the position from POS or AXS',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'ext',
            _factory.AttributeFactory(
                'distance_cosine',
                'types.McnpReal',
                'Distance for POS along AXS or Cosine of angle from AXS',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'axs',
            _factory.AttributeFactory(
                'vector', 'tuple[types.McnpReal]', 'Reference vector for EXT and RAD', ''
            ),
        ),
        _factory.DataOptionFactory(
            'x',
            _factory.AttributeFactory(
                'x_coordinate', 'types.McnpReal', 'X-cordinate of position', ''
            ),
        ),
        _factory.DataOptionFactory(
            'y',
            _factory.AttributeFactory(
                'y_coordinate', 'types.McnpReal', 'Y-cordinate of position', ''
            ),
        ),
        _factory.DataOptionFactory(
            'z',
            _factory.AttributeFactory(
                'z_coordinate', 'types.McnpReal', 'Z-cordinate of position', ''
            ),
        ),
        _factory.DataOptionFactory(
            'ccc',
            _factory.AttributeFactory(
                'number',
                'types.McnpInteger',
                'Cookie-cutter cell number',
                '0 <= number <= 99_999_999',
            ),
        ),
        _factory.DataOptionFactory(
            'ara',
            _factory.AttributeFactory('area', 'types.McnpReal', 'Area of surface', ''),
        ),
        _factory.DataOptionFactory(
            'wgt',
            _factory.AttributeFactory('weight', 'types.McnpReal', 'Particle weight', ''),
        ),
        _factory.DataOptionFactory(
            'eff',
            _factory.AttributeFactory(
                'criterion',
                'types.McnpReal',
                'Rejection efficiency criterion for position sampling',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'par',
            _factory.AttributeFactory('kind', 'str', 'Source particle type', ''),
        ),
    ],
)

_DataScFactory = _factory.DataFactory(
    'sc',
    True,
    False,
    [_factory.AttributeFactory('comment', 'tuple[str]', 'source comment', '')],
    [],
    [],
)

_DataSsrFactory = _factory.DataFactory(
    'ssr',
    False,
    False,
    [],
    [],
    [
        _factory.DataOptionFactory(
            'old',
            _factory.AttributeFactory(
                'numbers',
                'tuple[types.McnpInteger]',
                'Tuple of surface numbers from subset of surfaces on SSW card',
                '1 <= entry <= 99_999_999',
            ),
        ),
        _factory.DataOptionFactory(
            'cel',
            _factory.AttributeFactory(
                'numbers',
                'tuple[types.McnpInteger]',
                'Tuple of cell from subset of cells on SSW card',
                '1 <= entry <= 99_999_999',
            ),
        ),
        _factory.DataOptionFactory(
            'new',
            _factory.AttributeFactory(
                'numbers',
                'tuple[types.McnpInteger]',
                'Tuple of surface numbers to start run',
                '1 <= entry <= 99_999_999',
            ),
        ),
        _factory.DataOptionFactory(
            'pty',
            _factory.AttributeFactory(
                'particles', 'tuple[types.Designator]', 'Tuple of designators', ''
            ),
        ),
        _factory.DataOptionFactory(
            'col',
            _factory.AttributeFactory(
                'setting',
                'types.McnpInteger',
                'Collision option setting',
                'setting.value in {-1, 0, 1}',
            ),
        ),
        _factory.DataOptionFactory(
            'wgt',
            _factory.AttributeFactory(
                'constant', 'types.McnpReal', 'Particle weight multiplier', ''
            ),
        ),
        _factory.DataOptionFactory(
            'axs',
            _factory.AttributeFactory(
                'cosines', 'tuple[types.McnpReal]', 'Direction cosines defining', ''
            ),
        ),
        _factory.DataOptionFactory(
            'ext',
            _factory.AttributeFactory(
                'number',
                'types.DistributionNumber',
                'Distribution number for baising sampling',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'poa',
            _factory.AttributeFactory(
                'angle',
                'types.McnpReal',
                'Angle within which particles accepeted for transport',
                '',
            ),
        ),
    ],
)

_DataKcodeFactory = _factory.DataFactory(
    'kcode',
    False,
    False,
    [
        _factory.AttributeFactory(
            'nsrck', 'types.McnpInteger', 'Number of source histories per cycle', 'nsrck >= 0'
        ),
        _factory.AttributeFactory('rkk', 'types.McnpReal', 'Initial guess of keff', ''),
        _factory.AttributeFactory(
            'ikz',
            'types.McnpInteger',
            'Number of cycles to be skipped before beginning tally accumulation',
            '',
        ),
        _factory.AttributeFactory(
            'kct', 'types.McnpInteger', 'Total number of cycles to be done', 'kct > 0'
        ),
        _factory.AttributeFactory(
            'msrk',
            'types.McnpInteger',
            'Number of source points to allocate for.',
            'msrk < 40 * nsrck',
        ),
        _factory.AttributeFactory(
            'knrm', 'types.McnpInteger', 'Normalization of tallies setting', 'knrm.value in {0, 1}'
        ),
        _factory.AttributeFactory(
            'mrkp',
            'types.McnpInteger',
            'Maximum number of cycle values on MCTAL or RUNTPE files',
            'mrkp > 0',
        ),
        _factory.AttributeFactory(
            'kc8',
            'types.McnpInteger',
            'Number of cylces for average setting',
            'kc8.value in {0, 1}',
        ),
    ],
    [],
    [],
)

_DataKsrcFactory = _factory.DataFactory(
    'ksrc',
    False,
    False,
    [
        _factory.AttributeFactory(
            'locations', 'tuple[KsrcEntry]', 'Tuple of inital source points', ''
        ),
    ],
    [
        _factory.DataEntryFactory(
            'ksrc',
            [
                _factory.AttributeFactory('x', 'types.McnpReal', 'Location x-coordinate', ''),
                _factory.AttributeFactory('y', 'types.McnpReal', 'Location y-coordinate', ''),
                _factory.AttributeFactory('z', 'types.McnpReal', 'Location z-coordinate', ''),
            ],
        ),
    ],
    [],
)

_DataKoptsFactory = _factory.DataFactory(
    'kopts',
    False,
    False,
    [],
    [],
    [
        _factory.DataOptionFactory(
            'blocksize',
            _factory.AttributeFactory(
                'ncy',
                'types.McnpInteger',
                'Number of cycles in every outer iteration',
                'ncy >= 2',
            ),
        ),
        _factory.DataOptionFactory(
            'kinetics',
            _factory.AttributeFactory(
                'setting',
                'str',
                'Yes/No calculate point-kinetics parameters',
                'setting in {"yes", "no"}',
            ),
        ),
        _factory.DataOptionFactory(
            'precursor',
            _factory.AttributeFactory(
                'setting',
                'str',
                'Yes/No detailed precursor information',
                'setting in {"yes", "no"}',
            ),
        ),
        _factory.DataOptionFactory(
            'ksental',
            _factory.AttributeFactory(
                'fileopt',
                'str',
                'Format of sensity profiles output file',
                'fileopt in {"mctal"}',
            ),
        ),
        _factory.DataOptionFactory(
            'fmat',
            _factory.AttributeFactory('setting', 'str', 'Yes/No FMAT', 'setting in {"yes", "no"}'),
        ),
        _factory.DataOptionFactory(
            'fmatskpt',
            _factory.AttributeFactory('fmat_skip', 'types.McnpReal', 'fmat_skip', ''),
        ),
        _factory.DataOptionFactory(
            'fmatncyc',
            _factory.AttributeFactory('fmat_ncyc', 'types.McnpReal', 'fmat_ncyc', ''),
        ),
        _factory.DataOptionFactory(
            'fmatspace',
            _factory.AttributeFactory('fmat_space', 'types.McnpReal', 'fmat_space', ''),
        ),
        _factory.DataOptionFactory(
            'fmataccel',
            _factory.AttributeFactory('setting', 'str', 'fmataccel', 'setting in {"yes", "no"}'),
        ),
        _factory.DataOptionFactory(
            'fmatreduce',
            _factory.AttributeFactory('setting', 'str', 'fmatreduce', 'setting in {"yes", "no"}'),
        ),
        _factory.DataOptionFactory(
            'fmatnx',
            _factory.AttributeFactory('fmat_nx', 'types.McnpReal', 'fmat_nx', ''),
        ),
        _factory.DataOptionFactory(
            'fmatny',
            _factory.AttributeFactory('fmat_ny', 'types.McnpReal', 'fmat_ny', ''),
        ),
        _factory.DataOptionFactory(
            'fmatnz',
            _factory.AttributeFactory('fmat_nz', 'types.McnpReal', 'fmat_nz', ''),
        ),
    ],
)

_DataHsrcFactory = _factory.DataFactory(
    'hsrc',
    False,
    False,
    [
        _factory.AttributeFactory(
            'x_number',
            'types.McnpInteger',
            'Number of mesh intervals in x direction',
            'x_number > 0',
        ),
        _factory.AttributeFactory('x_minimum', 'types.McnpReal', 'Minimum x-value for mesh.', ''),
        _factory.AttributeFactory('x_maximum', 'types.McnpReal', 'Maximum x-value for mesh.', ''),
        _factory.AttributeFactory(
            'y_number',
            'types.McnpInteger',
            'Number of mesh intervals in y direction',
            'y_number > 0',
        ),
        _factory.AttributeFactory('y_minimum', 'types.McnpReal', 'Minimum y-value for mesh.', ''),
        _factory.AttributeFactory('y_maximum', 'types.McnpReal', 'Maximum y-value for mesh.', ''),
        _factory.AttributeFactory(
            'z_number',
            'types.McnpInteger',
            'Number of mesh intervals in z direction',
            'z_number > 0',
        ),
        _factory.AttributeFactory('z_minimum', 'types.McnpReal', 'Minimum z-value for mesh.', ''),
        _factory.AttributeFactory('z_maximum', 'types.McnpReal', 'Maximum z-value for mesh.', ''),
    ],
    [],
    [],
)

_DataNpsFactory = _factory.DataFactory(
    'nps',
    False,
    False,
    [
        _factory.AttributeFactory(
            'npp', 'types.McnpInteger', 'Total number of histories to run', 'npp > 0'
        ),
        _factory.AttributeFactory(
            'npsmg',
            'types.McnpInteger',
            'Number of history with direct source contributions',
            'npsmg > 0',
        ),
    ],
    [],
    [],
)

_DataRandFactory = _factory.DataFactory(
    'rand',
    False,
    False,
    [],
    [],
    [
        _factory.DataOptionFactory(
            'gen',
            _factory.AttributeFactory(
                'setting',
                'types.McnpInteger',
                'Type of pseudorandom number generator',
                'setting.value in {1, 2, 3, 4}',
            ),
        ),
        _factory.DataOptionFactory(
            'seed',
            _factory.AttributeFactory(
                'seed',
                'types.McnpInteger',
                'Random number generator seed',
                'seed.value % 2 == 1',
            ),
        ),
        _factory.DataOptionFactory(
            'stride',
            _factory.AttributeFactory(
                'stride',
                'types.McnpInteger',
                'Number of random numbers between source particle',
                '',
            ),
        ),
        _factory.DataOptionFactory(
            'hist',
            _factory.AttributeFactory(
                'hist', 'types.McnpInteger', 'Starting pseudorandom number', ''
            ),
        ),
    ],
)

exec(_DataAreaFactory.build())
exec(_DataTrFactory.build())
exec(_DataUFactory.build())
exec(_DataLatFactory.build())
exec(_DataFillFactory.build())
exec(_DataUranFactory.build())
exec(_DataDmFactory.build())
exec(_DataEmbedFactory.build())
exec(_DataEmbeeFactory.build())
exec(_DataEmbebFactory.build())
exec(_DataEmbemFactory.build())
exec(_DataEmbtbFactory.build())
exec(_DataEmbtmFactory.build())
exec(_DataEmbdbFactory.build())
exec(_DataEmbdfFactory.build())
exec(_DataMtFactory.build())
exec(_DataOtfdbFactory.build())
exec(_DataNonuFactory.build())
exec(_DataAwtabFactory.build())
exec(_DataXsFactory.build())
exec(_DataVoidFactory.build())
exec(_DataMgoptFactory.build())
exec(_DataDrxsFactory.build())
exec(_DataModeFactory.build())
exec(_DataActFactory.build())
exec(_DataCutFactory.build())
exec(_DataElptFactory.build())
exec(_DataThtmeFactory.build())
exec(_DataLcaFactory.build())
exec(_DataLcbFactory.build())
exec(_DataLccFactory.build())
exec(_DataLaeFactory.build())
exec(_DataLebFactory.build())
exec(_DataFmultFactory.build())
exec(_DataTroptFactory.build())
exec(_DataUncFactory.build())
exec(_DataCosypFactory.build())
exec(_DataCosyFactory.build())
exec(_DataBfldFactory.build())
exec(_DataBflclFactory.build())
exec(_DataSdefFactory.build())
exec(_DataScFactory.build())
exec(_DataSsrFactory.build())
exec(_DataKcodeFactory.build())
exec(_DataKsrcFactory.build())
exec(_DataKoptsFactory.build())
exec(_DataHsrcFactory.build())
exec(_DataNpsFactory.build())
exec(_DataRandFactory.build())


exec(
    _DataMFactory.build()
    + '''
    @staticmethod
    def from_formula(number: int, formulas: dict[str, float], atomic_or_weight: bool = True):
        """
        ``from_formula`` generates ``Datum`` objects from INP.

        ``from_formula`` constructs instances of ``Datum`` from chemcials
        formulas and fractions, so it operates as a class constructor method.

        Parameters:
            number: Arbitrary material number.
            formulas: Dictionary of formulas and atomic/weight fractions.
            atomic_or_weight: Atomtic/Weight fraction true/false flag.

        Returns:
            ``Datum`` object.
        """

        substances = []
        comments = []
        for formula, mixture_fraction in formulas.items():
            formula = molmass.Formula(formula)

            composition = formula.composition()
            for element in composition:
                compound_fraction = (
                    composition[element].fraction
                    if atomic_or_weight
                    else composition[element].mass / formula.mass
                )

                zaids = [
                    (
                        types.Zaid(_elements.ELEMENTS[element]['z'], a),
                        isotropic_fraction,
                    )
                    for a, isotropic_fraction in _elements.ELEMENTS[element]['fraction'].items()
                ]
                subcomments = [f'{element}-{zaid.a:03}' for zaid, _ in zaids]
                entries = [
                    MEntry(
                        zaid,
                        types.McnpReal(
                            (-1 if atomic_or_weight else 1)
                            * mixture_fraction
                            * compound_fraction
                            * isotropic_fraction
                        ),
                    )
                    for zaid, isotropic_fraction in zaids
                ]

                comments += subcomments
                substances += entries

        material = M(substances, {}, suffix=types.McnpInteger(number))
        material.comment = tuple(comments)

        return material
'''
)


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
