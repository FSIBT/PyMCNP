"""
Contains classes representing INP data cards.
"""

import re
from typing import Final

from . import _card
from ..utils import errors
from ..utils import _parser
from .data_mnemonic import DataMnemonic


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
