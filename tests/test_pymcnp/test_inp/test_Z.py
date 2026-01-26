import pymcnp
from ... import consts
from ... import classes


class Test_Z:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Z
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'z1': 3.1, 'r1': 3.1, 'z2': 3.1, 'r2': 3.1, 'z3': 3.1, 'r3': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'z1': consts.ast.types.REAL,
                'r1': consts.ast.types.REAL,
                'z2': consts.ast.types.REAL,
                'r2': consts.ast.types.REAL,
                'z3': consts.ast.types.REAL,
                'r3': consts.ast.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': None,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': None,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': None,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': None,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': None,
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': None,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': '1000',
                'z1': consts.string.types.REAL,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z1': None,
                'r1': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'z1': consts.string.types.REAL,
                'r1': None,
                'z2': consts.string.types.REAL,
                'r2': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
                'r3': consts.string.types.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Z
        EXAMPLES_VALID = [
            # 3.2
            '12 Z 1 0 2 1 3 4',
            '12 Z 2 1 3 4 5 9.380832',
            consts.string.inp.Z,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.Z, consts.ast.inp.Z)]
