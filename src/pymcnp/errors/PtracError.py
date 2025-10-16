from . import _error


class PtracCode(_error.Code):
    """
    Represents `ptrac` error codes.

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
    Represents `ptrac` errors.
    """

    def __str__(self):
        info = str(self.info).split('\n')
        info = '\n> '.join(info[: _error.CUTOFF] + ['...'] if len(info) > _error.CUTOFF else info)

        if self.code == PtracCode.SYNTAX_FILE:
            return f'PTRAC file not recognized.\n> {info}'
        if self.code == PtracCode.SYNTAX_BLOCK:
            return f'PTRAC table not recognized.\n> {info}'
        if self.code == PtracCode.SYNTAX_LINE:
            return f'PTRAC line not recognized.\n> {info}'
        if self.code == PtracCode.SYNTAX_KEYWORD:
            return f'PTRAC keyword not recognized.\n> {info}'
        if self.code == PtracCode.SEMANTICS_FILE:
            return f'Invalid PTRAC file.\n> {info}'
        if self.code == PtracCode.SEMANTICS_BLOCK:
            return f'Invalid PTRAC table.\n> {info}'
        if self.code == PtracCode.SEMANTICS_LINE:
            return f'Invalid PTRAC line.\n> {info}'
        if self.code == PtracCode.SEMANTICS_KEYWORD:
            return f'Invalid PTRAC keyword.\n> {info}'
