"""
Usage:
    pymcnp plot <outp> <number> [ options ]

Options:
    -p --pdf        Write to PDF.
"""

import pathlib

from docopt import docopt

from . import _io
from ..utils import errors


class Plot:
    """
    Plots MCNP files.

    Attribute:
        path: File to plot.
    """

    def __init__(self, path: str | pathlib.Path):
        """
        Initializes ``Plot``.

        Parameters:
            path: File to plot.

        Raises:
            CliError: SEMANTICS_PATH.
        """

        if path is None:
            raise errors.CliError(errors.CliCode.SEMANTICS_PATH, path)

        self.path = pathlib.Path(path)

    def to_show(self, number: int):
        """
        Plots file in window.

        Parameter:
            number: Tally number.
        """

        # outp = Outp.from_file(self.path)
        # df = outp.to_dataframe()
        # fig, ax = plt.subplots()
        # ax.errorbar(
        #    df['energy'],
        #    df['cts'],
        #    yerr=df['error'] * df['cts'],
        #    fmt='o',
        #    label='Error',
        #    color='orange',
        #    zorder=1,
        # )
        # ax.step(df['energy'], df['cts'], color='blue', where='mid', label='Counts', zorder=2)
        # ax.title('Energy histogram')
        # ax.xlabel('Energy [MeV]')
        # ax.ylabel('Counts/bin/neutron')
        # ax.yscale('log')
        # ax.legend()

        # return fig, ax

    def to_pdf(self, number: int):
        """
        Plots file in PDF.

        Parameters:
            number: Tally number.
        """

        fig, ax = self.to_show(number)
        path = _io.get_outfile(self.path, 'outp', 'pdf')
        fig.savefig(path)


def main() -> None:
    """
    Executes the ``pymcnp plot`` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    number = args['<number>'] or 0
    path = pathlib.Path(args['<outp>'])

    # Processing number.
    try:
        number = int(number)
    except Exception:
        _io.error(f'``{number}`` invalid number.')
        exit(1)

    # Plotting!
    try:
        plot = Plot(path)
    except errors.OutpError as err:
        _io.error(str(err))
        exit(2)
    except errors.CliError as err:
        _io.error(str(err))
        exit(3)

    if args['--pdf']:
        plot.to_pdf(number)
    else:
        fig, ax = plot.plot(number)
        fig.show()

    _io.done()
