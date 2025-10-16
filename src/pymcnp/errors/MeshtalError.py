from . import _error


class MeshtalCode(_error.Code):
    """
    Represents `meshtal` error codes.

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
    Represents `meshtal` errors.
    """

    def __str__(self):
        info = str(self.info).split('\n')
        info = '\n> '.join(info[: _error.CUTOFF] + ['...'] if len(info) > _error.CUTOFF else info)

        if self.code == MeshtalCode.SYNTAX_FILE:
            return f'MESHTAL file not recognized.\n> {info}'
        if self.code == MeshtalCode.SYNTAX_BLOCK:
            return f'MESHTAL table not recognized.\n> {info}'
        if self.code == MeshtalCode.SYNTAX_LINE:
            return f'MESHTAL line not recognized.\n> {info}'
        if self.code == MeshtalCode.SEMANTICS_FILE:
            return f'Invalid MESHTAL file.\n> {info}'
        if self.code == MeshtalCode.SEMANTICS_BLOCK:
            return f'Invalid MESHTAL table.\n> {info}'
        if self.code == MeshtalCode.SEMANTICS_LINE:
            return f'Invalid MESHTAL line.\n> {info}'
