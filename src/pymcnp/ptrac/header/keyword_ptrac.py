from . import _keyword
from ...utils import errors
from ...utils import _parser


class HeaderKeyword_Ptrac(_keyword.HeaderKeyword_):
    """
    Represents PTRAC input format index keywords.
    """

    BUFFER = 1
    CELL = 2
    EVENT = 3
    FILE = 4
    FILTER = 5
    MAX = 6
    MENP = 7
    NPS = 8
    SURFACE = 9
    TALLY = 10
    TYPE = 11
    VALUE = 12
    WRITE = 13
    UNKNOWN = 14

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracKeywords`` from PTRAC.

        Parameters:
            source: PTRAC for ``PtracKeywords``.

        Returns:
            ``PtracKeywords``.

        Raises:
            McnpError: INVALID_EVENT_TYPE.
        """

        source = _parser.Preprocessor.preprocess_ptrac(source)

        try:
            return HeaderKeyword_Ptrac(int(source))
        except ValueError:
            raise errors.McnpError(errors.McnpCode.INVALID_EVENT_TYPE)
