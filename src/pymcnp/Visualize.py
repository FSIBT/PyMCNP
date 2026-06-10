import os
import pathlib
import dataclasses

import numpy
import pyvista

from . import inp
from . import _show
from . import abc
from .Inp import Inp


@dataclasses.dataclass
class Visualize(abc.Utility):
    """
    Visualizes input files.

    Attributes:
        file: Input file to visualize.
    """

    file: Inp

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
        Visualizes all cells.
        """

        assert isinstance(self.file.surfaces, abc.Array)
        assert all(isinstance(card, (inp.card.Comment | inp.card.Surface)) for card in self.file.surfaces)
        assert isinstance(self.file.cells, abc.Array)
        assert all(isinstance(card, (inp.card.Comment | inp.card.Cell)) for card in self.file.cells)

        plot = pyvista.Plotter()
        pyvista.Plotter.add_axes(plot)

        surfaces = {str(surface.j): surface.to_show() for surface in self.file.surfaces if not isinstance(surface, inp.card.Comment)}
        cells = {}

        for cell in self.file.cells:
            if isinstance(cell, inp.card.Comment):
                continue

            shape = cell.to_show(surfaces, cells)
            cells[str(cell.j)] = shape

            grid = self._grid
            grid['cell'] = shape.cell(grid.points).astype(numpy.float32)
            plot.add_volume(grid, scalars='cell', opacity=[0, 0, 0.01, 0.01])
            plot.add_mesh(shape.surface, opacity=0.9)

        return plot

    def to_show_surfaces(self, skip=tuple()) -> pyvista.Plotter:
        """
        Visualizes INP all surfaces.
        """

        assert isinstance(self.file.surfaces, abc.Array)
        assert all(isinstance(card, (inp.card.Comment, inp.card.Surface)) for card in self.file.surfaces)
        assert isinstance(self.file.cells, abc.Array)
        assert all(isinstance(card, (inp.card.Comment, inp.card.Cell)) for card in self.file.cells)

        plot = pyvista.Plotter()
        pyvista.Plotter.add_axes(plot)

        for surface in self.file.surfaces:
            if isinstance(surface, inp.card.Comment):
                continue
            shape = surface.to_show()

            plot.add_mesh(shape.surface)

        return plot

    def to_show_cell(self, *number: str) -> pyvista.Plotter:
        """
        Visualizes input cell `number`.

        Parameters:
            numbers: Cell to visualize.
        """

        assert isinstance(self.file.surfaces, abc.Array)
        assert all(isinstance(card, (inp.card.Comment | inp.card.Surface)) for card in self.file.surfaces)
        assert isinstance(self.file.cells, abc.Array)
        assert all(isinstance(card, (inp.card.Comment | inp.card.Cell)) for card in self.file.cells)

        plot = pyvista.Plotter()
        pyvista.Plotter.add_axes(plot)

        surfaces = {str(surface.j): surface.to_show() for surface in self.file.surfaces if not isinstance(surface, inp.card.Comment)}
        cells = {}

        for cell in self.file.cells:
            if isinstance(cell, inp.card.Comment):
                continue

            shape = cell.to_show(surfaces, cells)
            cells[str(cell.j)] = shape

            if str(cell.j) not in number:
                continue

            grid = self._grid
            grid['cell'] = shape.cell(grid.points).astype(numpy.float32)
            plot.add_volume(grid, scalars='cell', opacity=[0, 0, 0.01, 0.01])
            plot.add_mesh(shape.surface, opacity=0.9)

        return plot

    def to_show_surface(self, *number: str) -> pyvista.Plotter:
        """
        Visualizes INP surface(s).

        Parameters:
            number: Surface number to visualize.
        """

        assert isinstance(self.file.surfaces, abc.Array)
        assert all(isinstance(card, (inp.card.Comment | inp.card.Surface)) for card in self.file.surfaces)
        assert isinstance(self.file.cells, abc.Array)
        assert all(isinstance(card, (inp.card.Comment | inp.card.Cell)) for card in self.file.cells)

        plot = pyvista.Plotter()
        pyvista.Plotter.add_axes(plot)

        for surface in self.file.surfaces:
            if isinstance(surface, inp.card.Comment):
                continue

            if str(surface.j) not in number:
                continue

            plot.add_mesh(surface.to_show().surface)

        return plot

    def to_pdf_cells(self, path: pathlib.Path | str):
        """
        Saves render of cells as PDF.

        Parameters:
            path: Path to new pdf file.
        """

        plot = self.to_show_cells()

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))

    def to_pdf_surfaces(self, path: pathlib.Path | str):
        """
        Saves render of surfaces as PDF.

        Parameters:
            path: Path to new pdf file.
        """

        plot = self.to_show_surfaces()

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))

    def to_pdf_cell(self, path: pathlib.Path | str, *number: str):
        """
        Saves render of cells as PDF.

        Parameters:
            path: Path to new pdf file.
            number: Cell numbers to visualize.
        """

        plot = self.to_show_cell(*number)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))

    def to_pdf_surface(self, path: pathlib.Path | str, *number: str):
        """
        Saves render of surfaces as PDF.

        Parameters:
            path: Path to new pdf file.
            number: Surface numbers to visualize.
        """

        plot = self.to_show_surface(*number)

        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            plot.save_graphic(str(path))
