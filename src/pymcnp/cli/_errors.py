"""
Contains classes representing errors for CLI.
"""

import enum
from typing import Final


class CliCode(enum.Enum):
    """
    Represents ``CliError`` error codes.

    Notes:
        10X: Value, ``Run``.
    """

    INVALID_INP = 100
    INVALID_PATH = 101
    INVALID_PREHOOK = 102
    INVALID_POSTHOOK = 103
    INVALID_COMMAND = 104


class CliError(Exception):
    """
    Represents cli errors.

    PyMCNP raises ``CliError`` while doing things with MCNP.

    Attributes:
        code: Error code.
        info: Error string.
    """

    def __init__(self, code: CliCode, info: str):
        """
        Initializes ``CliError``

        Parameters:
            code: Error code.
            info: Error string.
        """

        self.code: Final[CliCode] = code
        self.info: Final[str] = info

    def __str__(self) -> str:
        """
        Stringifies ``CliError``.
        """

        head = ''
        hint = ''

        match self.code:
            case CliCode.INVALID_INP:
                head += 'Invalid ``Inp`` object.'
                hint += ''
            case CliCode.INVALID_PATH:
                head += 'Invalid ``pathlib.Path`` object.'
                hint += ''
            case CliCode.INVALID_PREHOOK:
                head += 'Invalid prehook executable.'
                hint += 'Prehook executables need ``main`` functions.'
            case CliCode.INVALID_POSTHOOK:
                head += 'Invalid posthook executable.'
                hint += 'Posthook executables need ``main`` functions.'
            case CliCode.INVALID_COMMAND:
                head += 'Invalid command.'
                hint += 'Terminal command not found.'
            case _:
                head += "I'm working on it! :)"
                hint += ''

        if hint:
            return f'\n\033[31;4;1mCliError[{self.code.name}]\033[0m: {head}\n|\n| {repr(self.info)}\n|\n| \033[35;4mHint\033[0m: {hint}\n|'
        else:
            return f'\n\033[31;4;1mCliError[{self.code.name}]\033[0m: {head}\n|\n| {repr(self.info)}\n|'
