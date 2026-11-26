import re
import typing
import warnings
import pathlib
import collections.abc

import pandas

from . import abc
from . import ptrac
from .ptrac.Event import _Layout, _layout
from .ptrac.block.History import _history, _kinds, _truncated

_REGEX_HISTORY = re.compile(r' *\d+ +(?:[1345]000|-?20\d\d)(?: |$)')
_NEWLINE = abc.Terminal[r'\n']
_NEWLINE_OPTIONAL = abc.Terminal[r'\n?']
_HISTORIES = abc.Array[ptrac.block.History, _NEWLINE]


class Ptrac(abc.file.WithMcnpIter[ptrac.block.History, ptrac.block.Event], abc.file.WithDataIter, abc.File):
    """
    Represents ptrac files.

    Attributes:
        header: ptrac ``header`` parameter.
        histories: ptrac ``histories`` parameter.
    """

    header: ptrac.block.Header
    histories: typing.Annotated[abc.Array, ptrac.block.History, typing.Annotated[abc.Terminal, r'\n']]
    newline: typing.Annotated[abc.Terminal, r'\n?']

    @classmethod
    def _from_mcnp_iter_at(cls, source: str, pos: int, returning: bool = False) -> typing.Generator[typing.Generator[ptrac.block.Event, None, None], None, tuple[typing.Self | None, int]]:
        """
        Compiles source strings at positions into their corresponding ptrac files iteratively.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.
            returning: Flag to/to not build the ptrac file.

        Yields:
            Generators yielding the events of one history each, one per history; an unfinished generator is finished before the next is yielded.

        Returns:
            Ptrac file corresponding to ``source`` at ``pos`` if ``returning`` (else ``None``), and the position where it ends.
        """

        header, pos = ptrac.block.Header._from_mcnp_at(source, pos)
        kinds = _kinds(header)

        stop: bool = False
        spaces: list[abc.Terminal] = []
        if returning:
            items: list[abc.Symbol] = []

        def _generator(first: ptrac.block.Event, history: typing.Generator[ptrac.block.Event, None, tuple[ptrac.block.History | None, int]]) -> typing.Generator[ptrac.block.Event, None, None]:
            nonlocal items
            nonlocal pos
            nonlocal stop
            try:
                yield first
                item, pos = yield from history

                if returning:
                    items.append(item)
            except abc.Error:
                if spaces:
                    pos -= len(spaces.pop(-1))
                stop = True

        while True:
            # Looking ahead: a history whose first event does not compile ends the histories, without a generator.
            history = ptrac.block.History._from_mcnp_iter_at(source, pos, returning=True, _kinds=kinds)
            try:
                first = next(history)
            except abc.Error:
                if spaces:
                    pos -= len(spaces.pop(-1))
                break

            yield (generator := _generator(first, history))

            for _ in generator:
                pass

            if stop:
                break

            try:
                space, pos = _NEWLINE._from_mcnp_at(source, pos)

                if returning:
                    spaces.append(space)
                else:
                    spaces = [space]
            except abc.Error:
                break

        newline, pos = _NEWLINE_OPTIONAL._from_mcnp_at(source, pos)

        if not returning:
            return None, pos

        histories = _HISTORIES(*items, spaces=spaces)
        return cls(header=header, histories=histories, newline=newline), pos

    if typing.TYPE_CHECKING:

        @classmethod
        def from_mcnp_iter(cls, source: str, returning: bool = False) -> typing.Generator[typing.Generator[ptrac.block.Event, None, None], None, tuple[typing.Self, str] | None]: ...

        @classmethod
        def from_file_iter(cls, path: pathlib.Path | str, returning: bool = False) -> typing.Generator[typing.Generator[ptrac.block.Event, None, None], None, tuple[typing.Self, str] | None]: ...

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for histories, one history at a time.

        Columns are those of ``ptrac.Event.to_dict`` plus ``track`` (track number within the history) and ``parent_zaid`` (see ``ptrac.Track``), with nullable ``Int64``, ``string`` and ``float64`` dtypes.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for histories.

        Returns:
            Pandas dataframe for all histories.
        """

        if returning:
            frames = []

        layout = _layout(self.header)
        for history in self.histories:
            yield (frame := ptrac.to_dataframe(_history_rows(history, layout)))

            if returning:
                frames.append(frame)

        if returning:
            return pandas.concat(frames, ignore_index=True) if frames else ptrac.to_dataframe([])

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes for all histories.

        Builds one dataframe from the rows of all histories, which equals concatenating the dataframes of ``to_dataframe_iter``.

        Returns:
            Pandas dataframe for all histories.
        """

        layout = _layout(self.header)
        return ptrac.to_dataframe([row for history in self.histories for row in _history_rows(history, layout)])

    @staticmethod
    def iter_histories(path: pathlib.Path | str) -> collections.abc.Iterator[ptrac.block.History | ptrac.block.HistoryTruncated]:
        """
        Parses ptrac files one history at a time, without holding the file or the histories in memory.

        Parameters:
            path: Path to ptrac file to read.

        Yields:
            History blocks in file order, each parsed once. A last history that is cut short is yielded as far as it goes, as ``ptrac.block.HistoryTruncated``.

        Raises:
            Error: File not found.
            Error: Expected header.
            Error: Expected history.
        """

        reader = _read(path)
        next(reader)
        yield from reader

    @staticmethod
    def stream(path: pathlib.Path | str) -> collections.abc.Iterator[ptrac.Event]:
        """
        Parses ptrac files one event at a time in a single pass, with flat memory use.

        An event block's ``type`` announces the type of the next event, so each event is given its own type here.

        Parameters:
            path: Path to ptrac file to read.

        Yields:
            Events in file order, each with its history number (``nps``) and type.

        Raises:
            Error: File not found.
            Error: Expected history.
        """

        reader = _read(path)
        layout = _layout(typing.cast(ptrac.block.Header, next(reader)))
        for history in reader:
            yield from _history_events(typing.cast(ptrac.block.History | ptrac.block.HistoryTruncated, history), layout)

    @staticmethod
    def tracks(
        path: pathlib.Path | str,
        particle: ptrac.Particle | None = None,
        entered: int | None = None,
    ) -> collections.abc.Iterator[ptrac.Track]:
        """
        Streams the particle tracks of ptrac files, with banked particles linked to their parents.

        Parameters:
            path: Path to ptrac file to read.
            particle: Only yield tracks of this particle.
            entered: Only yield tracks with a surface crossing that enters this cell.

        Yields:
            Tracks in file order; see ``ptrac.Track``.
        """

        yield from ptrac.tracks(Ptrac.stream(path), particle, entered)

    @staticmethod
    def to_parquet(
        path: pathlib.Path | str,
        out: pathlib.Path | str,
        *,
        particle: ptrac.Particle | None = None,
        types: collections.abc.Collection[ptrac.EventType] | None = None,
        cell_entered: int | None = None,
        surface: int | None = None,
        chunk: int = 100_000,
    ) -> int:
        """
        Writes events of a ptrac file to a parquet file in one pass, ``chunk`` rows at a time, so files of any size fit in memory.

        Columns are those of ``Event.to_dict`` plus ``track`` (track number within the history) and ``parent_zaid`` (see ``ptrac.Track``).
        If ``cell_entered`` or ``surface`` is given, only surface crossings that match are written.

        Parameters:
            path: Path to ptrac file to read.
            out: Path to parquet file to write.
            particle: Only write events of tracks of this particle.
            types: Only write events of these types.
            cell_entered: Only write surface crossings entering this cell.
            surface: Only write surface crossings of this surface number (any facet).
            chunk: Number of rows held in memory before they are written.

        Returns:
            Number of rows written.

        Raises:
            Error: Invalid value.
            Error: File not found.
        """

        if chunk < 1:
            raise abc.Error('Invalid value.', f'{chunk=}')

        surfaces_only = cell_entered is not None or surface is not None
        writer = ptrac.ParquetWriter(out)
        rows: list[dict] = []
        total = 0
        try:
            for track in Ptrac.tracks(path, particle, cell_entered):
                events = track.entries(cell=cell_entered, surface=surface) if surfaces_only else track.events
                for event in events:
                    if types is not None and event.type not in types:
                        continue
                    rows.append({**event.to_dict(), 'track': track.index, 'parent_zaid': track.parent_zaid})
                    if len(rows) >= chunk:
                        writer.write(rows)
                        total += len(rows)
                        rows = []
            if rows:
                writer.write(rows)
                total += len(rows)
            writer.close()
        except BaseException:
            writer.abort()
            raise
        return total


