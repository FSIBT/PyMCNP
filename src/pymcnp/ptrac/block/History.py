from __future__ import annotations

import typing
import dataclasses
import collections.abc

import pandas

from ... import abc
from ..Block import Block
from .Event import Event
from .Event import EventSource
from .Event import EventBank
from .Event import EventSurface
from .Event import EventCollision
from .Event import EventTermination

if typing.TYPE_CHECKING:
    from ..Track import Track


class History(abc.symbol.WithMcnpIter, abc.symbol.WithDataIter, Block):
    """
    Represents history blocks.

    Attributes:
        nps: history block i line ``nps`` parameter.
        event_type: history block i line ``event_type`` parameter.
        number: history block i line ``number`` parameter.
        tfc: history block i line ``tfc`` parameter.
        newline: event block ``r'\\n'`` symbol.
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

        if not self.events:
            raise abc.Error('Invalid value.', f'{self.events=}')

        if self.events[-1].type != '      9000':
            raise abc.Error('Invalid value.', f'{self.events[-1].type=}')

    @classmethod
    def _from_mcnp_iter_at(cls, source: str, pos: int, returning: bool = False) -> typing.Generator[Event, None, tuple[typing.Self | None, int]]:
        """
        Compiles source strings at positions into their corresponding history blocks iteratively.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.
            returning: Flag to/to not build the history block.

        Yields:
            Events of history blocks.

        Returns:
            History block corresponding to ``source`` at ``pos`` if ``returning`` (else ``None``), and the position where it ends.
        """

        events = _events_at(cls, source, pos, returning)
        try:
            while True:
                yield next(events)[0]
        except StopIteration as stop:
            return stop.value

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
    def tracks(self) -> collections.abc.Iterator[Track]:
        """
        History block tracks, with banked particles linked to their parents; see ``pymcnp.ptrac.Track``.
        """

        from ... import ptrac
        from ...Ptrac import _history_events

        yield from ptrac.tracks(_history_events(self))


@dataclasses.dataclass
class HistoryTruncated:
    """
    Represents history blocks that were cut short, e.g., the last one of a ptrac file of a killed run.

    This is not a symbol, so ``History`` keeps requiring the event announcing type 9000.
    It has the attributes of ``History`` that are needed to read events.

    Attributes:
        nps: History number.
        event_type: Type of the first event.
        events: Events that are complete.
    """

    nps: str
    event_type: str
    events: list[Event]

    @classmethod
    def from_mcnp(cls, source: str) -> HistoryTruncated:
        """
        Reads as many events of a cut-short history block as there are.

        Parameters:
            source: Source string to read.

        Returns:
            Truncated history block corresponding to ``source``.

        Raises:
            Error: Invalid history line.
            Error: Expected history.
        """

        events: list[Event] = []
        text = source + '\n'
        end = None
        for event, end in _events_at(History, text, 0, returning=False):
            events.append(event)
        remainder = source.partition('\n')[2] if end is None else text[end:]

        # Only the event that was being written when the file was cut (its J and P lines) may be left over.
        if len(remainder.removeprefix('\n').rstrip('\n').split('\n')) > 2 and remainder.strip():
            raise abc.Error('Expected history.', f'{remainder[:80]!r}')

        return cls(nps=source[1:11], event_type=source[11:21], events=events)

    @property
    def tracks(self) -> collections.abc.Iterator[Track]:
        """
        History block tracks, with banked particles linked to their parents; see ``pymcnp.ptrac.Track``.
        """

        from ... import ptrac
        from ...Ptrac import _history_events

        yield from ptrac.tracks(_history_events(self))


_BLANK = abc.Terminal[r' ']
_TEN = abc.Terminal[r'.{10}']
_THIRTEEN = abc.Terminal[r'.{13}']
_EMPTY = abc.Terminal[r'']
_NEWLINE = abc.Terminal[r'\n']
_EVENT_TYPE = abc.Terminal[r'      [13459]000|     [- ]20(?:0[1-9]|1\d|2[0-6]|3[0-4])']
_EVENTS = abc.Array[Event, _NEWLINE]
_KINDS: dict[str, type[Event]] = {
    '      1000': EventSource,
    '      3000': EventSurface,
    '      4000': EventCollision,
    '      5000': EventTermination,
}


def _events_at(cls: type[History], source: str, pos: int, returning: bool) -> typing.Generator[tuple[Event, int], None, tuple[History | None, int]]:
    """
    Compiles history blocks at positions, yielding each event with the position where it ends.

    Parameters:
        cls: History block class to build.
        source: Source string to compile.
        pos: Position in ``source`` to compile at.
        returning: Flag to/to not build the history block.

    Yields:
        Events of history blocks and the positions where they end.

    Returns:
        History block corresponding to ``source`` at ``pos`` if ``returning`` (else ``None``), and the position where it ends.
    """

    blank, pos = _BLANK._from_mcnp_at(source, pos)
    nps, pos = _TEN._from_mcnp_at(source, pos)
    event_type, pos = _EVENT_TYPE._from_mcnp_at(source, pos)

    try:
        number, pos = _TEN._from_mcnp_at(source, pos)
    except abc.Error:
        number, pos = _EMPTY._from_mcnp_at(source, pos)

    try:
        tfc, pos = _THIRTEEN._from_mcnp_at(source, pos)
    except abc.Error:
        tfc, pos = _EMPTY._from_mcnp_at(source, pos)

    newline, pos = _NEWLINE._from_mcnp_at(source, pos)

    kind: str = event_type
    spaces: list[abc.Terminal] = []
    items: list[Event] = []

    while True:
        try:
            if kind == '      9000':
                if spaces:
                    pos -= len(spaces.pop(-1))
                break

            item, pos = _KINDS.get(kind, EventBank)._from_mcnp_at(source, pos)

            yield item, pos

            kind = item.type
            if returning:
                items.append(item)
        except abc.Error:
            if spaces:
                pos -= len(spaces.pop(-1))
            break

        try:
            space, pos = _NEWLINE._from_mcnp_at(source, pos)
            if returning:
                spaces.append(space)
            else:
                spaces = [space]
        except abc.Error:
            break

    if not returning:
        return None, pos

    return cls(
        blank=blank,
        nps=nps,
        event_type=event_type,
        number=number,
        tfc=tfc,
        newline=newline,
        events=_EVENTS(*items, spaces=spaces),
    ), pos
