import pathlib
import subprocess

import pymcnp
from ... import consts
from ... import classes


class Test_Visualize:
    class Test_Init(classes.Test_Init):
        element = pymcnp.cli.Visualize
        EXAMPLES_VALID = [
            {'inp': consts.ast.INP},
        ]
        EXAMPLES_INVALID = [{'inp': None}]

    class Test_Methods:
        element = pymcnp.cli.Visualize
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


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cells'])
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surfaces'])
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cells', '--pdf'])
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surfaces', '--pdf'])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_A.i')])
            subprocess.run(['pymcnp', 'visualize', 'hello'])
