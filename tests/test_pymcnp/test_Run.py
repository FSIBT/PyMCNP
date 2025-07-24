import shutil
import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Run:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Run
        EXAMPLES_VALID = [{'inps': [consts.ast.INP], 'command': 'echo'}]
        EXAMPLES_INVALID = [
            {'inps': [None], 'command': 'echo'},
            {'inps': [consts.ast.INP], 'command': None},
        ]

    class Test_Methods:
        element = pymcnp.Run
        PATH = pathlib.Path('.')
        EXAMPLES = [{'inps': [consts.ast.INP], 'command': 'echo'}]

        def test_prehook_file(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.prehook_file(self.PATH, 0)

        def test_posthook_file(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.posthook_file(self.PATH, 0)

        def test_prehook_batch(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.prehook_batch(self.PATH)

        def test_posthook_batch(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.posthook_batch(self.PATH)

        def test_run(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                directory = element.run(self.PATH)
                shutil.rmtree(directory)
