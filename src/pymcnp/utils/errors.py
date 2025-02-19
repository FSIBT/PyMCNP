import enum
import typing


class _Error(Exception):
    """
    Represents generic PyMCNP errors.

    Attributes:
        code: Error code.
        info: Error string.
    """

    def __init__(self, code: enum.Enum, info: str):
        """
        Initializes ``_Error``

        Parameters:
            code: Error code.
            info: Error string.

        Returns:
            ``_Error``.
        """

        self.code: typing.Final[CliCode] = code
        self.info: typing.Final[str] = info


class McnpCode(enum.Enum):
    """
    Represents MCNP error codes.

    Notes:
        0xxx - Syntax
        1xxx - Semantics
        x0xx - Types
    """

    SYNTAX_INTEGER = 0
    SYNTAX_REAL = 1
    SYNTAX_STRING = 2
    SYNTAX_REPEAT = 3
    SYNTAX_INSERT = 4
    SYNTAX_MULTIPLY = 5
    SYNTAX_JUMP = 6
    SYNTAX_LOG = 7
    SYNTAX_DISTRIBUTIONNUMBER = 8
    SYNTAX_EMBEDDEDDISTRIBUTIONNUMBER = 9
    SYNTAX_ZAID = 10
    SYNTAX_PARTICLE = 11
    SYNTAX_DESIGNATOR = 12
    SYNTAX_TUPLE = 13

    SEMANTICS_INTEGER_VALUE = 1000
    SEMANTICS_REAL_VALUE = 1001
    SEMANTICS_STRING_VALUE = 1002
    SEMANTICS_REPEAT_N = 1003
    SEMANTICS_INSERT_N = 1004
    SEMANTICS_MULTIPLY_X = 1005
    SEMANTICS_JUMP_N = 1006
    SEMANTICS_LOG_N = 1007
    SEMANTICS_DISTRIBUTIONNUMBER_N = 1008
    SEMANTICS_EMBEDDEDDISTRIBUTIONNUMBER_NUMBERS = 1009
    SEMANTICS_ZAID_Z = 1010
    SEMANTICS_ZAID_A = 1011
    SEMANTICS_ZAID_ABX = 1012
    SEMANTICS_DESIGNATOR_PARTICLES = 1013
    SEMANTICS_TUPLE_VALUE = 1014


class PtracCode(enum.Enum):
    """
    Represents PTRAC error codes.

    Notes:
        0xxx - Syntax
        1xxx - Semantics
        x0xx - Ptrac
        x1xx - Elements
    """

    SYNTAX_PTRAC = 0

    SYNTAX_BLOCK = 101
    SYNTAX_LINE = 102
    SYNTAX_KEYWORD = 103

    SEMANTICS_PTRAC_HEADER = 1000
    SEMANTICS_PTRAC_HISTORY = 1001

    SEMANTICS_BLOCK_VALUE = 1100
    SEMANTICS_LINE_VALUE = 1101
    SEMANTICS_KEYWORD_VALUE = 1102


class InpCode(enum.Enum):
    """
    Represents INP error codes.

    Notes:
        0xxx - Syntax
        1xxx - Semantics
        x0xx - Inp
        x1xx - Cell
        x2xx - Surface
        x3xx - Data
        x4xx - Comment
        x5xx - Types
    """

    SYNTAX_INP = 0

    SYNTAX_CARD = 101
    SYTNAX_ENTRY = 103
    SYNTAX_OPTION = 102

    SEMANTICS_INP_MESSAGE = 1000
    SEMANTICS_INP_TITLE = 1001
    SEMANTICS_INP_CELLS = 1002
    SEMANTICS_INP_COMMENTS = 1003
    SEMANTICS_INP_SURFACES = 1004
    SEMANTICS_INP_DATA = 1005
    SEMANTICS_INP_OTHER = 1006

    SEMANTICS_CARD_VALUE = 1101
    SEMANTICS_ENTRY_VALUE = 1102
    SEMANTICS_OPTION_VALUE = 1103


class CliCode(enum.Enum):
    """
    Represents CLI error codes.

    Notes:
        0xx - Misc
        1xx - Run
        2xx - Inp
    """

    SEMANTICS_INP = 0
    SEMANTICS_PATH = 1

    SEMANTICS_PREHOOK = 10
    SEMANTICS_POSTHOOK = 11
    SEMANTICS_COMMAND = 12


class McnpError(_Error):
    pass


class InpError(_Error):
    pass


class PtracError(_Error):
    pass


class CliError(_Error):
    pass
