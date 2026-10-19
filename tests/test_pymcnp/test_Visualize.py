import pathlib

import pymcnp


class Test_Visualize:
    def test_to_show_surfaces_valid(self, visualize: pymcnp.Visualize) -> None:
        visualize.to_show_surfaces()

    def test_to_show_cells_valid(self, visualize: pymcnp.Visualize) -> None:
        visualize.to_show_cells()

    def test_to_show_surface_valid(self, visualize: pymcnp.Visualize) -> None:
        visualize.to_show_surface('1')

    def test_to_show_cell_valid(self, visualize: pymcnp.Visualize) -> None:
        visualize.to_show_cell('1')
        visualize.to_show_cell('4')

    def test_to_pdf_surfaces_valid(self, visualize: pymcnp.Visualize) -> None:
        visualize.to_pdf_surfaces(pathlib.Path('hello.pdf'))

    def test_to_pdf_cells_valid(self, visualize: pymcnp.Visualize) -> None:
        visualize.to_pdf_cells(pathlib.Path('hello.pdf'))

    def test_to_pdf_surface_valid(self, visualize: pymcnp.Visualize) -> None:
        visualize.to_pdf_surface(pathlib.Path('hello.pdf'), '1')

    def test_to_pdf_cell_valid(self, visualize: pymcnp.Visualize) -> None:
        visualize.to_pdf_cell(pathlib.Path('hello.pdf'), '1')
