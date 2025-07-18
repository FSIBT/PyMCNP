import pathlib
import subprocess

import pymcnp
from ... import consts
from ... import classes


class Test_Convert:
    class Test_Init(classes.Test_Init):
        element = pymcnp.cli.Convert
        EXAMPLES_VALID = [
            {'outp': consts.ast.OUTP},
        ]
        EXAMPLES_INVALID = [{'outp': None}]

    class Test_Methods:
        element = pymcnp.cli.Convert
        EXAMPLES = [
            {'outp': consts.ast.OUTP, 'number': '1'},
        ]

        def test_check(self):
            path = pathlib.Path('hello.csv')

            for example in self.EXAMPLES:
                element = self.element(example['outp'])
                element.to_csv(example['number'], path)

        def test_fix(self):
            path = pathlib.Path('hello.parquet')

            for example in self.EXAMPLES:
                element = self.element(example['outp'])
                element.to_parquet(example['number'], path)


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'example_00.outp'), '1', '--csv'])
            subprocess.run(['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'example_00.outp'), '1', '--parquet'])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp'), '1', '--csv'])
            subprocess.run(['pymcnp', 'convert', 'hello', '1', '--csv'])
