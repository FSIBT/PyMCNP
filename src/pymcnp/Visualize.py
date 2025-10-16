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

    @property
    def _grid(self):
        surfaces = self.to_show_surfaces()

        return pyvista.ImageData(
            dimensions=(_show.pyvista.RESOLUTION, _show.pyvista.RESOLUTION, _show.pyvista.RESOLUTION),
            spacing=(
                (surfaces.bounds[1] - surfaces.bounds[0]) / _show.pyvista.RESOLUTION,
                (surfaces.bounds[3] - surfaces.bounds[2]) / _show.pyvista.RESOLUTION,
                (surfaces.bounds[5] - surfaces.bounds[4]) / _show.pyvista.RESOLUTION,
            ),
            origin=(-(surfaces.bounds[1] - surfaces.bounds[0]) / 2, -(surfaces.bounds[3] - surfaces.bounds[2]) / 2, -(surfaces.bounds[5] - surfaces.bounds[4]) / 2),
        )

    def to_show_cells(self, skip=tuple()) -> pyvista.Plotter:
        """
        Visualizes INP all cells.
        """

        plot = pyvista.Plotter()
        plot.add_axes()

        surfaces = {str(surface.number): surface.to_show() for surface in self.inpt.surfaces if isinstance(surface, inp.Surface)}
        cells = {}

        for cell in self.inpt.cells:
            if isinstance(cell, inp.Cell) and cell.number not in skip:
                shape = cell.to_show(surfaces, cells)
            elif isinstance(cell, inp.Like) and cell.number not in skip:
                shape = cells[str(cell.cell)]
            else:
                continue

            cells[str(cell.number)] = shape

            grid = self._grid
            grid['cell'] = shape.cell(grid.points).astype(numpy.float32)
            plot.add_volume(grid, scalars='cell', opacity=[0, 0, 0.01, 0.01])
            plot.add_mesh(shape.surface, opacity=0.9)

        return plot

    def to_show_surfaces(self, skip=tuple()) -> pyvista.Plotter:
        """
        Visualizes INP all surfaces.
        """

        plot = pyvista.Plotter()
        plot.add_axes()

        for surface in self.inpt.surfaces:
            if not isinstance(surface, inp.Surface) or surface.number in skip:
                continue

            shape = surface.to_show()

            plot.add_mesh(shape.surface)

        return plot

    def to_show_cell(self, number: tuple[str]) -> pyvista.Plotter:
        """
        Visualizes INP cell(s).

        Parameters:
            numbers: Cell number to visualize.
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

            if str(cell.number) not in number:
                continue

            grid = self._grid
            grid['cell'] = shape.cell(grid.points).astype(numpy.float32)
            plot.add_volume(grid, scalars='cell', opacity=[0, 0, 0.01, 0.01])
            plot.add_mesh(shape.surface, opacity=0.9)

        return plot

    def to_show_surface(self, number: tuple[str]) -> pyvista.Plotter:
        """
        Visualizes INP surface(s).

        Parameters:
            number: Surface number to visualize.
        """

        plot = pyvista.Plotter()
        plot.add_axes()

        for surface in self.inpt.surfaces:
            if not isinstance(surface, inp.Surface):
                continue

            if str(surface.number) not in number:
                continue

            plot.add_mesh(surface.to_show().surface)

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

    def to_pdf_cell(self, number: tuple[str], path: str | pathlib.Path):
        """
        Saves render of cells as PDF.

        Parameters:
            number: Cell numbers to visualize.
            path: Path to new pdf file.
        """

        plot = self.to_show_cell(number)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))

    def to_pdf_surface(self, number: tuple[str], path: str | pathlib.Path):
        """
        Saves render of surfaces as PDF.

        Parameters:
            number: Surface numbers to visualize.
            path: Path to new pdf file.
        """

        plot = self.to_show_surface(number)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))
