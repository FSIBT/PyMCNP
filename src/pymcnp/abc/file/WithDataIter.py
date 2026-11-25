import pathlib

import pandas

from .. import symbol


class WithDataIter(symbol.WithDataIter):
    """
    Represents nonterminal start symbols with iterative dataframe writers.
    """

    def to_file_csv(self, path: pathlib.Path | str) -> None:
        """
        Writes dataframes for repeated subsymbols to csv files.

        Parameters:
            path: Path of csv file to write.
        """

        self.to_dataframe().to_csv(pathlib.Path(path), index=False)

    def to_file_parquet(self, path: pathlib.Path | str) -> None:
        """
        Writes dataframes for repeated subsymbols to parquet files.

        Parameters:
            path: Path of parquet file to write.
        """

        frame = self.to_dataframe()
        for column in [column for column in frame.columns if pandas.api.types.is_object_dtype(frame[column])]:
            frame[column] = frame[column].map(lambda value: value if value is None or isinstance(value, str) or pandas.isna(value) else str(value))
        frame.to_parquet(pathlib.Path(path), index=False)
