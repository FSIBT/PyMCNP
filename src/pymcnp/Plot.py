import typing
import pathlib
import dataclasses

import numpy
import pandas
import matplotlib.pyplot
import matplotlib.figure
import matplotlib.backends.backend_pdf

from . import abc
from .Outp import Outp


matplotlib.pyplot.rcParams['figure.max_open_warning'] = 0


@dataclasses.dataclass
class Plot(abc.Utility):
    """
    Represents utilities that plot output files.
    """

    @staticmethod
    def _edges(bins: pandas.Series) -> numpy.ndarray:
        """
        Finds the bin edges of tally bins.

        OUTP bins are upper bin edges, so the lower edge of the first bin is
        not in the file. It is 0 if the first bin is not negative, e.g., an
        energy or time (which may itself be 0), else one bin width below the
        first bin, e.g., -1 for cosine bins -0.5, 0, 1 (MCNP's lower bound
        for cosines is -1).

        Parameters:
            bins: Upper bin edges, increasing.

        Returns:
            Bin edges, one more than ``bins``.
        """

        upper = bins.to_numpy(dtype=float)
        if upper[0] >= 0:
            lower = 0.0
        elif len(upper) > 1:
            lower = upper[0] - (upper[1] - upper[0])
        else:
            lower = upper[0] - 1
        return numpy.concatenate(([lower], upper))

    def to_show(self, outp: Outp, number: int | str) -> tuple[matplotlib.figure.Figure, ...]:
        """
        Plots tally ``number` of output file `outp``.

        Parameter:
            number: Tally number to plot.

        Raises:
            Error: Tally not found.
            Error: Tally not parsed, i.e., in the file in a layout PyMCNP
                cannot parse.
        """

        number = str(number).strip()

        try:
            tally = next(frame for frame in outp.to_dataframe_iter() if not frame.empty and str(frame['number'].iloc[0]).strip() == number)
        except StopIteration:
            if number in (unparsed := outp._unparsed_tallies()):
                raise abc.Error('Tally not parsed.', f'{number=}: tally {number} (type {unparsed[number]}) is in the file, but PyMCNP cannot parse its layout')
            raise abc.Error('Tally not found.', f'{number=}')

        figures = []
        names = tally.columns[3:-4]
        subtallies = tally.groupby(list(names))

        for idents, subtally in subtallies:
            fig, ax = matplotlib.pyplot.subplots()

            edges = self._edges(subtally['bins'])
            ax.errorbar(
                (edges[:-1] + edges[1:]) / 2,
                subtally['counts'],
                yerr=subtally['errors'] * subtally['counts'],
                label='Error',
                color='c',
                zorder=1,
                fmt='none',
            )
            ax.set_title(
                f'Counts vs Bins\n{" ".join(f"{name}: {ident}" for name, ident in zip(names, idents if isinstance(idents, typing.Iterable) else (idents,)))}',
                fontsize=12,
            )
            ax.set_xlabel('Bins', fontsize=12)
            ax.set_ylabel('Counts', fontsize=12)
            ax.stairs(subtally['counts'], edges, color='blue', zorder=2, label='Tally')
            ax.legend()

            figures.append(fig)

        return tuple(figures)

    def to_pdf(self, outp: Outp, number: int | str, path: pathlib.Path | str) -> None:
        """
        Plots tally ``number`` of output files in PDF file.

        Parameters:
            number: Tally number to plot.
            path: Path to new pdf file.
        """

        with matplotlib.backends.backend_pdf.PdfPages(path) as pdf:
            for fig in self.to_show(outp, number):
                pdf.savefig(fig)
        matplotlib.pyplot.close()
