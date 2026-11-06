"""
Usage:
    pymcnp convert outp (--csv | --parquet) <file>
    pymcnp convert ptrac (--csv | --parquet) <file>
    pymcnp convert meshtal (--csv | --parquet) <file>

Options:
    -c --csv        Write CSV.
    -p --parquet    Write PARQUET.
"""

import pathlib
import sys

from docopt import docopt

from . import _io
from .. import abc
from ..Outp import Outp
from ..Ptrac import Ptrac
from ..Meshtal import Meshtal


def main() -> None:
    """
    Executes the ``pymcnp convert`` command.
    """

    # Processing CLI arguments.
    args = docopt(__doc__, options_first=True)

    if args['outp']:
        DataFile = Outp
    elif args['ptrac']:
        DataFile = Ptrac
    else:
        DataFile = Meshtal

    file = pathlib.Path(args['<file>'])

    # Reading output file.
    try:
        datafile = DataFile.from_file(file)[0]
    except abc.Error as err:
        _io.error(str(err))
        sys.exit(1)

    # Converting!
    if args['--csv']:
        datafile.to_csv_file(_io.get_outfile(file, 'csv'))
    else:
        datafile.to_parquet_file(_io.get_outfile(file, 'parquet'))

    _io.done()
