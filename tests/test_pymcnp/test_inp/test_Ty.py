import pymcnp
from ... import consts
from ... import classes


class Test_Ty:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ty
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'x': 3.1, 'y': 3.1, 'z': 3.1, 'a': 3.1, 'b': 3.1, 'c': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'a': consts.ast.types.REAL,
                'b': consts.ast.types.REAL,
                'c': consts.ast.types.REAL,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': None,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': None,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': '1000',
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': None,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': None,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': None,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': None,
                'b': consts.string.types.REAL,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': None,
                'c': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'a': consts.string.types.REAL,
                'b': consts.string.types.REAL,
                'c': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ty
        EXAMPLES_VALID = [consts.string.inp.TY]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Ty
        EXAMPLES = [consts.string.inp.TY]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.TY, consts.ast.inp.TY)]
