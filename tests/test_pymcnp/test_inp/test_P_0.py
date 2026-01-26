import pymcnp
from ... import consts
from ... import classes


class Test_P_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.P_0
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
                'd': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'a': 3.1, 'b': 3.1, 'c': 3.1, 'd': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'a': consts.ast.types.REAL,
                'b': consts.ast.types.REAL,
                'c': consts.ast.types.REAL,
                'd': consts.ast.types.REAL,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
                'd': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': None,
                'transform': consts.string.types.INTEGER,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
                'd': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': None,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
                'd': consts.string.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
                'd': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
                'd': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': '1000',
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
                'd': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'a': None,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
                'd': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'a': consts.string.types.REAL,
                'b': None,
                'c': consts.string.types.REAL,
                'd': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': None,
                'd': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
                'd': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.P_0
        EXAMPLES_VALID = [consts.string.inp.P_0]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.P_0
        EXAMPLES = [consts.string.inp.P_0]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.P_0, consts.ast.inp.P_0)]
