import pathlib

import pymcnp
from .. import classes


class Test_Check:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Check
        EXAMPLES_VALID = [{'path': pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'}]
        EXAMPLES_INVALID = [
            {'path': None},
        ]

    class Test_Methods:
        element = pymcnp.Check
        EXAMPLES = [{'path': pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'}]

        def test_check(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.check()

        def test_fix(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.check()
