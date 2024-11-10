"""
``datum`` contains the class representing INP data cards.

``datum`` packages the ``Datum`` class, providing an object-oriented,
importable interface for INP datum cards.
"""

from enum import Enum


from .. import _card
from ...utils import errors
from ...utils import _parser


class DatumMnemonic(str, Enum):
    """
    ``DatumMnemonic`` represents INP data card mnemonics

    ``DatumMnemonic`` implements INP data card mnemonics as a Python inner
    class. It enumerates MCNP mnemonics and provides methods for casting
    strings to ``DatumMnemonic`` instances. It represents the INP data card
    mnemonics syntax element, so ``Datum`` depends on ``DatumMnemonic`` as
    an enum.
    """

    VOLUME = 'vol'
    AREA = 'area'
    TRANSFORMATION = 'tr'
    TRANSFORMATION_ANGLE = '*tr'
    UNIVERSE = 'u'
    LATTICE = 'lat'
    FILL = 'fill'
    FILL_ANGLE = '*fill'
    STOCHASTIC_GEOMETRY = 'uran'
    DETERMINISTIC_MATERIALS = 'dm'
    DETERMINISTIC_WEIGHT_WINDOW = 'dawwg'
    EMBEDDED_GEOMETRY = 'embed'
    EMBEDDED_CONTROL = 'embee'
    EMBEDDED_ENERGY_BOUNDARIES = 'embeb'
    EMBEDDED_ENERGY_MULTIPLIERS = 'embem'
    EMBEDDED_TIME_BOUNDARIES = 'embtb'
    EMBEDDED_TIME_MULTIPLIERS = 'embtm'
    EMBEDDED_DOSE_BOUNDARIES = 'embde'
    EMBEDDED_DOSE_MULTIPLIERS = 'embdf'
    MATERIAL = 'm'
    MATERIAL_NEUTRON_SCATTERING = 'mt'
    MATERIAL_NUCLIDE_SUBSTITUTION = 'mx'
    ON_THE_FLY_BROADENING = 'otfdb'
    TOTAL_FISSION = 'totnu'
    FISSION_TURNOFF = 'nonu'
    ATOMIC_WEIGHT = 'awtab'
    CROSS_SECTION_FILE = 'xs'
    VOID = 'void'
    MULTIGROUP_ADJOINT_TRANSPORT = 'mgopt'
    DISCRETE_REACTION_CROSS_SECTION = 'drxs'
    PROBLEM_TYPE = 'mode'
    PARTICLE_PHYSICS_OPTIONS = 'phys'
    ACTIVATION_CONTROL = 'act'
    TIME_ENERGY_WEIGHT_CUTOFFS = 'cut'
    CELL_ENERGY_CUTOFFS = 'elpt'
    FREE_GAS_THERMAL_TEMPERATURE = 'tmp'
    THERMAL_TIMES = 'thtme'
    MODEL_PHYSICS_CONTROL = 'mphys'
    LCA = 'lca'
    LCB = 'lcb'
    LCC = 'lcc'
    LEA = 'lea'
    LEB = 'leb'
    MULTIPLICITY_CONSTANTS = 'fmult'
    TRANSPORT_OPTIONS = 'tropt'
    UNCOLLIDED_SECONDARIES = 'unc'
    COSYP = 'cosyp'
    COSY = 'cosy'
    BFLD = 'bfld'
    BFLCL = 'bflcl'
    GRAVITATIONAL_FIELD = 'field'
    GENERAL_SOURCE_DEFINITION = 'sdef'
    SOURCE_INFORMATION = 'si'
    SOURCE_PROBABILITY = 'sp'
    SOURCE_BIAS = 'sb'
    DEPENDENT_SOURCE_DISTRIBUTION = 'ds'
    SOURCE_COMMENT = 'sc'
    SURFACE_SOURCE_WRITE = 'ssw'
    SURFACE_SOURCE_READ = 'ssr'
    CRITICALITY_SOURCE = 'kcode'
    CRITICALITY_SOURCE_POINTS = 'ksrc'
    CRITICALITY_CALCULIATION_OPTIONS = 'kopts'
    ENTROPY_SOURCE_DISTRIBUTION = 'hsrc'
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
    HISTORY_CUTOFF = 'nps'
    COMPUTER_TIME_CUTOFF = 'ctme'
    PERCISION_CUTOFF = 'stop'
    OUTPUT_PRINT_TABLES = 'print'
    NEGATE_PRINTING_TALLIES = 'talnp'
    PRINT_DUMP_CYCLES = 'prdmp'
    PARTICLE_TRACK_OUTPUT = 'ptrac'
    PLOT_TALLIES_WHITE_RUNNING = 'mplot'
    CREATE_LAHET = 'histp'
    RANDOM = 'rand'
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
        if source not in [enum.value for enum in DatumMnemonic]:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_MNEMONIC)

        return DatumMnemonic(source)

    def to_mcnp(self):
        """
        ``to_mcnp`` generates INP from ``DatumMnemonic`` objects.

        ``to_mcnp`` creates INP source string from ``DatumMnemonic`` objects,
        so it provides an MCNP endpoint.

        Returns:
            INP string for ``DatumMnemonic`` object.
        """

        return self.value


class Datum(_card.Card):
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

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Datum`` objects.

        ``to_mcnp`` creates INP source string from ``Datum``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``Datum`` object.
        """

        suffix_str = self.suffix.to_mcnp() if hasattr(self, 'suffix') else ''
        designator_str = f':{self.designator}' if hasattr(self, 'designator') else ''

        parameters_str = ''
        for parameter in self.parameters:
            if parameter is None:
                continue
            elif isinstance(parameter, tuple):
                parameters_str += f" {' '.join([str(entry) for entry in parameter])}"
            elif not hasattr(parameter, 'to_mcnp'):
                parameters_str += f' {str(parameter)}'
            else:
                parameters_str += f' {parameter.to_mcnp()}'

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()}{suffix_str}{designator_str}{parameters_str}'
        )

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
            'mnemonic': (self.mnemonic.to_mcnp()),
            'm': self.suffix.to_mcnp() if hasattr(self, 'suffix') else None,
            'n': self.designator.to_mcnp() if hasattr(self, 'designator') else None,
            'parameters': tuple(
                [
                    parameter.to_mcnp() if hasattr(parameter, 'to_mcnp') else parameter
                    for parameter in self.parameters
                ]
            ),
        }


class _Placeholder(Datum):
    """Placeholder for F8, FT8, etc."""

    def __init__(self, mnemonic: DatumMnemonic, parameters: tuple[any]):
        self.id = mnemonic
        self.mnemonic = mnemonic
        self.parameters = parameters

    def to_mcnp(self):
        tmp = []
        # convert all parameters to strings
        for parameter in self.parameters:
            parameters_str = ''
            if parameter is None:
                continue
            elif isinstance(parameter, tuple):
                parameters_str += ' '.join([str(entry) for entry in parameter])
            elif not hasattr(parameter, 'to_mcnp'):
                parameters_str += str(parameter)
            else:
                parameters_str += parameter.to_mcnp()

            tmp.append(parameters_str)
        return _parser.Postprocessor.add_continuation_lines(' '.join(tmp))
