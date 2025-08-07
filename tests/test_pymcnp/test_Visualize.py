import pathlib

import pytest

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
                element.to_show_surface('2')

            with pytest.raises(pymcnp.errors.CliError):
                element.to_show_surface('13209458743')

        def test_to_show_cell(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.to_show_cell('1')
                element.to_show_cell('2')

            with pytest.raises(pymcnp.errors.CliError):
                element.to_show_cell('13209458743')

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
