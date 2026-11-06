import typing
import inspect
import pathlib

import pandas

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

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes from ptrac files.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        if not self.histories:
            return pandas.DataFrame()
        else:
            return pandas.concat((track.to_dataframe() for history in self.histories for track in history.tracks), ignore_index=True)

    def to_dataframe_iter(self) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame]:
        """
        Generates pandas dataframes from ptrac files iteratively.

        Yields:
            Pandas dataframes concatenated into the returned dataframe.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        if not self.histories:
            return pandas.DataFrame()

        frames = []
        for history in self.histories:
            for track in history.tracks:
                frame = track.to_dataframe()
                yield frame
                frames.append(frame)

        return pandas.concat(frames, ignore_index=True)
