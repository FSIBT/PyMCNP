import typing

from ... import abc
from ..Block import Block
from .. import line


class Bin(Block):
    """
    Represents bin blocks.

    Attributes:
        label: bin block ` Tally bin boundaries:\\n` symbol.
        boundaries: bin block boundaries.
    """

    label: typing.Annotated[abc.Terminal, r' Tally bin boundaries:\n']
    boundaries: typing.Annotated[abc.Array, line.Boundary, typing.Annotated[abc.Terminal, r'\n']]

    def __post_init__(self) -> None:
        """
        Validates bin blocks.

        Raises:
            Error: Invalid value.
        """

        if len(self.boundaries) == 0:
            raise abc.Error('Invalid value.', f'{self.boundaries=}')
