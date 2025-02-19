from . import _keyword
from ...utils import errors
from ...utils import _parser


class HistoryKeyword_Nters(_keyword.HistoryKeyword_):
    """
    Represents PTRAC event NTER variables.
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
        Generates ``HistoryKeyword_Nters`` from PTRAC.

        Parameters:
            source: PTRAC for ``HistoryKeyword_Nters``.

        Returns:
            ``HistoryKeyword_Nters``.

        Raises:
            PtracError: SYNTAX_HISTORY_KEYWORD.
        """

        source = _parser.Preprocessor.preprocess_ptrac(source)

        try:
            return HistoryKeyword_Nters(int(source))
        except ValueError:
            raise errors.PtracError(errors.PtracCode.SYNTAX_HISTORY_KEYWORD, source)
