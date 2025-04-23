import enum
import typing


class Error(Exception):
    """
    Represents generic PyMCNP errors.

    Attributes:
        code: Error code.
        info: Error string.
    """

    def __init__(self, code: enum.Enum, info: str):
        """
        Initializes ``Error``

        Parameters:
            code: Error code.
            info: Error string.

        Returns:
            ``Error``.
        """

        self.code: typing.Final[CliCode] = code
        self.info: typing.Final[str] = info


class McnpCode(enum.Enum):
    """
    Represents MCNP error codes.

    Notes:
        0x - Syntax
        1x - Semantics
    """

    SYNTAX_TYPE = 0

    SEMANTICS_TYPE = 10


class MeshtalCode(enum.Enum):
    """
    Represents MESHTAL error codes.

    Notes:
        0x - Syntax
        1x - Semantics
    """

    SYNTAX_MESHTAL = 0
    SYNTAX_BLOCK = 1
    SYNTAX_LINE = 2

    SEMANTICS_MESHTAL = 10
    SEMANTICS_BLOCK = 11
    SEMANTICS_LINE = 12


class PtracCode(enum.Enum):
    """
    Represents PTRAC error codes.

    Notes:
        0x - Syntax
        1x - Semantics
    """

    SYNTAX_PTRAC = 0
    SYNTAX_BLOCK = 1
    SYNTAX_LINE = 2
    SYNTAX_KEYWORD = 3

    SEMANTICS_PTRAC = 10
    SEMANTICS_BLOCK = 11
    SEMANTICS_LINE = 12
    SEMANTICS_KEYWORD = 13


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
    SYNTAX_CARD = 1
    SYNTAX_OPTION = 2

    SEMANTICS_INP = 10
    SEMANTICS_CARD = 11
    SEMANTICS_OPTION = 12


class CliCode(enum.Enum):
    """
    Represents CLI error codes.

    Notes:
        0xxx - Misc
    """

    SEMANTICS_INP = 0
    SEMANTICS_PATH = 1
    SEMANTICS_COMMAND = 2

    pass


class McnpError(Error):
    pass


class InpError(Error):
    pass


class PtracError(Error):
    pass


class CliError(Error):
    pass
    pass
