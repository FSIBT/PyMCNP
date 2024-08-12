"""
'ptrac'
"""


from typing import Self

from .header import Header
from .history import History


class Ptrac:
    """
    'Ptrac'
    """

    def __init__(self) -> Self:
        """
        '__init__'
        """

        self.header: Header = None
        self.histories: list[History] = None

    @classmethod
    def from_mcnp(cls, source: str) -> Self:
        """
        'from_mcnp'
        """

        ptrac = cls()

        # Processing Header
        ptrac.header, lines = Header().from_mcnp(source)

        # Processing History
        histories = []

        while lines:
            history, lines = History().from_mcnp(lines, ptrac.header)
            histories.append(history)

        ptrac.histories = tuple(histories)

        return ptrac

    @classmethod
    def from_mcnp_file(cls, filename: str):
        """
        'from_mcnp_file'
        """

        with open(filename) as file:
            source = "".join(file.readlines())

        return cls.from_mcnp(source)

    def to_arguments(self) -> dict:
        """
        'to_arguments'
        """

        return {
            "header": self.header.to_arguments(),
            "histories": [history.to_arguments() for history in self.histories],
        }
