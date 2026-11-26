"""
Usage:
    pymcnp convert outp (--csv | --parquet) <file>
    pymcnp convert ptrac (--csv | --parquet) <file>
    pymcnp convert meshtal (--csv | --parquet) <file>

Options:
    -c --csv        Write CSV.
    -p --parquet    Write PARQUET.

Writes the data of OUTP (all tallies), PTRAC (one row per event), or
MESHTAL (all mesh tallies, with a ``number`` column) files next to them,
e.g., ``file.outp`` to ``file.csv``.
"""

import pathlib
import sys

import pandas
from docopt import docopt

from . import _io
from .. import abc
from ..abc.file.WithDataIter import _write_parquet
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

    # Reading output file; meshtal files may hold several mesh tallies.
    try:
        if Nonterminal is Meshtal:
            frame = pandas.concat([tally.to_dataframe().assign(number=tally.tally_number) for tally in Meshtal.iter_tallies(file)], ignore_index=True)
            frame.insert(0, 'number', frame.pop('number'))
        else:
            nonterminal, _ = Nonterminal.from_file(file)
            frame = nonterminal.to_dataframe()
    except abc.Error as err:
        _io.error(str(err))
        sys.exit(1)

    # Converting!
    if args['--csv']:
        frame.to_csv(_io.get_outfile(file, 'csv'), index=False)
    else:
        _write_parquet(frame, _io.get_outfile(file, 'parquet'))

    _io.done()
