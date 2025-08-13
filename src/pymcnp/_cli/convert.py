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
from .. import errors
from ..Outp import Outp
from ..Convert import Convert


def main() -> None:
    """
    Executes the `pymcnp convert` command.
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
    # except errors.TypesError as err:
    # _io.error(str(err))
    # exit(3)

    # Converting!
    if args['--csv']:
        convert.to_csv(number, _io.get_outfile(file, 'csv', number))
    elif args['--parquet']:
        convert.to_parquet(number, _io.get_outfile(file, 'parquet', number))

    _io.done()
