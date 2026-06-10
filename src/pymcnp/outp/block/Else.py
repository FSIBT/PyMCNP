import typing
import dataclasses

from ... import abc
from ..Block import Block


class Else(Block):
    """
    Represents else blocks.

    Attributes:
        text: Text of block.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    text: typing.Annotated[abc.Terminal, r'[\s\S]+?(?=\n1\w+|\Z)']
