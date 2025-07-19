import pytest

import pymcnp
from ... import consts
from ... import classes


class Test_Tuple:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Tuple
        EXAMPLES_VALID = [
            {'value': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'value': [None]},
            {'value': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Tuple
        EXAMPLES_VALID = [
            consts.string.types.TUPLE,
        ]
        EXAMPLES_INVALID = []

        def test_valid(self):
            """
            Tests ``EXAMPLES_VALID`` on ``from_mcnp`` and ``to_mcnp``.
            """

            for example in self.EXAMPLES_VALID:
                print(repr(example))

                a = self.element.from_mcnp(example, pymcnp.types.Real)
                print(repr(a.to_mcnp()))
                b = self.element.from_mcnp(a.to_mcnp(), pymcnp.types.Real)
                print(repr(b.to_mcnp()))

                assert a.to_mcnp() == b.to_mcnp()
