from . import _error


class TypesCode(_error.Code):
    """
    Represents ``types`` error codes.

    Notes:
        0x - Syntax
        1x - Semantics
        x0 - Type
    """

    SYNTAX_TYPE = 0

    SEMANTICS_TYPE = 10


class TypesError(_error.Error):
    """
    Represents ``types`` errors.
    """

    pass