def _read(path: pathlib.Path | str) -> collections.abc.Iterator[ptrac.block.Header | ptrac.block.History | ptrac.block.HistoryTruncated]:
    """
    Parses ptrac files one history at a time, yielding the header block first; see ``Ptrac.iter_histories``.
    """

    path = pathlib.Path(path)
    if not path.is_file():
        raise abc.Error('File not found.', f'{path=}')

    def parse(lines: list[str], number: int, complete: bool, last: bool) -> ptrac.block.History | ptrac.block.HistoryTruncated:
        # Only the last history of a file can be cut short (e.g., by a killed run); it is read as far as it goes.
        if complete:
            try:
                history, remainder = _history('\n'.join(lines), kinds)
            except abc.Error:
                if not last:
                    raise
            else:
                if remainder != '':
                    raise abc.Error('Expected history.', f'line {number}: {remainder[:80]!r}')
                return history

        truncated, _ = _truncated('\n'.join(lines), kinds)
        warnings.warn(abc.Warning('Last history is truncated.', f'{path=} nps={truncated.nps.strip()} events kept={len(truncated.events)}'))
        return truncated

    with path.open() as file:
        # Header: everything before the first history line.
        header: list[str] = []
        line = file.readline()
        while line and not (header and _REGEX_HISTORY.match(line) and len(header) >= 6):
            header.append(line.rstrip('\n'))
            line = file.readline()
        if not header:
            raise abc.Error('Expected header.', f'{path=}')
        header_block, remainder = ptrac.block.Header.from_mcnp('\n'.join(header) + '\n')
        if remainder != '':
            raise abc.Error('Expected header.', f'{remainder[:80]!r}')
        kinds = _kinds(header_block)
        yield header_block

        # Histories: one `i` line, then `j`/`p` line pairs up to the event announcing type 9000.
        number = len(header)
        while line:
            lines = [line.rstrip('\n')]
            complete = False
            while True:
                j = file.readline()
                p = file.readline() if j else ''
                number += 2
                if not j:
                    break
                lines.extend((j.rstrip('\n'), p.rstrip('\n')))
                if j[1:11].strip() == '9000':
                    complete = True
                    break
            if len(lines) > 1 and lines[-1] == '':
                lines.pop()
            line = file.readline()
            yield parse(lines, number, complete, last=line == '')
            number += 1
            while line.strip() == '':
                line = file.readline() if line else ''
                if not line:
                    break


