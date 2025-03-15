"""
Usage:
    pymcnp plot [-n number] [--pdf] <input>

Options:
    -n --number=<number>        Which tally should be converted.
    --pdf                       Save as pdf.
"""

import pathlib

from docopt import docopt
from matplotlib import pyplot as plt

from . import _io
from .. import outp


def main() -> None:
    """
    Executes the ``pymcnp plot`` command.
    """

    _io.disclaimer()

    args = docopt(__doc__)

    N = args['--number']
    file_in = pathlib.Path(args['<input>'])

    if not file_in.is_file():
        print(f'[red]Error[/] Cannot access file {file_in}')
        exit(1)

    x = outp.read_output(file_in)
    N = int(N) if N is not None else 0

    try:
        df = x.read_tally(N)
    except IndexError:
        print('[red]Error[/] Tally number out of range')
        exit(2)

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
        output_filename = pathlib.Path(f'{file_in.stem}_tally_{N}.pdf')
        if output_filename.is_file():
            print('[orange3]Warning[/] Overwriting output file')
        plt.savefig(output_filename)
    else:
        plt.show()

    _io.done()
