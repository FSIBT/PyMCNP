import pytest

import pymcnp
from ... import consts
from ... import classes


class Test_History:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.History
        EXAMPLES_VALID = [
            {
                'i_line': consts.ast.ptrac.history.I,
                'events': [consts.ast.ptrac.history.EVENT],
            },
        ]
        EXAMPLES_INVALID = [
            {
                'i_line': None,
                'events': [consts.ast.ptrac.history.EVENT],
            },
            {
                'i_line': consts.ast.ptrac.history.I,
                'events': [None],
            },
        ]

    class Test_Mcnp:
        element = pymcnp.ptrac.History
        EXAMPLES_VALID = [consts.string.ptrac.HISTORY]
        EXAMPLES_INVALID = ['hello']

        def test_valid(self):
            """
            Tests ``EXAMPLES_VALID`` on ``from_mcnp`` and ``to_mcnp``.
            """

            for example in self.EXAMPLES_VALID:
                print(repr(example))

                a = self.element.from_mcnp(example, consts.ast.ptrac.HEADER)
                print(repr(a.to_mcnp()))
                b = self.element.from_mcnp(a.to_mcnp(), consts.ast.ptrac.HEADER)

                assert a.to_mcnp() == b.to_mcnp()

        def test_invalid(self):
            """
            Tests ``EXAMPLES_INVALID`` on ``from_mcnp``.
            """

            for example in self.EXAMPLES_INVALID:
                with pytest.raises((pymcnp.errors.Error)):
                    print(repr(example))

                    self.element.from_mcnp(example, consts.ast.ptrac.HEADER)