def _events(file: Ptrac | pathlib.Path | str) -> collections.abc.Iterator[ptrac.Event]:
    """
    Yields the events of ptrac files, streaming them if ``file`` is a path.
    """

    if not isinstance(file, Ptrac):
        yield from Ptrac.stream(file)
        return

    layout = _layout(file.header)
    for history in file.histories:
        yield from _history_events(history, layout)


def _history_rows(history: ptrac.block.History | ptrac.block.HistoryTruncated, layout: _Layout | None = None) -> list[dict]:
    """
    Converts histories to dataframe rows: ``ptrac.Event.to_dict`` plus ``track`` and ``parent_zaid``.
    """

    return [{**event.to_dict(), 'track': track.index, 'parent_zaid': track.parent_zaid} for track in ptrac.tracks(_history_events(history, layout)) for event in track.events]


def _history_events(history: ptrac.block.History | ptrac.block.HistoryTruncated, layout: _Layout | None = None) -> collections.abc.Iterator[ptrac.Event]:
    """
    Yields the events of history blocks, each with its own type, i.e., the type announced by the line before it.
    ``layout`` is the J-line layout from the file's header; without it, values are read by the event blocks' field names.
    """

    nps = int(history.nps)
    code = abs(int(history.event_type))
    for event in history.events:
        kind = ptrac.EventType.from_code(code)
        yield ptrac.Event(nps, kind, code if kind is ptrac.EventType.BANK else None, event, _layout=layout)
        code = abs(int(event.type))
