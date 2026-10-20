import re
import typing
import pathlib
import collections.abc

from . import abc
from . import ptrac

_REGEX_HISTORY = re.compile(r' *\d+ +(?:[1345]000|-?20\d\d)(?: |$)')


def _events(file: 'Ptrac | pathlib.Path | str') -> collections.abc.Iterator[ptrac.Event]:
    if not isinstance(file, Ptrac):
        yield from Ptrac.stream(file)
        return

    for history in file.histories:
        yield from _history_events(history)


def _history_events(history: ptrac.block.History) -> collections.abc.Iterator[ptrac.Event]:
    nps = int(history.i.nps)
    code = abs(int(history.i.event_type))
    for event in history.events:
        kind = ptrac.EventType.from_code(code)
        yield ptrac.Event(nps, kind, code if kind is ptrac.EventType.BANK else None, event.j, event.p)
        code = abs(int(event.j.type))


class Ptrac(abc.File):
    """
    Represents ptrac files.

    Attributes:
        header: ptrac `header` parameter.
        histories: ptrac `histories` parameter.
    """

    header: ptrac.block.Header
    histories: typing.Annotated[abc.Array, ptrac.block.History, typing.Annotated[abc.Terminal, r'\n']]
    newline: typing.Annotated[abc.Terminal, r'\n?']

    @staticmethod
    def iter_histories(path: pathlib.Path | str) -> collections.abc.Iterator[ptrac.block.History]:
        """
        Parses ptrac files one history at a time, without holding the file or the histories in memory.

        Parameters:
            path: Path to ptrac file to read.

        Yields:
            History blocks in file order, each parsed once.

        Raises:
            Error: File not found.
            Error: Expected history.
        """

        path = pathlib.Path(path)
        if not path.is_file():
            raise abc.Error('File not found.', f'{path=}')

        def parse(lines: list[str], number: int) -> ptrac.block.History:
            history, remainder = ptrac.block.History.from_mcnp('\n'.join(lines))
            if remainder != '':
                raise abc.Error('Expected history.', f'line {number}: {remainder[:80]!r}')
            return history

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
                while True:
                    j = file.readline()
                    p = file.readline() if j else ''
                    number += 2
                    if not j:
                        break
                    lines.extend((j.rstrip('\n'), p.rstrip('\n')))
                    if j[1:11].strip() == '9000':
                        break
                if len(lines) > 1 and lines[-1] == '':
                    lines.pop()
                yield parse(lines, number)
                line = file.readline()
                number += 1
                while line.strip() == '':
                    line = file.readline() if line else ''
                    if not line:
                        break

    @staticmethod
    def stream(path: pathlib.Path | str) -> collections.abc.Iterator[ptrac.Event]:
        """
        Parses ptrac files one event at a time in a single pass, with flat memory use.

        An event's `j` line announces the type of the next event, so each event is given its own type here.

        Parameters:
            path: Path to ptrac file to read.

        Yields:
            Events in file order, each with its history number (`nps`) and type.

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
            Tracks in file order; see `ptrac.Track`.
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
        Writes events of a ptrac file to a parquet file in one pass, `chunk` rows at a time, so files of any size fit in memory.

        Columns are those of `Event.to_dict` plus `track` (track number within the history) and `parent_zaid` (see `ptrac.Track`).
        If `cell_entered` or `surface` is given, only surface crossings that match are written.

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
