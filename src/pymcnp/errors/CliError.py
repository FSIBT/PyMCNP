from . import _error


class CliCode(_error.Code):
    """
    Represents `cli` error codes.
    """

    RUNTIME_PATH = 0
    RUNTIME_DOER = 1


class CliError(_error.Error):
    """
    Represents `cli` errors.
    """

    def __str__(self):
        info = str(self.info).split('\n')
        info = '\n> '.join(info[: _error.CUTOFF] + ['...'] if len(info) > _error.CUTOFF else info)

        if self.code == CliCode.RUNTIME_PATH:
            return f'Bad path.\n> {info}'
        if self.code == CliCode.RUNTIME_DOER:
            return f'Bad parameter.\n> {info}'
