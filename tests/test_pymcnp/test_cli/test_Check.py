import pathlib
import subprocess

import pymcnp
from ... import classes


class Test_Check:
    class Test_Init(classes.Test_Init):
        element = pymcnp.cli.Check
        EXAMPLES_VALID = [{'path': pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A.i'}]
        EXAMPLES_INVALID = [
            {'path': None},
        ]

    class Test_Methods:
        element = pymcnp.cli.Check
        EXAMPLES = [{'path': pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A.i'}]

        def test_check(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.check()

        def test_fix(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.check()


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A.i')])
            subprocess.run(['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_C.i'), '--fix'])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'check', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'invalid_A.i')])
            subprocess.run(['pymcnp', 'check', 'hello'])
