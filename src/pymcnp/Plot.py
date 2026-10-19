import os
import typing
import pathlib
import dataclasses

import matplotlib.pyplot
import matplotlib.backends.backend_pdf

from . import abc
from .Outp import Outp


matplotlib.pyplot.rcParams['figure.max_open_warning'] = 0


@dataclasses.dataclass
class Plot(abc.Utility):
    """
    Represents utilties that plot output files.

    Attribute:
        file: Output file to plot.
    """

    file: Outp

    def to_show(self, number: str):
        """
        Plots tally `number` of output files in window.

        Parameter:
            number: Tally number to plot.

        Raises:
            Error: Tally not found.
        """

        tallies = self.file.to_dataframe()
        if number not in tallies:
            raise abc.Error('Tally not found.', f'{number=}')

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
            ax.set_title(f'Counts vs Bins\n{" ".join(f"{name}: {ident}" for name, ident in zip(names, idents if isinstance(idents, typing.Iterable) else (idents,)))}', fontsize=12)
            ax.set_xlabel('Bins', fontsize=12)
            ax.set_ylabel('Counts', fontsize=12)
            ax.step(subtally['bins'], subtally['counts'], color='blue', where='mid', zorder=2, label='Tally')
            ax.legend()

            figures.append(fig)

        return figures

    def to_pdf(self, number: str, path: pathlib.Path | str):
        """
        Plots tally `number` of output files in PDF file.

        Parameters:
            number: Tally number to plot.
            path: Path to new pdf file.
        """

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            with matplotlib.backends.backend_pdf.PdfPages(path) as pdf:
                for fig in self.to_show(number):
                    pdf.savefig(fig)
            matplotlib.pyplot.close()
