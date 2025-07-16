import pymcnp
from ..... import consts
from ..... import classes


class Test_J_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.history.event.J_0
        EXAMPLES_VALID = [
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'pbl': consts.ast.types.INTEGER,
                'nsr': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'next_type': None,
                'pbl': consts.ast.types.INTEGER,
                'nsr': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'pbl': None,
                'nsr': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'pbl': consts.ast.types.INTEGER,
                'nsr': None,
                'ncl': consts.ast.types.INTEGER,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'pbl': consts.ast.types.INTEGER,
                'nsr': consts.ast.types.INTEGER,
                'ncl': None,
                'mat': consts.ast.types.INTEGER,
            },
            {
                'next_type': consts.ast.ptrac.history.event.j.EVENT_TYPE,
                'pbl': consts.ast.types.INTEGER,
                'nsr': consts.ast.types.INTEGER,
                'ncl': consts.ast.types.INTEGER,
                'mat': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.history.event.J_0
        EXAMPLES_VALID = [consts.string.ptrac.history.event.J_0]
        EXAMPLES_INVALID = ['hello']
