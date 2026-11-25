import re
import typing
import warnings
import pathlib
import collections.abc

import pandas

from . import abc
from . import ptrac

_REGEX_HISTORY = re.compile(r' *\d+ +(?:[1345]000|-?20\d\d)(?: |$)')


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
    def from_mcnp_iter(
        cls, source: str, returning: bool = False
    ) -> typing.Generator[typing.Generator[tuple[ptrac.block.Event, str], None, tuple[ptrac.block.History, str] | None], None, tuple[typing.Self, str] | None]:
        """
        Compiles source strings into their corresponding ptrac files iteratively.

        Parameters:
            source: Source string to compile.

        Yields:
            Generators yielding ptrac events and returning ptrac histories corresponding to ``source``.

        Returns:
            Ptrac file corresponding to ``source``.

        Raises:
            Error: Inner generator not done.
        """

        header, source = ptrac.block.Header.from_mcnp(source)

        stop: bool = False
        spaces: list[abc.Terminal] = []
        if returning:
            items: list[abc.Symbol] = []

        def _generator():
            nonlocal items
            nonlocal source
            nonlocal stop
            try:
                result = yield from ptrac.block.History.from_mcnp_iter(source, returning=True)
                assert result is not None
                item, source = result

                if returning:
                    items.append(item)
            except abc.Error:
                if spaces:
                    source = spaces.pop(-1).to_mcnp() + source
                stop = True

        while True:
            yield (generator := _generator())

            for _ in generator:
                pass

            if stop:
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
            histories = abc.Array[ptrac.block.History, abc.Terminal[r'\n']](*items, spaces=spaces)

        newline, source = abc.Terminal[r'\n?'].from_mcnp(source)

        if returning:
            return cls(header=header, histories=histories, newline=newline), source

    if typing.TYPE_CHECKING:

        @classmethod
        def from_file_iter(
            cls, path: pathlib.Path | str, returning: bool = False
        ) -> typing.Generator[typing.Generator[tuple[ptrac.block.Event, str], None, tuple[ptrac.block.History, str] | None], None, tuple[typing.Self, str] | None]: ...

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

        for history in self.histories:
            yield (
                frame := ptrac.to_dataframe([{**event.to_dict(), 'track': track.index, 'parent_zaid': track.parent_zaid} for track in ptrac.tracks(_history_events(history)) for event in track.events])
            )

            if returning:
                frames.append(frame)

        if returning:
            return pandas.concat(frames, ignore_index=True) if frames else ptrac.to_dataframe([])

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

        path = pathlib.Path(path)
        if not path.is_file():
            raise abc.Error('File not found.', f'{path=}')

        def parse(lines: list[str], number: int, complete: bool, last: bool) -> ptrac.block.History | ptrac.block.HistoryTruncated:
            # Only the last history of a file can be cut short (e.g., by a killed run); it is read as far as it goes.
            if complete:
                try:
                    history, remainder = ptrac.block.History.from_mcnp('\n'.join(lines))
                except abc.Error:
                    if not last:
                        raise
                else:
                    if remainder != '':
                        raise abc.Error('Expected history.', f'line {number}: {remainder[:80]!r}')
                    return history

            truncated = ptrac.block.HistoryTruncated.from_mcnp('\n'.join(lines))
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
            _, remainder = ptrac.block.Header.from_mcnp('\n'.join(header) + '\n')
            if remainder != '':
                raise abc.Error('Expected header.', f'{remainder[:80]!r}')

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

        for history in Ptrac.iter_histories(path):
            yield from _history_events(history)

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


def _events(file: Ptrac | pathlib.Path | str) -> collections.abc.Iterator[ptrac.Event]:
    """
    Yields the events of ptrac files, streaming them if ``file`` is a path.
    """

    if not isinstance(file, Ptrac):
        yield from Ptrac.stream(file)
        return

    for history in file.histories:
        yield from _history_events(history)


def _history_events(history: ptrac.block.History | ptrac.block.HistoryTruncated) -> collections.abc.Iterator[ptrac.Event]:
    """
    Yields the events of history blocks, each with its own type, i.e., the type announced by the line before it.
    """

    nps = int(history.nps)
    code = abs(int(history.event_type))
    for event in history.events:
        kind = ptrac.EventType.from_code(code)
        yield ptrac.Event(nps, kind, code if kind is ptrac.EventType.BANK else None, event)
        code = abs(int(event.type))
