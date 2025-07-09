import pymcnp
from .... import consts
from .... import classes


class Test_I:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.history.I
        EXAMPLES_VALID = [
            {
                'nps': consts.ast.type.INTEGER,
                'event_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'number': consts.ast.type.INTEGER,
                'tfc': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'nps': None,
                'event_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'number': consts.ast.type.INTEGER,
                'tfc': consts.ast.type.REAL,
            },
            {
                'nps': consts.ast.type.INTEGER,
                'event_type': None,
                'number': consts.ast.type.INTEGER,
                'tfc': consts.ast.type.REAL,
            },
            {
                'nps': consts.ast.type.INTEGER,
                'event_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'number': None,
                'tfc': consts.ast.type.REAL,
            },
            {
                'nps': consts.ast.type.INTEGER,
                'event_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'number': consts.ast.type.INTEGER,
                'tfc': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.I
        EXAMPLES_VALID = [consts.string.ptrac.history.I]
        EXAMPLES_INVALID = ['hello']
