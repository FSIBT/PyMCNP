"""
Usage:
    pymcnp convert <outp> <number> --csv
    pymcnp convert <outp> <number> --parquet

Options:
    -c --csv        Write CSV.
    -p --parquet    Write PARQUET.

Takes an F1, F4, or F8 output file that can have multiple tallies in it and outputs a specific one as
a pandas dataframe as parquet or csv file.
"""

import os
import pathlib

from docopt import docopt

from . import _io
from . import _doer
from .. import errors
from ..Outp import Outp


class Convert(_doer.Doer):
    """
    Converts OUTP files.

    Attribute:
        outp: OUTP to convert.
    """

    def __init__(self, outp: Outp):
        """
        Initializes ``Convert``.

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


def main() -> None:
    """
    Executes the ``pymcnp convert`` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    number = args['<number>']
    file = pathlib.Path(args['<outp>'])

    # Reading OUTP.
    try:
        outp = Outp.from_file(file)
        convert = Convert(outp)
    except errors.OutpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)

    # Converting!
    if args['--csv']:
        convert.to_csv(number, _io.get_outfile(file, 'csv', number))
    elif args['--parquet']:
        convert.to_parquet(number, _io.get_outfile(file, 'parquet', number))

    _io.done()
