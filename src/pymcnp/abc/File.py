import os
import abc
import typing
import pathlib

import pandas

from .Nonterminal import Nonterminal
from .Error import Error


class File(Nonterminal):
    """
    Represents nonterminal start symbols.
    """

    @classmethod
    def from_file(cls, path: pathlib.Path | str) -> tuple[typing.Self, str]:
        """
        Compiles files into their corresponding nonterminal symbols.

        Parameters:
            path: Path to file to compile.

        Returns:
            Nonterminal symbol corresponding to file at ``path``.

        Raises:
            Error: File not found.
        """

        path = pathlib.Path(path)

        if not path.is_file():
            raise Error('File not found.', f'{path=}')

        source = path.read_text()

        return cls.from_mcnp(source)

    def to_file(self, path: pathlib.Path | str) -> None:
        """
        Decompiles nonterminal symbols into their corresponding file at ``path``.
        """

        path = pathlib.Path(path)
        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            path.write_text(self.to_mcnp())


class DataFile(File):
    """
    Represents nonterminal start symbols that convert to pandas dataframes, e.g., OUTP, MESHTAL, and PTRAC files.

    Subclasses implement ``to_dataframe_iter``; ``to_dataframe``, ``to_file_csv``, and ``to_file_parquet`` build on it.
    """

    @abc.abstractmethod
    def to_dataframe_iter(self) -> typing.Iterator[pandas.DataFrame]:
        """
        Generates pandas dataframes from nonterminal start symbols one part at a time, e.g., one tally or one history.

        Yields:
            Pandas dataframes, which concatenated give ``to_dataframe``.
        """

        raise NotImplementedError

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes from nonterminal start symbols.

        Returns:
            Pandas dataframe corresponding to ``self``, empty if there is no data.
        """

        frames = list(self.to_dataframe_iter())

        if not frames:
            return pandas.DataFrame()

        return pandas.concat(frames, ignore_index=True)

    def to_file_csv(self, path: pathlib.Path | str) -> None:
        """
        Writes ``to_dataframe`` to a csv file.

        Parameters:
            path: Path of csv file to write.
        """

        self.to_dataframe().to_csv(pathlib.Path(path), index=False)

    def to_file_parquet(self, path: pathlib.Path | str) -> None:
        """
        Writes ``to_dataframe`` to a parquet file.

        Columns that mix strings and numbers, e.g., energy bins with a ``Total`` bin, are written as strings.

        Parameters:
            path: Path of parquet file to write.
        """

        frame = self.to_dataframe()

        for column in [column for column in frame.columns if pandas.api.types.is_object_dtype(frame[column])]:
            frame[column] = frame[column].map(lambda value: value if value is None or isinstance(value, str) or pandas.isna(value) else str(value))

        frame.to_parquet(pathlib.Path(path), index=False)
