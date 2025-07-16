from . import _error


class CliCode(_error.Code):
    """
    Represents ``cli`` error codes.

    Notes:
        0x - Runtime
        x0 - Check
        x1 - Convert
        x2 - Plot
        x3 - Run
        x4 - Visualize
    """

    RUNTIME_PATH = 0
    RUNTIME_DOER = 1


class CliError(_error.Error):
    """
    Represents ``cli`` errors.
    """

    pass
