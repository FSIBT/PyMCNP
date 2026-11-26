from __future__ import annotations

import sys
import typing
import warnings
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
from .Header import Header
from .Header import _event_lines

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
    def _from_mcnp_iter_at(cls, source: str, pos: int, returning: bool = False, *, _kinds: dict[str, type[Event]] | None = None) -> typing.Generator[Event, None, tuple[typing.Self | None, int]]:
        """
        Compiles source strings at positions into their corresponding history blocks iteratively.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.
            returning: Flag to/to not build the history block.
            _kinds: Event block class per event type, chosen from the PTRAC header by ``_kinds``; without it, each event
                block is parsed by trying its forms.

        Yields:
            Events of history blocks.

        Returns:
            History block corresponding to ``source`` at ``pos`` if ``returning`` (else ``None``), and the position where it ends.
        """

        events = _events_at(cls, source, pos, returning, _kinds or _KINDS)
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
    def from_mcnp(cls, source: str) -> tuple[HistoryTruncated, str]:
        """
        Reads as many events of a cut-short history block as there are.

        Parameters:
            source: Source string to read.

        Returns:
            Truncated history block corresponding to ``source``, and the
            remainder: the lines of the event that was cut short, if any.

        Raises:
            Error: Invalid history line.
            Error: Expected history.
        """

        truncated, remainder = _truncated(source, _KINDS)
        return cls(nps=truncated.nps, event_type=truncated.event_type, events=truncated.events), remainder

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
# Event block class per event type, in the order of the header's event lines; bank events have many type codes.
_BANK = 'bank'
_KINDS: dict[str, type[Event]] = {
    '      1000': EventSource,
    _BANK: EventBank,
    '      3000': EventSurface,
    '      4000': EventCollision,
    '      5000': EventTermination,
}
_NAMES = {'      1000': 'source', _BANK: 'bank', '      3000': 'surface', '      4000': 'collision', '      5000': 'termination'}

# Variable IDs of the J-line fields of event blocks (MCNP manual, PTRAC file format).
_IDS = {
    'pbl_i_node': 8,
    'nsr': 9,
    'nxs_2_iex': 10,
    'ntyn': 11,
    'pbl_i_mtp': 11,
    'nsf_pbl_i_jsu': 12,
    'angle': 13,
    'nter': 14,
    'branch_number': 15,
    'pbl_i_ipt': 16,
    'ncl_pbl_i_icl': 17,
    'mat_pbl_i_icl': 18,
    'pbl_i_ncp': 19,
}


def _shape(form: type[Event]) -> tuple[list[int], int]:
    """
    Finds the variable IDs of the J-line values after ``type`` and the number of P-line values of event block forms.
    """

    names = list(form._fields)
    return [_IDS[name] for name in names[names.index('type') + 1 : names.index('newline')]], len(names) - names.index('blank_1') - 1


def _kinds(header: Header) -> dict[str, type[Event]]:
    """
    Chooses the event block class per event type from the variable IDs of PTRAC headers.

    An event type gets the form whose J-line variable IDs and number of P-line values are the header's, e.g.,
    ``EventSource_3`` for ``8 9 17 18 19`` and 9 P values. An event type that no form fits, or a header whose counts
    and IDs do not fit together, keeps the class whose forms are tried in turn, as without a header; event types that
    no form fits get one ``abc.Warning``.

    Returns:
        Event block class per event type, as ``_KINDS``.
    """

    kinds = dict(_KINDS)
    lines = _event_lines(header)
    if lines is not None:
        unmatched = []
        for (code, name), line in zip(_NAMES.items(), lines):
            forms = [form for form in _KINDS[code]._forms if _shape(form) == line]
            if forms:
                kinds[code] = forms[0]
            else:
                unmatched.append(f'{name} (J line {" ".join(map(str, line[0]))}, {line[1]} P values)')
        if unmatched:
            warning = abc.Warning(
                'PTRAC header layout has no event block form.',
                f'{", ".join(unmatched)}: these event blocks are parsed by trial, so their ptrac.block field names may not follow the header; stream and to_dataframe do',
            )
            warnings.warn_explicit(warning, abc.Warning, __file__, sys._getframe().f_lineno, module=__name__)

    return kinds


def _event_at(kinds: dict[str, type[Event]], kind: str, source: str, pos: int) -> tuple[Event, int]:
    """
    Compiles the event block of type ``kind`` at positions, with the class ``kinds`` gives; if that form does not fit
    the lines, its forms are tried in turn, as without a header.
    """

    form = kinds.get(kind, kinds[_BANK])
    try:
        return form._from_mcnp_at(source, pos)
    except abc.Error:
        base = _KINDS.get(kind, _KINDS[_BANK])
        if form is base:
            raise
        return base._from_mcnp_at(source, pos)


def _events_at(cls: type[History], source: str, pos: int, returning: bool, kinds: dict[str, type[Event]]) -> typing.Generator[tuple[Event, int], None, tuple[History | None, int]]:
    """
    Compiles history blocks at positions, yielding each event with the position where it ends.

    Parameters:
        cls: History block class to build.
        source: Source string to compile.
        pos: Position in ``source`` to compile at.
        returning: Flag to/to not build the history block.
        kinds: Event block class per event type, see ``_kinds``.

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

            item, pos = _event_at(kinds, kind, source, pos)

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


def _truncated(source: str, kinds: dict[str, type[Event]]) -> tuple[HistoryTruncated, str]:
    """
    Reads cut-short history blocks, as ``HistoryTruncated.from_mcnp``, with the event block classes ``kinds``.
    """

    events: list[Event] = []
    text = source + '\n'
    end = None
    for event, end in _events_at(History, text, 0, False, kinds):
        events.append(event)
    # The remainder is from ``source``, without the newline added to ``text`` or the one before the cut event.
    remainder = source.partition('\n')[2] if end is None else source[end:].removeprefix('\n')

    # Only the event that was being written when the file was cut (its J and P lines) may be left over.
    if len(remainder.rstrip('\n').split('\n')) > 2 and remainder.strip():
        raise abc.Error('Expected history.', f'{remainder[:80]!r}')

    return HistoryTruncated(nps=source[1:11], event_type=source[11:21], events=events), remainder


def _history(source: str, kinds: dict[str, type[Event]]) -> tuple[History, str]:
    """
    Compiles source strings into history blocks, as ``History.from_mcnp``, with the event block classes ``kinds``.
    """

    events = _events_at(History, source, 0, True, kinds)
    try:
        while True:
            next(events)
    except StopIteration as stop:
        history, end = stop.value

    return history, source[end:]
