import pymcnp
from .... import consts
from .... import classes


class Test_Leb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Leb
        EXAMPLES_VALID = [
            {'yzere': consts.ast.type.REAL, 'bzere': consts.ast.type.REAL, 'yzero': consts.ast.type.REAL, 'bzero': consts.ast.type.REAL},
            {'yzere': None, 'bzere': consts.ast.type.REAL, 'yzero': consts.ast.type.REAL, 'bzero': consts.ast.type.REAL},
            {'yzere': consts.ast.type.REAL, 'bzere': None, 'yzero': consts.ast.type.REAL, 'bzero': consts.ast.type.REAL},
            {'yzere': consts.ast.type.REAL, 'bzere': consts.ast.type.REAL, 'yzero': None, 'bzero': consts.ast.type.REAL},
            {'yzere': consts.ast.type.REAL, 'bzere': consts.ast.type.REAL, 'yzero': consts.ast.type.REAL, 'bzero': None},
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Leb
        EXAMPLES_VALID = [consts.string.inp.data.LEB]
        EXAMPLES_INVALID = ['hello']


class Test_LebBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.LebBuilder
        EXAMPLES_VALID = [
            {'yzere': consts.string.type.REAL, 'bzere': consts.string.type.REAL, 'yzero': consts.string.type.REAL, 'bzero': consts.string.type.REAL},
            {'yzere': 3.1, 'bzere': 3.1, 'yzero': 3.1, 'bzero': 3.1},
            {'yzere': consts.ast.type.REAL, 'bzere': consts.ast.type.REAL, 'yzero': consts.ast.type.REAL, 'bzero': consts.ast.type.REAL},
            {'yzere': None, 'bzere': consts.string.type.REAL, 'yzero': consts.string.type.REAL, 'bzero': consts.string.type.REAL},
            {'yzere': consts.string.type.REAL, 'bzere': None, 'yzero': consts.string.type.REAL, 'bzero': consts.string.type.REAL},
            {'yzere': consts.string.type.REAL, 'bzere': consts.string.type.REAL, 'yzero': None, 'bzero': consts.string.type.REAL},
            {'yzere': consts.string.type.REAL, 'bzere': consts.string.type.REAL, 'yzero': consts.string.type.REAL, 'bzero': None},
        ]
        EXAMPLES_INVALID = [
            {'yzere': -3.1, 'bzere': consts.string.type.REAL, 'yzero': consts.string.type.REAL, 'bzero': consts.string.type.REAL},
            {'yzere': consts.string.type.REAL, 'bzere': -3.1, 'yzero': consts.string.type.REAL, 'bzero': consts.string.type.REAL},
            {'yzere': consts.string.type.REAL, 'bzere': consts.string.type.REAL, 'yzero': -3.1, 'bzero': consts.string.type.REAL},
            {'yzere': consts.string.type.REAL, 'bzere': consts.string.type.REAL, 'yzero': consts.string.type.REAL, 'bzero': -3.1},
        ]
