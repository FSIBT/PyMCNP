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

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.History
        EXAMPLES_VALID = [consts.string.ptrac.HISTORY]
        EXAMPLES_INVALID = ['hello']
