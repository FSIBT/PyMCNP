import shutil
import pathlib
import subprocess

import pymcnp
from ... import consts
from ... import classes


class Test_Run:
    class Test_Init(classes.Test_Init):
        element = pymcnp.cli.Run
        EXAMPLES_VALID = [{'inps': [consts.ast.INP], 'command': 'echo'}]
        EXAMPLES_INVALID = [
            {'inps': [None], 'command': 'echo'},
            {'inps': [consts.ast.INP], 'command': None},
        ]

    class Test_Methods:
        element = pymcnp.cli.Run
        PATH = pathlib.Path('.')
        EXAMPLES = [{'inps': [consts.ast.INP], 'command': 'echo'}]

        def test_prehook_file(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.prehook_file(self.PATH)

        def test_posthook_file(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.prehook_file(self.PATH)

        def test_prehook_batch(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.prehook_batch(self.PATH)

        def test_posthook_batch(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.prehook_batch(self.PATH)

        def test_run(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                directory = element.run(self.PATH)
                shutil.rmtree(directory)


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_A.i')])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'invalid_A.i')])
            subprocess.run(['pymcnp', 'run', 'hello'])
