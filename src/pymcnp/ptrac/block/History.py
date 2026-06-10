import typing
import dataclasses

from ... import abc
from ..Block import Block
from .. import line
from .Event import Event


class History(Block):
    """
    Represents history blocks.

    Attributes:
        i: history block `i` parameter.
        events: history block `events` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    i: line.I
    newline: typing.Annotated[abc.Terminal, r'\n']
    events: typing.Annotated[abc.Array, Event, typing.Annotated[abc.Terminal, r'\n']]
