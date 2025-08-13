from . import _error


class TypesCode(_error.Code):
    """
    Represents `types` error codes.

    Notes:
        0x - Syntax
        1x - Semantics
        x0 - Type
    """

    SYNTAX_TYPE = 0

    SEMANTICS_TYPE = 10


class TypesError(_error.Error):
    """
    Represents `types` errors.
    """

    def __str__(self):
        info = str(self.info).split('\n')
        info = '\n> '.join(info[: _error.CUTOFF] + ['...'] if len(info) > _error.CUTOFF else info)

        if self.code == TypesCode.SYNTAX_TYPE:
            return f'MCNP data type not recognized.\n> {info}'
        if self.code == TypesCode.SEMANTICS_TYPE:
            return f'Invalid MCNP data type.\n> {info}'
