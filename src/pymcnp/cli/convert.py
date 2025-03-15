"""
Usage:
    pymcnp convert <input> <output> [ options ]

Options:
    -n --number=<number>        Which tally should be converted.

Takes an F1, F4, or F8 output file that can have multiple tallies in it and outputs a specific one as
a pandas dataframe as parquet or csv file.
"""

import pathlib

from docopt import docopt

from . import _io
from .. import outp


def main() -> None:
    """
    Executes the ``pymcnp convert`` command.

    ``pymcnp convert`` converts MCNP output files to pandas dataframes.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    number = args['--number']
    file_input = pathlib.Path(args['<input>'])
    file_output = pathlib.Path(args['<output>'])

    if number is None:
        _io.error(f'``{number}`` invalid number.')
        exit(1)

    if not file_input.is_file():
        _io.error(f'``{file_input}`` not found.')
        exit(2)

    if not file_output.is_file():
        _io.error(f'``{file_output}`` not found.')
        exit(3)

    # Reading OUTP file.
    x = outp.read_output(file_input)
    number = int(number)

    # Converting!
    try:
        df = x.read_tally(number)
    except IndexError:
        _io.error('Tally number out of range.')
        exit(4)

    match file_output.suffix:
        case '.csv':
            df.to_csv(file_output)
            _io.info(f'Saving tally {number} as csv.', file_output)
        case '.parquet':
            df.to_parquet(file_output)
            _io.info(f'Saving tally {number} as parquet.', file_output)
        case _:
            _io.info('Currently cannot handle this file type.')

    _io.done()
