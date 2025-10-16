import pymcnp
from ..... import consts
from ..... import classes


class Test_Entry:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.filter.Entry
        EXAMPLES_VALID = [
            {
                'lower': consts.string.types.REAL,
                'variable': consts.string.types.STRING,
                'upper': consts.string.types.REAL,
            },
            {
                'lower': 0.5,
                'variable': consts.string.types.STRING,
                'upper': 0.5,
            },
            {
                'lower': consts.ast.types.REAL,
                'variable': consts.ast.types.STRING,
                'upper': consts.ast.types.REAL,
            },
            {
                'lower': consts.ast.types.REAL,
                'variable': None,
                'upper': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'lower': None,
                'variable': consts.ast.types.STRING,
                'upper': consts.ast.types.REAL,
            },
            {
                'lower': consts.ast.types.REAL,
                'variable': consts.ast.types.STRING,
                'upper': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.filter.Entry
        EXAMPLES_VALID = [consts.string.inp.ptrac.filter.ENTRY]
        EXAMPLES_INVALID = ['hello']
