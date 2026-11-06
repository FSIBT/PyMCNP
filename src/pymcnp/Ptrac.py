import typing
import inspect
import pathlib

from . import abc
from . import ptrac


class Ptrac(abc.File):
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
    def from_mcnp_iter(cls, source: str) -> typing.Generator[typing.Generator[tuple[ptrac.block.Event, str], None, tuple[ptrac.block.History, str]], None, tuple[typing.Self, str]]:
        """
        Compiles source strings into their corresponding ptrac files iteratively.

        Parameters:
            source: Source string to compile.

        Yields:
            Generators yielding ptrac events and returning ptrac histories corresponding to `source`.

        Returns:
            Ptrac file corresponding to `source`.

        Raises:
            Error: Inner generator not done.
        """

        header, source = ptrac.block.Header.from_mcnp(source)

        spaces: list[abc.Terminal] = []
        items: list[abc.Symbol] = []
        while True:
            try:
                generator = ptrac.block.History.from_mcnp_iter(source)
                yield generator
            except abc.Error:
                if spaces:
                    source = spaces.pop(-1).to_mcnp() + source
                break

            if inspect.getgeneratorstate(generator) == inspect.GEN_SUSPENDED:
                raise abc.Error('Inner generator not done.', f'{generator=}')
            try:
                assert next(generator) is None
            except StopIteration as err:
                item, source = err.value
                items.append(item)

            try:
                space, source = abc.Terminal[r'\n'].from_mcnp(source)
                spaces.append(space)
            except abc.Error:
                break

        histories = abc.Array[ptrac.block.History, abc.Terminal[r'\n']](*items, spaces=spaces)
        newline, source = abc.Terminal[r'\n?'].from_mcnp(source)

        return cls(header=header, histories=histories, newline=newline), source

    @classmethod
    def from_file_iter(cls, path: pathlib.Path | str) -> typing.Generator[typing.Generator[tuple[ptrac.block.Event, str], None, tuple[ptrac.block.History, str]], None, tuple[typing.Self, str]]:
        """
        Compiles files into their corresponding ptrac files iteratively.

        Parameters:
            path: Path to file to compile.

        Yields:
            Generators yielding ptrac events and returning ptrac histories corresponding to `source`.

        Returns:
            Ptrac file corresponding to `source`.

        Raises:
            Error: File not found.
            Error: Inner generator not done.
        """

        path = pathlib.Path(path)

        if not path.is_file():
            raise abc.Error('File not found.', f'{path=}')

        source = path.read_text()

        return cls.from_mcnp_iter(source)


#    @staticmethod
#    def to_parquet(
#        path: pathlib.Path | str,
#        out: pathlib.Path | str,
#        *,
#        particle: ptrac.Particle | None = None,
#        types: collections.abc.Collection[ptrac.EventType] | None = None,
#        cell_entered: int | None = None,
#        surface: int | None = None,
#        chunk: int = 100_000,
#    ) -> int:
#        """
#        Writes events of a ptrac file to a parquet file in one pass, `chunk` rows at a time, so files of any size fit in memory.
#
#        Columns are those of `Event.to_dict` plus `track` (track number within the history) and `parent_zaid` (see `ptrac.Track`).
#        If `cell_entered` or `surface` is given, only surface crossings that match are written.
#
#        Parameters:
#            path: Path to ptrac file to read.
#            out: Path to parquet file to write.
#            particle: Only write events of tracks of this particle.
#            types: Only write events of these types.
#            cell_entered: Only write surface crossings entering this cell.
#            surface: Only write surface crossings of this surface number (any facet).
#            chunk: Number of rows held in memory before they are written.
#
#        Returns:
#            Number of rows written.
#
#        Raises:
#            Error: Invalid value.
#        """
#
#        if chunk < 1:
#            raise abc.Error('Invalid value.', f'{chunk=}')
#
#        surfaces_only = cell_entered is not None or surface is not None
#        writer = ptrac.ParquetWriter(out)
#        rows: list[dict] = []
#        total = 0
#        try:
#            for track in Ptrac.tracks(path, particle, cell_entered):
#                events = track.entries(cell=cell_entered, surface=surface) if surfaces_only else track.events
#                for event in events:
#                    if types is not None and event.type not in types:
#                        continue
#                    rows.append({**event.to_dict(), 'track': track.index, 'parent_zaid': track.parent_zaid})
#                    if len(rows) >= chunk:
#                        writer.write(rows)
#                        total += len(rows)
#                        rows = []
#            if rows:
#                writer.write(rows)
#                total += len(rows)
#            writer.close()
#        except BaseException:
#            writer.abort()
#            raise
#        return total
