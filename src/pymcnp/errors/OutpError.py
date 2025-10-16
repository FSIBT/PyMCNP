from . import _error


class OutpCode(_error.Code):
    """
    Represents `outp` error codes.

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
    Represents `outp` errors.
    """

    def __str__(self):
        info = str(self.info).split('\n')
        info = '\n> '.join(info[: _error.CUTOFF] + ['...'] if len(info) > _error.CUTOFF else info)

        if self.code == OutpCode.SYNTAX_FILE:
            return f'OUTP file not recognized.\n> {info}'
        if self.code == OutpCode.SYNTAX_TABLE:
            return f'OUTP table not recognized.\n> {info}'
        if self.code == OutpCode.SEMANTICS_FILE:
            return f'Invalid OUTP file.\n> {info}'
        if self.code == OutpCode.SEMANTICS_TABLE:
            return f'Invalid OUTP table.\n> {info}'
