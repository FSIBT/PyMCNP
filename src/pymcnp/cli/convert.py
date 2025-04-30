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

import pathlib

from docopt import docopt

from . import _io
from ..utils import errors


class Convert:
    """
    Converts MCNP files.

    Attribute:
        path: File to convert.
        number: Tally number.
    """

    def __init__(self, path: str | pathlib.Path):
        """
        Initializes ``Convert``.

        Parameters:
            path: File to convert.

        Raises:
            CliError: SEMANTICS_PATH.
        """

        if path is None:
            raise errors.CliError(errors.CliCode.SEMANTICS_PATH, path)

        self.path = pathlib.Path(path)

    def to_csv(self, number: int):
        """
        Converts file to CSV.

        Parameter:
            number: Tally to read.
        """

        # outp = Outp.from_file(self.path)
        # df = outp.to_dataframe()

        # path = _io.get_outfile(self.path, 'outp', 'csv')
        # with path.open('r') as file:
        # file.write(df.to_csv())

    def to_parquet(self, number: int):
        """
        Converts file to PARQUET.

        Parameters:
            number: Tally to read.
        """

        # outp = Outp.from_file(self.path)
        # df = outp.to_dataframe()

        # path = _io.get_outfile(self.path, 'outp', 'parquet')
        # with path.open('r') as file:
        # file.write(df.to_parquet())


def main() -> None:
    """
    Executes the ``pymcnp convert`` command.

    ``pymcnp convert`` converts MCNP output files to pandas dataframes.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    number = args['<number>']
    file = pathlib.Path(args['<outp>'])

    # Processing number.
    try:
        number = int(number)
    except Exception:
        _io.error(f'``{number}`` invalid number.')
        exit(1)

    # Reading OUTP file.
    try:
        convert = Convert(file)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)

    # Converting!
    if args['--csv']:
        convert.to_csv(number)
    elif args['--parquet']:
        convert.to_parquet(number)

    _io.done()
