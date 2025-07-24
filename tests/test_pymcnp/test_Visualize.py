import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Visualize:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Visualize
        EXAMPLES_VALID = [
            {'inp': consts.ast.INP},
        ]
        EXAMPLES_INVALID = [{'inp': None}]

    class Test_Methods:
        element = pymcnp.Visualize
        EXAMPLES = [{'inp': consts.ast.INP}]

        def test_to_show_surfaces(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_surfaces()

        def test_to_show_cells(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_cells()

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
