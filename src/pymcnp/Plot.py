import os
import pathlib

import matplotlib.pyplot
import matplotlib.backends.backend_pdf

from . import _doer
from . import errors
from .Outp import Outp


matplotlib.pyplot.rcParams['figure.max_open_warning'] = 0


class Plot(_doer.Doer):
    """
    Plots OUTP files.

    Attribute:
        path: File to plot.
    """

    def __init__(self, outp: Outp):
        """
        Initializes `Plot`.

        Parameters:
            path: File to plot.

        Raises:
            CliError: RUNTIME_DOER.
        """

        if outp is None:
            raise errors.CliError(errors.CliCode.RUNTIME_DOER, outp)

        self.outp = outp

    def to_show(self, number: str):
        """
        Plots file in window.

        Parameter:
            number: Tally number.
        """

        tallies = self.outp.to_dataframe()
        if number not in tallies:
            raise errors.CliError(errors.CliCode.RUNTIME_DOER, number)

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
                color='c',
                zorder=1,
                fmt='none',
            )
            ax.set_title(f'Counts vs Bins\n{" ".join(f"{name}: {ident}" for name, ident in zip(names, idents))}', fontsize=12)
            ax.set_xlabel('Bins', fontsize=12)
            ax.set_ylabel('Counts', fontsize=12)
            ax.step(subtally['bins'], subtally['counts'], color='blue', where='mid', zorder=2, label='Tally')
            ax.legend()

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
            matplotlib.pyplot.close()
