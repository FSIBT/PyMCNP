import os
import pathlib

import pyvista

from . import _doer
from . import errors
from .Inp import Inp


class Visualize(_doer.Doer):
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

        Raises:
            CliCode: RUNTIME_DOER.
        """

        if inp is None:
            raise errors.CliError(errors.CliCode.RUNTIME_DOER, inp)

        self.inp = inp

    def to_show_cells(self) -> pyvista.Plotter:
        """
        Visualizes INP cells.
        """

        plot = pyvista.Plotter()
        plot.add_axes()
        # vis = self.inp.draw()
        # plot.add_mesh(vis.data)

        return plot

    def to_show_surfaces(self) -> pyvista.Plotter:
        """
        Visualizes INP surfaces.
        """

        plot = pyvista.Plotter()
        plot.add_axes()
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
        plot.add_axes()
        vis = self.inp.draw()
        plot.add_mesh(vis.data)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))
