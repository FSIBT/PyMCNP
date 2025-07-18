import pymcnp
from .... import consts
from .... import classes


class Test_I:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.history.I
        EXAMPLES_VALID = [
            {
                'nps': consts.ast.types.INTEGER,
                'event_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'number': consts.ast.types.INTEGER,
                'tfc': consts.ast.types.REAL,
            },
            {
                'nps': consts.ast.types.INTEGER,
                'event_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'number': None,
                'tfc': consts.ast.types.REAL,
            },
            {
                'nps': consts.ast.types.INTEGER,
                'event_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'number': consts.ast.types.INTEGER,
                'tfc': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'nps': None,
                'event_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'number': consts.ast.types.INTEGER,
                'tfc': consts.ast.types.REAL,
            },
            {
                'nps': consts.ast.types.INTEGER,
                'event_type': None,
                'number': consts.ast.types.INTEGER,
                'tfc': consts.ast.types.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.I
        EXAMPLES_VALID = [consts.string.ptrac.history.I]
        EXAMPLES_INVALID = ['hello']
