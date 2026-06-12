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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    label: typing.Annotated[abc.Terminal, r' Tally bin boundaries:\n']
    boundaries: typing.Annotated[abc.Array, line.Boundary, typing.Annotated[abc.Terminal, r'\n']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
