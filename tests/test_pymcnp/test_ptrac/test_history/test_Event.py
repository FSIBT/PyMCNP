import pytest

import pymcnp
from .... import consts
from .... import classes


class Test_Event:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.history.Event
        EXAMPLES_VALID = [
            {
                'j_line': consts.ast.ptrac.history.event.J_0,
                'p_line': consts.ast.ptrac.history.event.P_0,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'j_line': None,
                'p_line': consts.ast.ptrac.history.event.P_0,
            },
            {
                'j_line': consts.ast.ptrac.history.event.J_0,
                'p_line': None,
            },
        ]

    class Test_Mcnp:
        element = pymcnp.ptrac.history.Event
        EXAMPLES_VALID = [consts.string.ptrac.history.EVENT]
        EXAMPLES_INVALID = ['hello']

        def test_valid(self):
            """
            Tests ``EXAMPLES_VALID`` on ``from_mcnp`` and ``to_mcnp``.
            """

            for example in self.EXAMPLES_VALID:
                print(repr(example))

                a = self.element.from_mcnp(example, consts.ast.ptrac.history.I, consts.ast.ptrac.HEADER)
                print(repr(a.to_mcnp()))
                b = self.element.from_mcnp(a.to_mcnp(), consts.ast.ptrac.history.I, consts.ast.ptrac.HEADER)

                assert a.to_mcnp() == b.to_mcnp()

        def test_invalid(self):
            """
            Tests ``EXAMPLES_INVALID`` on ``from_mcnp``.
            """

            for example in self.EXAMPLES_INVALID:
                with pytest.raises((pymcnp.utils.errors.Error)):
                    print(repr(example))

                    self.element.from_mcnp(example, consts.ast.ptrac.history.I, consts.ast.ptrac.HEADER)
