import pathlib


import pymcnp
from .. import consts
from .. import classes


class Test_Visualize:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Visualize
        EXAMPLES_VALID = [
            {'inpt': consts.ast.INP},
        ]
        EXAMPLES_INVALID = [{'inpt': None}]

    class Test_Methods:
        element = pymcnp.Visualize
        EXAMPLES = [{'inpt': consts.ast.INP}]

        def test_to_show_surfaces(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_surfaces()

        def test_to_show_cells(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_cells()

        def test_to_show_surface(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_surface('1')

        def test_to_show_cell(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_cell('1')

        def test_to_pdf_surfaces(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_pdf_surfaces(path)

        def test_to_pdf_cells(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_pdf_cells(path)

        def test_to_pdf_surface(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_pdf_surface('1', path)

        def test_to_pdf_cell(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_pdf_cell('1', path)
