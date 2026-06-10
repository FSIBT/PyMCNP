import os
import pathlib
import dataclasses

from . import abc
from .Outp import Outp


@dataclasses.dataclass
class Convert(abc.Utility):
    """
    Represents utilites that convert output files.

    Attribute:
        file: Output file to convert.
    """

    file: Outp

    def to_csv(self, number: str, path: pathlib.Path | str):
        """
        Converts tally `number` in output file `outp` to a CSV file.

        Parameters:
            number: Tally in output file `outp` to convert.
            path: .
        """

        tallies = self.file.to_dataframe()
        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            with open(path, 'w') as file:
                file.write(tallies[number].to_csv())

    def to_parquet(self, number: str, path: pathlib.Path | str):
        """
        Converts tally `number` in output file `outp` to a PARQUET file.

        Parameters:
            number: Tally in output file `outp` to convert.
            path: .
        """

        tallies = self.file.to_dataframe()
        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            with open(path, 'wb') as file:
                file.write(tallies[number].to_parquet())
