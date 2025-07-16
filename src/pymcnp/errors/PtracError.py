from . import _error


class PtracCode(_error.Code):
    """
    Represents ``ptrac`` error codes.

    Notes:
        0x - Syntax
        1x - Semantics
    """

    SYNTAX_FILE = 0
    SYNTAX_BLOCK = 1
    SYNTAX_LINE = 2
    SYNTAX_KEYWORD = 3

    SEMANTICS_FILE = 10
    SEMANTICS_BLOCK = 11
    SEMANTICS_LINE = 12
    SEMANTICS_KEYWORD = 13


class PtracError(_error.Error):
    """
    Represents ``ptrac`` errors.
    """

    pass
