import pathlib
import subprocess

import pymcnp
from ... import consts
from ... import classes


class Test_Plot:
    class Test_Init(classes.Test_Init):
        element = pymcnp.cli.Plot
        EXAMPLES_VALID = [
            {'outp': consts.ast.OUTP},
        ]
        EXAMPLES_INVALID = [{'outp': None}]

    class Test_Methods:
        element = pymcnp.cli.Plot
        EXAMPLES = [{'outp': consts.ast.OUTP, 'number': '1'}]

        def test_to_show(self):
            for example in self.EXAMPLES:
                element = self.element(example['outp'])
                element.to_show(example['number'])

        def test_to_pdf(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(example['outp'])
                element.to_pdf(example['number'], path)


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_A.o'), '1'])
            subprocess.run(['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_A.o'), '1', '--pdf'])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'invalid_A.o'), '1'])
            subprocess.run(['pymcnp', 'plot', 'hello', '1'])
