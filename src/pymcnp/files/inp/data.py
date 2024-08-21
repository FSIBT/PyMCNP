"""
'data' contains classes representing INP data card blocks.

'data' packages the 'Data' class, providing an importable interface
for INP data cards.
"""


from typing import Self

from .block import Block
from .datum import Datum
from .._utils import parser


class Data(Block):
    """
    'Data' represents MNCP INP data card blocks.

    'Data' abstracts the INP data card syntax element and it
    encapsulates all functionallity for parsing data cards.
    """

    def __init__(self) -> Self:
        """
        '__init__' initalizes 'Data'.
        """

        super().__init__()

    @classmethod
    def from_mcnp(cls, source: str) -> Self:
        """
        'from_mcnp' generates data block objects from INP.

        Parameters:
            source : INP to parse.

        Returns:
            block (Data): Data block object.
        """

        block = cls()

        lines = parser.Preprocessor.process_inp(source).split("\n")
        for line in lines:
            if line == "":
                break
            block.append(Datum.from_mcnp(line))

        return block

    def to_mcnp(self) -> str:
        """
        'to_mcnp' generates INP from data block objects.

        Returns:
            source : INP for data block objects.
        """

        return "\n".join([datum.to_mcnp() for datum in self._cards.values()])

    def to_arguments(self) -> list:
        """
        'to_arguments' generates lists of datum card objects.

        Returns:
            arguments (list): List of datum block objects.
        """

        return [card.to_arguments() for card in self._cards.values()]
