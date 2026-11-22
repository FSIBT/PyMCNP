import typing
import pathlib

import pandas

from . import abc
from . import ptrac


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
        Generates pandas dataframes for histories.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for histories.

        Returns:
            Pandas dataframe for all histories.
        """

        if self.histories:
            if returning:
                frames = []

            for history in self.histories:
                yield (frame := history.to_dataframe())

                if returning:
                    frames.append(frame)

            if returning:
                return pandas.concat(frames, ignore_index=True)
        else:
            if returning:
                return pandas.DataFrame()
