from . import _error


class OutpCode(_error.Code):
    """
    Represents ``outp`` error codes.

    Notes:
        0x - Syntax
        1x - Semantics
        x0 - File
        x1 - Table
    """

    SYNTAX_FILE = 0
    SYNTAX_TABLE = 1

    SEMANTICS_FILE = 10
    SEMANTICS_TABLE = 11


class OutpError(_error.Error):
    """
    Represents ``outp`` errors.
    """

    pass
