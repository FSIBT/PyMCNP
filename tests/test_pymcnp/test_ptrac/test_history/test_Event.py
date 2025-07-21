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

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.Event
        EXAMPLES_VALID = [consts.string.ptrac.history.EVENT]
        EXAMPLES_INVALID = ['hello']
