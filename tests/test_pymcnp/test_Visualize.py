import pathlib

import pytest
import pyvista

import pymcnp


EXAMPLE = pathlib.Path(__file__).parent.parent.parent / 'examples' / 'example_00.inp'


pytestmark = pytest.mark.render


class Test_Visualize:
    def test_to_show_surfaces_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_surfaces(inp)

    def test_to_show_cells_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_cells(inp)

    def test_to_show_surface_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_surface(inp, '1')

    def test_to_show_cell_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_cell(inp, '1')
        visualizer.to_show_cell(inp, '4')

    def test_to_pdf_surfaces_valid(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_surfaces(inp, tmp_path / 'hello.pdf')

    def test_to_pdf_cells_valid(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_cells(inp, tmp_path / 'hello.pdf')

    def test_to_pdf_surface_valid(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_surface(inp, tmp_path / 'hello.pdf', '1')

    def test_to_pdf_cell_valid(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_cell(inp, tmp_path / 'hello.pdf', '1')

    def test_visualize_cells_runs(self) -> None:
        inp = pymcnp.Inp.from_file(EXAMPLE)[0]

        plot = pymcnp.Visualize().to_show_cells(inp)

        assert isinstance(plot, pyvista.Plotter)
        assert len(plot.renderer.actors) >= 1

    def test_visualize_pdf(self, tmp_path: pathlib.Path) -> None:
        # Renders for real, off screen (``pyvista.OFF_SCREEN`` is set in ``conftest.py``).
        inp = pymcnp.Inp.from_file(EXAMPLE)[0]
        path = tmp_path / 'c.pdf'

        pymcnp.Visualize().to_pdf_cells(inp, path)

        assert path.exists()
        assert path.stat().st_size > 0
