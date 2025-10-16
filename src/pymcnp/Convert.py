import os
import pathlib

from . import _doer
from . import errors
from .Outp import Outp


class Convert(_doer.Doer):
    """
    Converts OUTP files.

    Attribute:
        outp: OUTP to convert.
    """

    def __init__(self, outp: Outp):
        """
        Initializes `Convert`.

        Parameters:
            outp: OUTP to convert.

        Raises:
            CliError: RUNTIME_DOER.
        """

        if outp is None:
            raise errors.CliError(errors.CliCode.RUNTIME_DOER, outp)

        self.outp = outp

    def to_csv(self, number: str, path: str | pathlib.Path):
        """
        Converts file to CSV.

        Parameter:
            number: Tally to read.
            path: Path to new csv file.
        """

        tallies = self.outp.to_dataframe()

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            with open(path, 'w') as file:
                file.write(tallies[number].to_csv())

    def to_parquet(self, number: str, path: str | pathlib.Path):
        """
        Converts file to PARQUET.

        Parameters:
            number: Tally to read.
            path: Path to new parquet file.
        """

        tallies = self.outp.to_dataframe()

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            with open(path, 'wb') as file:
                file.write(tallies[number].to_parquet())
