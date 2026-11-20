import pathlib

import pymcnp


class Test_Visualize:
    def test_to_show_surfaces_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_surfaces(
            inp,
        )

    def test_to_show_cells_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_cells(
            inp,
        )

    def test_to_show_surface_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_surface(inp, '1')

    def test_to_show_cell_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_cell(inp, '1')
        visualizer.to_show_cell(inp, '4')

    def test_to_pdf_surfaces_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_surfaces(inp, pathlib.Path('hello.pdf'))

    def test_to_pdf_cells_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_cells(inp, pathlib.Path('hello.pdf'))

    def test_to_pdf_surface_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_surface(inp, pathlib.Path('hello.pdf'), '1')

    def test_to_pdf_cell_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_cell(inp, pathlib.Path('hello.pdf'), '1')
