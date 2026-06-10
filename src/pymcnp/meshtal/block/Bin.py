import typing
import dataclasses

from ... import abc
from ..Block import Block
from .. import line


class Bin(Block):
    """
    Represents bin blocks.

    Attributes:
        label: bin block `label` parameter.
        bins: bin block `bins` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    label: typing.Annotated[abc.Terminal, r' Tally bin boundaries:\n']
    bins: typing.Annotated[abc.Array, line.Boundary, typing.Annotated[abc.Terminal, r'\n']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
