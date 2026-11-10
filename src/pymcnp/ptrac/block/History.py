from __future__ import annotations

import typing
import dataclasses

from ... import abc
from ..Block import Block
from .Event import Event
from .Event import EventSource
from .Event import EventBank
from .Event import EventSurface
from .Event import EventCollision
from .Event import EventTermination


_KINDS: dict[int, type[Event]] = {
    1000: EventSource,
    2000: EventBank,
    3000: EventSurface,
    4000: EventCollision,
    5000: EventTermination,
}


def _kind(code: str) -> type[Event] | None:
    """
    Gets the event block class for PTRAC event codes, e.g., ``1000`` or ``-2013``, ``None`` for the end of a history (``9000``).

    Raises:
        Error: Invalid event type.
    """

    try:
        number = abs(int(code))
    except ValueError:
        raise abc.Error('Invalid event type.', f'{code=}')

    return _KINDS.get(2000 if 2000 <= number < 3000 else number)


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
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding history blocks.

        Parameters:
            source: Source string to compile.

        Returns:
            History block corresponding to ``source``.
        """

        generator = cls.from_mcnp_iter(source)
        while True:
            try:
                next(generator)
            except StopIteration as stop:
                return stop.value

    @classmethod
    def from_mcnp_iter(cls, source: str) -> typing.Generator[tuple[Event, str], None, tuple[typing.Self, str]]:
        """
        Compiles source strings into their corresponding history blocks iteratively.

        Parameters:
            source: Source string to compile.

        Each event block's ``type`` announces the type of the next event (the ``i`` line's ``event_type`` the first), which picks the event block class to parse.

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
        kind = _kind(event_type)
        while kind is not None:
            try:
                item, source = kind.from_mcnp(source)
                yield item, source
                items.append(item)
                kind = _kind(item.type)
            except abc.Error:
                if spaces:
                    source = spaces.pop(-1).to_mcnp() + source
                break

            # The event announcing the end of the history (9000) is the last one.
            if kind is None:
                break

            try:
                space, source = abc.Terminal[r'\n'].from_mcnp(source)
                spaces.append(space)
            except abc.Error:
                break

        events = cls._fields['events'][0](*items, spaces=spaces)

        return cls(
            blank=blank,
            nps=nps,
            event_type=event_type,
            number=number,
            tfc=tfc,
            newline=newline,
            events=events,
        ), source

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
