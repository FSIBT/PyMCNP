"""
Usage:
    pymcnp convert <input>
    pymcnp convert [-n <number>] <input> <output>

Option_s:
    -n number --number=<number>   Which tally should be converted.
    -o file --output=file         Write to file instead of overwriting the input file.

Takes an F1, F4, or F8 output file that can have multiple tallies in it and outputs a specific one as
a pandas dataframe as parquet or csv file.
The output data file is taken from the file ending.

If no output file is given, the number of available tallies will be printed.

"""

from pathlib import Path
import sys

from docopt import docopt
from rich import print

import pymcnp
from . import _io


def main() -> None:
    """
    Executes the ``pymcnp convert`` command.

    ``pymcnp convert`` converts MCNP output files to pandas dataframes.
    """

    _io.warning()

    args = docopt(__doc__)

    N = args['--number']
    file_in = Path(args['<input>'])

    if not file_in.is_file():
        print(f'[red]Error[/] Cannot access file {file_in}')
        sys.exit(1)

    x = pymcnp.read_output(file_in)
    if N is not None and args['<output>']:
        N = int(N)
        file_out = Path(args['<output>'])

        try:
            df = x.read_tally(N)
        except IndexError:
            print('[red]Error[/] Tally number out of range')
            sys.exit(2)

        match file_out.suffix:
            case '.csv':
                df.to_csv(file_out)
                print(f'Saving tally {N} as csv to ', file_out)
            case '.parquet':
                df.to_parquet(file_out)
                print(f'Saving tally {N} as parquet to ', file_out)
            case _:
                print('Currently cannot handle this file type')

    _io.done()
