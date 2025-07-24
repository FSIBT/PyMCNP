import pathlib

import matplotlib.pyplot

import pymcnp
from .. import consts
from .. import classes


class Test_Plot:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Plot
        EXAMPLES_VALID = [
            {'outp': consts.ast.OUTP},
        ]
        EXAMPLES_INVALID = [{'outp': None}]

    class Test_Methods:
        element = pymcnp.Plot
        EXAMPLES = [{'outp': consts.ast.OUTP, 'number': '1'}]

        def test_to_show(self):
            for example in self.EXAMPLES:
                element = self.element(example['outp'])
                element.to_show(example['number'])

            matplotlib.pyplot.close()

        def test_to_pdf(self):
            path = pathlib.Path('hello.pdf')

            for example in self.EXAMPLES:
                element = self.element(example['outp'])
                element.to_pdf(example['number'], path)
