import typing
import dataclasses

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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    label: typing.Annotated[abc.Terminal, r' Tally bin boundaries:\n'] = dataclasses.field(kw_only=True)
    boundaries: typing.Annotated[abc.Array, line.Boundary, typing.Annotated[abc.Terminal, r'\n']] = dataclasses.field(kw_only=True)

    def __post_init__(self) -> None:
        """
        Validates bin blocks.

        Raises:
            Error: Invalid value.
        """

        if len(self.boundaries) == 0:
            raise abc.Error('Invalid value.', f'{self.boundaries=}')
