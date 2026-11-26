import typing
import pathlib
import dataclasses

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

    def to_show(self, outp: Outp, number: int | str) -> tuple[matplotlib.figure.Figure, ...]:
        """
        Plots tally ``number` of output file `outp``.

        Parameter:
            number: Tally number to plot.

        Raises:
            Error: File not found.
            Error: Tally not found.
        """

        number = str(number).strip()

        try:
            tally = next(frame for frame in outp.to_dataframe_iter() if not frame.empty and str(frame['number'].iloc[0]).strip() == number)
        except StopIteration:
            raise abc.Error('Tally not found', f'{number=}')

        figures = []
        names = tally.columns[3:-4]
        subtallies = tally.groupby(list(names))

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
            ax.set_title(
                f'Counts vs Bins\n{" ".join(f"{name}: {ident}" for name, ident in zip(names, idents if isinstance(idents, typing.Iterable) else (idents,)))}',
                fontsize=12,
            )
            ax.set_xlabel('Bins', fontsize=12)
            ax.set_ylabel('Counts', fontsize=12)
            ax.step(subtally['bins'], subtally['counts'], color='blue', where='pre', zorder=2, label='Tally')
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
