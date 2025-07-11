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
            for example in self.EXAMPLES:
                element = self.element(example['outp'])
                element.to_csv(example['number'], pathlib.Path('hello.csv')).unlink()

        def test_fix(self):
            for example in self.EXAMPLES:
                element = self.element(example['outp'])
                element.to_parquet(example['number'], pathlib.Path('hello.parquet')).unlink()


class Test_Main:
    class Test_Main:
        def test_valid(self):
            subprocess.run(['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_A.o'), '1', '--csv'])
            subprocess.run(['rm', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_A-1.csv')])
            subprocess.run(['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_A.o'), '1', '--parquet'])
            subprocess.run(['rm', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_A-1.parquet')])

        def test_invalid(self):
            subprocess.run(['pymcnp', 'convert', str(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'invalid_A.i'), '1', '--csv'])
            subprocess.run(['pymcnp', 'convert', 'hello', '1', '--csv'])
