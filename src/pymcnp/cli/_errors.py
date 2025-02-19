"""
Contains classes representing errors for CLI.
"""

import enum
from typing import Final


class CliCode(enum.Enum):
    """
    Represents ``CliError`` error codes.

    Notes:
        10X: System.
        11X: Value, ``Run``.
    """

    INVALID_INP = 110
    INVALID_PATH = 111
    INVALID_PREHOOK = 112
    INVALID_POSTHOOK = 113
    INVALID_COMMAND = 114


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
            return f'[red][bold]InpError[{self.code.name}]:[/][/] {head}\n\n``{self.info[:]}``\n\n[magenta][bold]Hint:[/bold][/magenta] {hint}'
        else:
            return f'[red][bold]InpError[{self.code.name}]:[/][/] {head}\n\n``{self.info[:]}``'
