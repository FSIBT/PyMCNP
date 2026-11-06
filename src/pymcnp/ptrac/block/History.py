from __future__ import annotations

import typing

from ... import abc
from ..Block import Block
from .. import line
from .Event import Event


class History(Block):
    """
    Represents history blocks.

    Attributes:
        i: history block i line.
        newline: event block `r'\\n'` symbol.
        events: history block events.
    """

    i: line.I
    newline: typing.Annotated[abc.Terminal, r'\n']
    events: typing.Annotated[abc.Array, Event, typing.Annotated[abc.Terminal, r'\n']]

    @classmethod
    def from_mcnp_iter(cls, source: str) -> typing.Generator[tuple[Event, str], None, tuple[typing.Self, str]]:
        """
        Compiles source strings into their corresponding history blocks iteratively.

        Parameters:
            source: Source string to compile.

        Yields:
            History block events corresponding to `source`.

        Returns:
            History blocks corresponding to `source`.
        """

        blank, source = abc.Terminal[r' '].from_mcnp(source)
        nps, source = abc.Terminal[r'.{10}'].from_mcnp(source)
        event_type, source = abc.Terminal[r'.{10}'].from_mcnp(source)

        try:
            number, source = abc.Terminal[r'.{10}'].from_mcnp(source)
        except abc.Error:
            number, source = abc.Terminal[r''].from_mcnp(source)

        try:
            tfc, source = abc.Terminal[r'.{13}'].from_mcnp(source)
        except abc.Error:
            tfc, source = abc.Terminal[r''].from_mcnp(source)

        newline, source = abc.Terminal[r'\n'].from_mcnp(source)

        spaces: list[abc.Terminal] = []
        items: list[abc.Symbol] = []
        while True:
            try:
                item, source = Event.from_mcnp(source)
                yield item, source
                items.append(item)
            except abc.Error:
                if spaces:
                    source = spaces.pop(-1).to_mcnp() + source
                break

            try:
                space, source = abc.Terminal[r'\n'].from_mcnp(source)
                spaces.append(space)
            except abc.Error:
                break

        events = abc.Array[Event, abc.Terminal[r'\n']](*items, spaces=spaces)

        return cls(
            blank=blank,
            nps=nps,
            event_type=event_type,
            number=number,
            tfc=tfc,
            newline=newline,
            events=events,
        ), source
