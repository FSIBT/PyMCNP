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
    def source(self) -> EventSource | EventBank:
        """
        source: Track source event.
        """

        assert isinstance(self.events[0], EventSource | EventBank)
        return self.events[0]

    @property
    def banks(self) -> tuple[EventBank, ...]:
        """
        Track bank events.
        """

        return tuple(event for event in self.events[1:] if isinstance(event, EventBank))

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

        assert isinstance(self.events[-1], EventTermination)
        return self.events[-1]

    @property
    def particle(self) -> abc.Terminal:
        """
        Track particle.
        """

        return self.source.particle


class History(abc.symbol.WithMcnpIter, abc.symbol.WithDataIter, Block):
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

    def __post_init__(self) -> None:
        """
        Validates history blocks.
        """

        if self.events[-1].type != '      9000':
            raise abc.Error('Invalid value.', f'{self.events[-1].type=}')

    @classmethod
    def from_mcnp_iter(cls, source: str, returning: bool = False) -> typing.Generator[tuple[Event, str], None, tuple[typing.Self, str] | None]:
        """
        Compiles source strings into their corresponding history blocks iteratively.

        Parameters:
            source: Source string to compile.
            returning: Flag to/to not return.

        Yields:
            Events of history blocks.

        Returns:
            History block corresponding to `source`.
        """

        blank, source = abc.Terminal[r' '].from_mcnp(source)
        nps, source = abc.Terminal[r'.{10}'].from_mcnp(source)
        event_type, source = abc.Terminal[r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])'].from_mcnp(source)

        try:
            number, source = abc.Terminal[r'.{10}'].from_mcnp(source)
        except abc.Error:
            number, source = abc.Terminal[r''].from_mcnp(source)

        try:
            tfc, source = abc.Terminal[r'.{13}'].from_mcnp(source)
        except abc.Error:
            tfc, source = abc.Terminal[r''].from_mcnp(source)

        newline, source = abc.Terminal[r'\n'].from_mcnp(source)

        kind: str = event_type
        spaces: list[abc.Terminal] = []
        if returning:
            items: list[Event] = []

        while True:
            try:
                match kind:
                    case '      1000':
                        item, source = EventSource.from_mcnp(source)
                    case '      3000':
                        item, source = EventSurface.from_mcnp(source)
                    case '      4000':
                        item, source = EventCollision.from_mcnp(source)
                    case '      5000':
                        item, source = EventTermination.from_mcnp(source)
                    case '      9000':
                        if spaces:
                            source = spaces.pop(-1).to_mcnp() + source
                        break
                    case _:
                        item, source = EventBank.from_mcnp(source)

                yield item, source

                kind = item.type
                if returning:
                    items.append(item)
            except abc.Error:
                if spaces:
                    source = spaces.pop(-1).to_mcnp() + source
                break

            try:
                space, source = abc.Terminal[r'\n'].from_mcnp(source)
                if returning:
                    spaces.append(space)
                else:
                    spaces = [space]
            except abc.Error:
                break

        if returning:
            events = abc.Array[Event, abc.Terminal[r'\n']](*items, spaces=spaces)

        if returning:
            return cls(
                blank=blank,
                nps=nps,
                event_type=event_type,
                number=number,
                tfc=tfc,
                newline=newline,
                events=events,
            ), source

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for history block events.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for history block events.

        Returns:
            Pandas dataframe for all history block events.
        """

        if returning:
            frames = []

        for event in self.events:
            yield (frame := event.to_dataframe())

            if returning:
                frames.append(frame)

        if returning:
            return pandas.concat(frames, ignore_index=True)

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
                source = i + 1

                while banks > 0:
                    stack.append(track)
                    banks -= 1
