"""
Usage:
    pymcnp convert outp (--csv | --parquet) <file>
    pymcnp convert ptrac (--csv | --parquet) <file>
    pymcnp convert meshtal (--csv | --parquet) <file>

Options:
    -c --csv        Write CSV.
    -p --parquet    Write PARQUET.

Writes the data of OUTP (all tallies), PTRAC (one row per event), or
MESHTAL files next to them, e.g., ``file.outp` to `file.csv``.
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
    args = docopt(__doc__)

    if args['outp']:
        Nonterminal = Outp
    elif args['ptrac']:
        Nonterminal = Ptrac
    else:
        Nonterminal = Meshtal

    file = pathlib.Path(args['<file>'])

    # Reading output file.
    try:
        nonterminal, _ = Nonterminal.from_file(file)
    except abc.Error as err:
        _io.error(str(err))
        sys.exit(1)

    # Converting!
    if args['--csv']:
        nonterminal.to_file_csv(_io.get_outfile(file, 'csv'))
    else:
        nonterminal.to_file_parquet(_io.get_outfile(file, 'parquet'))

    _io.done()
