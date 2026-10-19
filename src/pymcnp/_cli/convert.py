"""
Usage:
    pymcnp convert (--csv | --parquet) <outp> <number>

Options:
    -c --csv        Write CSV.
    -p --parquet    Write PARQUET.

Takes an F1, F4, or F8 output file that can have multiple tallies in it and outputs a specific one as
a pandas dataframe as parquet or csv file.
"""

import pathlib
import sys

from docopt import docopt

from . import _io
from .. import abc
from ..Outp import Outp
from ..Convert import Convert


def main() -> None:
    """
    Executes the `pymcnp convert` command.
    """

    # Processing CLI arguments.
    args = docopt(__doc__)
    number = args['<number>']
    file = pathlib.Path(args['<outp>'])

    # Reading output file.
    try:
        outp = Outp.from_file(file)[0]
        convert = Convert(outp)
    except abc.Error as err:
        _io.error(str(err))
        sys.exit(1)

    # Converting!
    if args['--csv']:
        convert.to_csv(number, _io.get_outfile(file, 'csv', number))
    elif args['--parquet']:
        convert.to_parquet(number, _io.get_outfile(file, 'parquet', number))

    _io.done()
