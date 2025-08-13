import pymcnp
from ... import consts
from ... import classes


class Test_Leb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Leb
        EXAMPLES_VALID = [
            {'yzere': consts.string.types.REAL, 'bzere': consts.string.types.REAL, 'yzero': consts.string.types.REAL, 'bzero': consts.string.types.REAL},
            {'yzere': 3.1, 'bzere': 3.1, 'yzero': 3.1, 'bzero': 3.1},
            {'yzere': consts.ast.types.REAL, 'bzere': consts.ast.types.REAL, 'yzero': consts.ast.types.REAL, 'bzero': consts.ast.types.REAL},
            {'yzere': None, 'bzere': consts.string.types.REAL, 'yzero': consts.string.types.REAL, 'bzero': consts.string.types.REAL},
            {'yzere': consts.string.types.REAL, 'bzere': None, 'yzero': consts.string.types.REAL, 'bzero': consts.string.types.REAL},
            {'yzere': consts.string.types.REAL, 'bzere': consts.string.types.REAL, 'yzero': None, 'bzero': consts.string.types.REAL},
            {'yzere': consts.string.types.REAL, 'bzere': consts.string.types.REAL, 'yzero': consts.string.types.REAL, 'bzero': None},
        ]
        EXAMPLES_INVALID = [
            {'yzere': -3.1, 'bzere': consts.string.types.REAL, 'yzero': consts.string.types.REAL, 'bzero': consts.string.types.REAL},
            {'yzere': consts.string.types.REAL, 'bzere': -3.1, 'yzero': consts.string.types.REAL, 'bzero': consts.string.types.REAL},
            {'yzere': consts.string.types.REAL, 'bzere': consts.string.types.REAL, 'yzero': -3.1, 'bzero': consts.string.types.REAL},
            {'yzere': consts.string.types.REAL, 'bzere': consts.string.types.REAL, 'yzero': consts.string.types.REAL, 'bzero': -3.1},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Leb
        EXAMPLES_VALID = [consts.string.inp.LEB]
        EXAMPLES_INVALID = ['hello']
