from __future__ import annotations

import typing
import dataclasses

import pandas

from ... import abc
from ..Block import Block
from .Event import Event
from .Event import EventSource
from .Event import EventBank
from .Event import EventSurface
from .Event import EventCollision
from .Event import EventTermination


@dataclasses.dataclass
class Track:
    """
    Represents tracks of particles.

    Attributes:
        history: Track history block.
        events: Track events.
        parent: Parent track.
    """

    history: History
    events: tuple[Event, ...]
    parent: Track | None

    @property
    def source(self) -> EventSource:
        """
        source: Track source event.
        """

        return next(event for event in self.events if isinstance(event, EventSource))

    @property
    def banks(self) -> tuple[EventBank, ...]:
        """
        Track bank events.
        """

        return tuple(event for event in self.events if isinstance(event, EventBank))

    @property
    def surfaces(self) -> tuple[EventSurface, ...]:
        """
        Track surface events.
        """

        return tuple(event for event in self.events if isinstance(event, EventSurface))

    @property
    def collisions(self) -> tuple[EventCollision, ...]:
        """
        Track collision events.
        """

        return tuple(event for event in self.events if isinstance(event, EventCollision))

    @property
    def termination(self) -> EventTermination:
        """
        Track termination event.
        """

        return next(event for event in self.events if isinstance(event, EventTermination))

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes from history blocks.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        if banks := self.banks:
            banks_frame = pandas.concat((event.to_dataframe() for event in banks), ignore_index=True)
        else:
            banks_frame = pandas.DataFrame()

        if surfaces := self.surfaces:
            surfaces_frame = pandas.concat((event.to_dataframe() for event in surfaces), ignore_index=True)
        else:
            surfaces_frame = pandas.DataFrame()

        if collisions := self.collisions:
            collisions_frame = pandas.concat((event.to_dataframe() for event in collisions), ignore_index=True)
        else:
            collisions_frame = pandas.DataFrame()

        return pandas.DataFrame(
            {
                'source': self.source.to_dataframe(),
                'banks': banks_frame,
                'surfaces': surfaces_frame,
                'collisions': collisions_frame,
                'termination': self.termination.to_dataframe(),
            }
        )


class History(Block):
    """
    Represents history blocks.

    Attributes:
        nps: history block i line `nps` parameter.
        event_type: history block i line `event_type` parameter.
        number: history block i line `number` parameter.
        tfc: history block i line `tfc` parameter.
        newline: event block `r'\\n'` symbol.
        events: history block events.
    """

    blank: typing.Annotated[abc.Terminal, r' ']
    nps: typing.Annotated[abc.Terminal, r'.{10}']
    event_type: typing.Annotated[abc.Terminal, r'.{10}']
    number: typing.Annotated[abc.Terminal, r'.{10}'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    tfc: typing.Annotated[abc.Terminal, r'.{13}'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes from history blocks.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        if not self.events:
            return pandas.DataFrame()
        else:
            return pandas.concat((event.to_dataframe() for event in self.events), ignore_index=True)

    @property
    def tracks(self) -> typing.Generator[Track, None, None]:
        """
        History block tracks.
        """

        stack: list[Track] = []
        source: int = 0
        banks: int = 0

        for i, event in enumerate(self.events):
            if isinstance(event, EventBank):
                banks += 1
            elif isinstance(event, EventTermination):
                track = Track(
                    history=self,
                    events=tuple(self.events[source : i + 1]),
                    parent=stack.pop() if stack else None,
                )

                yield track

                while banks > 0:
                    stack.append(track)
                    banks -= 1
