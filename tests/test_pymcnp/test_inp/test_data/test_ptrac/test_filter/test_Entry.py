import pymcnp
from ...... import consts
from ...... import classes


class Test_Entry:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.filter.Entry
        EXAMPLES_VALID = [
            {
                'lower': consts.string.type.REAL,
                'variable': consts.string.type.STRING,
                'upper': consts.string.type.REAL,
            },
            {
                'lower': 0.5,
                'variable': consts.string.type.STRING,
                'upper': 0.5,
            },
            {
                'lower': consts.ast.type.REAL,
                'variable': consts.ast.type.STRING,
                'upper': consts.ast.type.REAL,
            },
            {
                'lower': consts.ast.type.REAL,
                'variable': None,
                'upper': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'lower': None,
                'variable': consts.ast.type.STRING,
                'upper': consts.ast.type.REAL,
            },
            {
                'lower': consts.ast.type.REAL,
                'variable': consts.ast.type.STRING,
                'upper': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.filter.Entry
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.filter.ENTRY]
        EXAMPLES_INVALID = ['hello']
