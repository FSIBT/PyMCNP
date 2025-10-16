from . import _error


class InpCode(_error.Code):
    """
    Represents `inp` error codes.

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
    Represents `inp` errors.
    """

    def __str__(self):
        info = str(self.info).split('\n')
        info = '\n> '.join(info[: _error.CUTOFF] + ['...'] if len(info) > _error.CUTOFF else info)

        if self.code == InpCode.SYNTAX_FILE:
            return f'INP file not recognized.\n> {info}'
        if self.code == InpCode.SYNTAX_CARD:
            return f'INP card not recognized.\n> {info}'
        if self.code == InpCode.SYNTAX_OPTION:
            return f'INP option not recognized.\n> {info}'
        if self.code == InpCode.SYNTAX_ENTRY:
            return f'INP entry not recognized.\n> {info}'
        if self.code == InpCode.SEMANTICS_FILE:
            return f'Invalid INP file.\n> {info}'
        if self.code == InpCode.SEMANTICS_CARD:
            return f'Invalid INP card.\n> {info}'
        if self.code == InpCode.SEMANTICS_OPTION:
            return f'Invalid INP option.\n> {info}'
        if self.code == InpCode.SEMANTICS_ENTRY:
            return f'Invalid INP entry.\n> {info}'
