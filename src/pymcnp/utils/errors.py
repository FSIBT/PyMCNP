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

    SYNTAX_TYPE = 0

    SEMANTICS_TYPE_VALUE = 1000


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
