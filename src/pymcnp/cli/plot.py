"""
Usage:
    pymcnp plot [-n number] [--pdf] <input>

Options:
    -n number --number=<number>   Which tally should be converted.
    --pdf                         Save as pdf
"""

from pathlib import Path
import sys

from docopt import docopt
from matplotlib import pyplot as plt
from rich import print
from rich.panel import Panel

import pymcnp


def main() -> None:
    """Check the syntax of an input file.

    If `--fix` is given, reformat the output.
    """

    args = docopt(__doc__)

    N = args['--number']
    file_in = Path(args['<input>'])

    print(
        Panel(
            '[orange3]Warning[/] PyMCNP is just getting started.'
            'Please double check the output to make sure everyhing is working as expected'
            'If you find an error, please report it at https://github.com/FSIBT/PyMCNP/issues'
        )
    )

    if not file_in.is_file():
        print(f'[red]Error[/] Cannot access file {file_in}')
        sys.exit(1)

    x = pymcnp.read_output(file_in)
    N = int(N) if N is not None else 0

    try:
        df = x.read_tally(N)
    except IndexError:
        print('[red]Error[/] Tally number out of range')
        sys.exit(2)

    plt.figure()

    plt.errorbar(
        df['energy'],
        df['cts'],
        yerr=df['error'] * df['cts'],
        fmt='o',
        label='Error',
        color='orange',
        zorder=1,
    )
    plt.step(df['energy'], df['cts'], color='blue', where='mid', label='Counts', zorder=2)

    plt.title('Energy histogram')
    plt.xlabel('Energy [MeV]')
    plt.ylabel('Counts/bin/neutron')

    plt.yscale('log')
    plt.legend()

    if args['--pdf']:
        output_filename = Path(f'{file_in.stem}_tally_{N}.pdf')
        if output_filename.is_file():
            print('[orange3]Warning[/] Overwriting output file')
        plt.savefig(output_filename)
    else:
        plt.show()
