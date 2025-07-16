from . import _error


class InpCode(_error.Code):
    """
    Represents ``inp`` error codes.

    Notes:
        0x - Syntax
        1x - Semantics
        x0 - File
        x1 - Card
        x2 - Option
        x3 - Entry
    """

    SYNTAX_FILE = 0
    SYNTAX_CARD = 1
    SYNTAX_OPTION = 2
    SYNTAX_ENTRY = 3

    SEMANTICS_FILE = 10
    SEMANTICS_CARD = 11
    SEMANTICS_OPTION = 12
    SEMANTICS_ENTRY = 13


class InpError(_error.Error):
    """
    Represents ``inp`` errors.
    """

    pass
