from . import _error


class MeshtalCode(_error.Code):
    """
    Represents ``meshtal`` error codes.

    Notes:
        0x - Syntax
        1x - Semantics
    """

    SYNTAX_FILE = 0
    SYNTAX_BLOCK = 1
    SYNTAX_LINE = 2

    SEMANTICS_FILE = 10
    SEMANTICS_BLOCK = 11
    SEMANTICS_LINE = 12


class MeshtalError(_error.Error):
    """
    Represents ``meshtal`` errors.
    """

    pass
