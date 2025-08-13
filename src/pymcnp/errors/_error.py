import enum
import typing


CUTOFF: typing.Final[int] = 4


class Code(enum.EnumMeta):
    """
    Represents generic PyMCNP error codes.
    """

    pass


class Error(Exception):
    """
    Represents generic PyMCNP errors.

    Attributes:
        code: Error code.
        info: Error string.
    """

    def __init__(self, code: enum.Enum, info: str):
        """
        Initializes `Error`

        Parameters:
            code: Error code.
            info: Error string.

        Returns:
            `Error`.
        """

        self.code: typing.Final[Code] = code
        self.info: typing.Final[str] = info
