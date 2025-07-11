"""
Usage:
    pymcnp visualize <inp> [ options ]

Options:
    -c --cells          Visualize cells.
    -s --surfaces       Visualize surfaces.
    --pdf               Write PDF.
"""

import os
import pathlib

import pyvista
from docopt import docopt

from . import _io
from ..Inp import Inp
from ..utils import errors


PLOT = pyvista.Plotter()


class Visualize:
    """
    Visualizes INP files.

    Attributes:
        inp: Files to visualize.
    """

    def __init__(self, inp: Inp):
        """
        Initializes ``Visualize``.

        Parameters:
            inp: Files to visualize.
        """

        if inp is None:
            raise errors.CliError(errors.CliCode.SEMANTICS_INP, inp)

        self.inp = inp

    def to_show_cells(self) -> pyvista.Plotter:
        """
        Visualizes INP cells.
        """

        plot = pyvista.Plotter()
        # vis = self.inp.draw()
        # plot.add_mesh(vis.data)

        return plot

    def to_show_surfaces(self) -> pyvista.Plotter:
        """
        Visualizes INP surfaces.
        """

        plot = pyvista.Plotter()
        vis = self.inp.draw()
        plot.add_mesh(vis.data)

        return plot

    def to_pdf_cells(self, path: str | pathlib.Path):
        """
        Saves render of cells as PDF.

        Parameters:
            path: Path to new pdf file.
        """

        # plot = pyvista.Plotter()
        # vis = self.inp.draw()
        # plot.add_mesh(vis.data)

        # plot.save_graphic(str(path))

    def to_pdf_surfaces(self, path: str | pathlib.Path):
        """
        Saves render of surfaces as PDF.

        Parameters:
            path: Path to new pdf file.
        """

        plot = pyvista.Plotter()
        vis = self.inp.draw()
        plot.add_mesh(vis.data)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))


def main() -> None:
    """
    Executes the ``pymcnp visualize`` command.
    """

    _io.disclaimer()

    # Processing CLI arguments.
    args = docopt(__doc__)
    file = pathlib.Path(args['<inp>'])

    # Reading INP.
    try:
        inp = Inp.from_file(file)
        visualize = Visualize(inp)
    except errors.InpError as err:
        _io.error(str(err))
        exit(1)
    except errors.CliError as err:
        _io.error(str(err))
        exit(2)

    # Visualizing!
    if args['--cells']:
        if args['--pdf']:
            visualize.to_pdf_cells(_io.get_outfile(file, 'pdf', 'cells'))
        else:
            plot = visualize.to_show_cells()

            if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                plot.plot()

    else:
        if args['--pdf']:
            visualize.to_pdf_surfaces(_io.get_outfile(file, 'pdf', 'surfaces'))
        else:
            plot = visualize.to_show_surfaces()

            if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
                plot.plot()

    _io.done()
