import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Convert:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Convert
        EXAMPLES_VALID = [
            {'outp': consts.ast.OUTP},
        ]
        EXAMPLES_INVALID = [{'outp': None}]

    class Test_Methods:
        element = pymcnp.Convert
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
