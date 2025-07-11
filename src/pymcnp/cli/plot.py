"""
Usage:
    pymcnp plot <outp> <number> [ options ]

Options:
    --pdf       Write PDF.
"""

import os
import pathlib

import matplotlib.pyplot
import matplotlib.backends.backend_pdf
from docopt import docopt

from . import _io
from ..Outp import Outp
from ..utils import errors


class Plot:
    """
    Plots OUTP files.

    Attribute:
        path: File to plot.
    """

    def __init__(self, outp: Outp):
        """
        Initializes ``Plot``.

        Parameters:
            path: File to plot.

        Raises:
            CliError: SEMANTICS_PATH.
        """

        if outp is None:
            raise errors.CliError(errors.CliCode.SEMANTICS_OUTP, outp)

        self.outp = outp

    def to_show(self, number: str):
        """
        Plots file in window.

        Parameter:
            number: Tally number.
        """

        tallies = self.outp.to_dataframe()
        names = tallies[number].columns[3:-4]

        figures = []
        subtallies = tallies[number].groupby(list(names))
        for idents, subtally in subtallies:
            fig, ax = matplotlib.pyplot.subplots()

            ax.errorbar(
                subtally['bins'],
                subtally['counts'],
                yerr=subtally['errors'] * subtally['counts'],
                label='Error',
                color='orange',
                zorder=1,
            )
            ax.set_title(f'Counts vs Bins: {" ".join(f"{name}: {ident}" for name, ident in zip(names, idents))}', fontsize=12)
            ax.set_xlabel('Bins', fontsize=12)
            ax.set_ylabel('Counts', fontsize=12)
            ax.step(subtally['bins'], subtally['counts'], color='blue', where='mid', zorder=2)

            figures.append(fig)

        return figures

    def to_pdf(self, number: str, path: str | pathlib.Path):
        """
        Plots file in PDF.

        Parameters:
            number: Tally number.
            path: Path to new pdf file.
        """

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            with matplotlib.backends.backend_pdf.PdfPages(path) as pdf:
                for fig in self.to_show(number):
                    pdf.savefig(fig)


def main() -> None:
    """
    Executes the ``pymcnp plot`` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    number = args['<number>']
    file = pathlib.Path(args['<outp>'])

    # Reading OUTP.
    try:
        outp = Outp.from_file(file)
        plot = Plot(outp)
    except errors.OutpError as err:
        _io.error(err)
        exit(1)
    except errors.CliError as err:
        _io.error(err)
        exit(2)

    # Plotting!
    if args['--pdf']:
        plot.to_pdf(number, pathlib.Path(_io.get_outfile(file, 'pdf')))
    else:
        plot.to_show(number)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            matplotlib.pyplot.show()

    _io.done()
