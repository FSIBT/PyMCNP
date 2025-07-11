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

        def test_draw_surfaces(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.draw_surfaces()

        def test_draw_cells(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.draw_cells()


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A.i'), '--cells'])
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A.i'), '--surfaces'])
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A.i'), '--cells', '--pdf'])
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A.i'), '--surfaces', '--pdf'])
            subprocess.run(['rm', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A-cells.pdf')])
            subprocess.run(['rm', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A-surfaces.pdf')])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'invalid_A.i')])
            subprocess.run(['pymcnp', 'visualize', 'hello'])
