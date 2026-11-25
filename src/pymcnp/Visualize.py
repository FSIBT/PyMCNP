import pathlib
import dataclasses

import numpy
import pyvista

from . import inp as inp_
from . import _show
from . import abc
from .Inp import Inp


def _numbers(numbers) -> set[str]:
    # Card numbers as plain strings, so ``1``, ``'1'``, ``' 1 '`` and ``Integer('1')`` all match.
    return {str(number).strip() for number in numbers}


@dataclasses.dataclass
class Visualize(abc.Utility):
    """
    Visualizes input files.
    """

    def _grid(self, inp: Inp):
        surfaces = self.to_show_surfaces(inp)

        return pyvista.ImageData(
            dimensions=(_show.pyvista.RESOLUTION, _show.pyvista.RESOLUTION, _show.pyvista.RESOLUTION),
            spacing=(
                (surfaces.bounds[1] - surfaces.bounds[0]) / _show.pyvista.RESOLUTION,
                (surfaces.bounds[3] - surfaces.bounds[2]) / _show.pyvista.RESOLUTION,
                (surfaces.bounds[5] - surfaces.bounds[4]) / _show.pyvista.RESOLUTION,
            ),
            origin=(-(surfaces.bounds[1] - surfaces.bounds[0]) / 2, -(surfaces.bounds[3] - surfaces.bounds[2]) / 2, -(surfaces.bounds[5] - surfaces.bounds[4]) / 2),
        )

    def to_show_cell(self, inp: Inp, *number: int | str) -> pyvista.Plotter:
        """
        Visualizes input cell ``number``.

        Parameters:
            numbers: Cell to visualize.
        """

        plot = pyvista.Plotter()
        pyvista.Plotter.add_axes(plot)

        number = _numbers(number)
        surfaces = {str(surface.j): surface.to_show() for surface in inp.surfaces.filter(inp_.card.Surface)}
        cells = {}

        for cell in inp.cells.filter(inp_.card.Cell):
            shape = cell.to_show(surfaces, cells)
            cells[str(cell.j)] = shape

            if str(cell.j).strip() not in number:
                continue

            grid = self._grid(inp)
            grid['cell'] = shape.cell(grid.points).astype(numpy.float32)
            plot.add_volume(grid, scalars='cell', opacity=numpy.array([0, 0, 0.01, 0.01]))
            plot.add_mesh(shape.surface, opacity=0.9)

        return plot

    def to_show_surface(self, inp: Inp, *number: int | str) -> pyvista.Plotter:
        """
        Visualizes INP surface(s).

        Parameters:
            number: Surface number to visualize.
        """

        plot = pyvista.Plotter()
        pyvista.Plotter.add_axes(plot)

        number = _numbers(number)

        for surface in inp.surfaces.filter(inp_.card.Surface):
            if str(surface.j).strip() not in number:
                continue

            plot.add_mesh(surface.to_show().surface)

        return plot

    def to_show_cells(self, inp: Inp, skip=()) -> pyvista.Plotter:
        """
        Visualizes all cells.

        Parameters:
            skip: Cell numbers to leave out.
        """

        skip = _numbers(skip)
        plot = pyvista.Plotter()
        pyvista.Plotter.add_axes(plot)

        surfaces = {str(surface.j): surface.to_show() for surface in inp.surfaces.filter(inp_.card.Surface)}
        cells = {}

        for cell in inp.cells.filter(inp_.card.Cell):
            # Skipped cells are still resolved, since other cells may refer to them with ``#``.
            shape = cell.to_show(surfaces, cells)
            cells[str(cell.j)] = shape

            if str(cell.j).strip() in skip:
                continue

            grid = self._grid(inp)
            grid['cell'] = shape.cell(grid.points).astype(numpy.float32)
            plot.add_volume(grid, scalars='cell', opacity=numpy.array([0, 0, 0.01, 0.01]))
            plot.add_mesh(shape.surface, opacity=0.9)

        return plot

    def to_show_surfaces(self, inp: Inp, skip=()) -> pyvista.Plotter:
        """
        Visualizes INP all surfaces.

        Parameters:
            skip: Surface numbers to leave out.
        """

        skip = _numbers(skip)
        plot = pyvista.Plotter()
        pyvista.Plotter.add_axes(plot)

        for surface in inp.surfaces.filter(inp_.card.Surface):
            if str(surface.j).strip() in skip:
                continue

            shape = surface.to_show()

            plot.add_mesh(shape.surface)

        return plot

    def to_pdf_cells(self, inp: Inp, path: pathlib.Path | str, skip=()):
        """
        Saves render of cells as PDF.

        Parameters:
            path: Path to new pdf file.
            skip: Cells numbers to leave out.
        """

        plot = self.to_show_cells(inp, skip=skip)

        plot.save_graphic(str(path))

    def to_pdf_surfaces(self, inp: Inp, path: pathlib.Path | str, skip=()):
        """
        Saves render of surfaces as PDF.

        Parameters:
            path: Path to new pdf file.
            skip: Surfaces numbers to leave out.
        """

        plot = self.to_show_surfaces(inp, skip=skip)

        plot.save_graphic(str(path))

    def to_pdf_cell(self, inp: Inp, path: pathlib.Path | str, *number: int | str):
        """
        Saves render of cells as PDF.

        Parameters:
            path: Path to new pdf file.
            number: Cell numbers to visualize.
        """

        plot = self.to_show_cell(inp, *number)

        plot.save_graphic(str(path))

    def to_pdf_surface(self, inp: Inp, path: pathlib.Path | str, *number: int | str):
        """
        Saves render of surfaces as PDF.

        Parameters:
            path: Path to new pdf file.
            number: Surface numbers to visualize.
        """

        plot = self.to_show_surface(inp, *number)

        plot.save_graphic(str(path))
