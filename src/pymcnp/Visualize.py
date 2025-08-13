import os
import pathlib

import numpy
import pyvista

from . import inp
from . import _show
from . import _doer
from . import errors
from .Inp import Inp


class Visualize(_doer.Doer):
    """
    Visualizes INP files.

    Attributes:
        inpt: Files to visualize.
    """

    GRID = pyvista.ImageData(
        dimensions=(_show.pyvista.RESOLUTION, _show.pyvista.RESOLUTION, _show.pyvista.RESOLUTION),
        spacing=(_show.pyvista.BOUND / _show.pyvista.RESOLUTION, _show.pyvista.BOUND / _show.pyvista.RESOLUTION, _show.pyvista.BOUND / _show.pyvista.RESOLUTION),
        origin=(-_show.pyvista.BOUND / 2, -_show.pyvista.BOUND / 2, -_show.pyvista.BOUND / 2),
    )

    def __init__(self, inpt: Inp):
        """
        Initializes `Visualize`.

        Parameters:
            inpt: Files to visualize.

        Raises:
            CliCode: RUNTIME_DOER.
        """

        if inpt is None:
            raise errors.CliError(errors.CliCode.RUNTIME_DOER, inpt)

        self.inpt = inpt

    def to_show_cells(self) -> pyvista.Plotter:
        """
        Visualizes INP cells.
        """

        plot = pyvista.Plotter()
        plot.add_axes()

        surfaces = {str(surface.number): surface.to_show() for surface in self.inpt.surfaces if isinstance(surface, inp.Surface)}
        cells = {}

        for cell in self.inpt.cells:
            if isinstance(cell, inp.Cell):
                shape = cell.to_show(surfaces, cells)
            elif isinstance(cell, inp.Like):
                shape = cells[str(cell.cell)]
            else:
                continue

            cells[str(cell.number)] = shape

            self.GRID['cell'] = shape.cell(self.GRID.points).astype(numpy.float32)
            plot.add_volume(self.GRID, scalars='cell', opacity=[0, 0, 0.01, 0.01])
            plot.add_mesh(shape.surface, opacity=0.9)

        return plot

    def to_show_surfaces(self) -> pyvista.Plotter:
        """
        Visualizes INP surfaces.
        """

        plot = pyvista.Plotter()
        plot.add_axes()

        for surface in self.inpt.surfaces:
            if not isinstance(surface, inp.Surface):
                continue

            shape = surface.to_show()

            plot.add_mesh(shape.surface)

        return plot

    def to_show_cell(self, number: str) -> pyvista.Plotter:
        """
        Visualizes INP cells.

        Parameters:
            number: Cell number to visualize.
        """

        plot = pyvista.Plotter()
        plot.add_axes()

        surfaces = {str(surface.number): surface.to_show() for surface in self.inpt.surfaces if isinstance(surface, inp.Surface)}
        cells = {}

        for cell in self.inpt.cells:
            if isinstance(cell, inp.Cell):
                shape = cell.to_show(surfaces, cells)
            elif isinstance(cell, inp.Like):
                shape = cells[str(cell.cell)]
            else:
                continue

            cells[str(cell.number)] = shape

            if str(cell.number) != number:
                continue

            self.GRID['cell'] = shape.cell(self.GRID.points).astype(numpy.float32)
            plot.add_volume(self.GRID, scalars='cell', opacity=[0, 0, 0.01, 0.01])
            plot.add_mesh(shape.surface, opacity=0.9)

            break
        else:
            raise errors.CliError(errors.CliCode.RUNTIME_DOER, number)

        return plot

    def to_show_surface(self, number: str) -> pyvista.Plotter:
        """
        Visualizes INP surfaces.

        Parameters:
            number: Surface number to visualize.
        """

        plot = pyvista.Plotter()
        plot.add_axes()

        for surface in self.inpt.surfaces:
            if not isinstance(surface, inp.Surface) or str(surface.number) != number:
                continue

            plot.add_mesh(surface.to_show().surface)
            break
        else:
            raise errors.CliError(errors.CliCode.RUNTIME_DOER, number)

        return plot

    def to_pdf_cells(self, path: str | pathlib.Path):
        """
        Saves render of cells as PDF.

        Parameters:
            path: Path to new pdf file.
        """

        plot = self.to_show_cells()

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))

    def to_pdf_surfaces(self, path: str | pathlib.Path):
        """
        Saves render of surfaces as PDF.

        Parameters:
            path: Path to new pdf file.
        """

        plot = self.to_show_surfaces()

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))
