import os
import abc
import typing
import pathlib

import pandas
import pyarrow
import pyarrow.parquet

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
    Represents nonterminal start symbols with `DataFile.to_dataframe`.
    """

    @abc.abstractmethod
    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes from nonterminal start symbols.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def to_dataframe_iter(self) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame]:
        """
        Generates pandas dataframes from nonterminal start symbols iteratively.

        Yields:
            Pandas dataframes concatenated into the returned dataframe.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        raise NotImplementedError

    def to_file_csv(self, path: pathlib.Path | str) -> None:
        """
        Generates csv files from meshtal files.

        Parameters:
            path: Path of csv file to generate.
        """

        path = pathlib.Path(path)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            for i, chunck in enumerate(self.to_dataframe_iter()):
                if path.exists():
                    path.unlink()

                chunck.to_csv(
                    path,
                    mode='a',
                    index=False,
                    header=(i == 0),
                )

    def to_file_parquet(self, path: pathlib.Path | str) -> None:
        """
        Generates parquet files from meshtal files.

        Parameters:
            path: Path of parquet file to generate.
        """

        path = pathlib.Path(path)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            if path.exists():
                path.unlink()

            dataframe_iter = self.to_dataframe_iter()

            try:
                chunk = next(dataframe_iter)
                table = pyarrow.Table.from_pandas(chunk, preserve_index=False)

                with pyarrow.parquet.ParquetWriter(path, table.schema) as writer:
                    writer.write_table(table)

                    for chunk in dataframe_iter:
                        table = pyarrow.Table.from_pandas(chunk, preserve_index=False)
                        writer.write_table(table)
            except StopIteration:
                pass
