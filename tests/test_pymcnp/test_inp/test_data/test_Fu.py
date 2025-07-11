import pymcnp
from .... import consts
from .... import classes


class Test_Fu:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Fu
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 'nt': 'nt', 'c': 'c'},
            {'suffix': 1, 'bounds': [3.1], 'nt': 'nt', 'c': 'c'},
            {'suffix': consts.ast.type.INTEGER, 'bounds': [consts.ast.type.REAL], 'nt': pymcnp.types.String('nt'), 'c': pymcnp.types.String('c')},
            {'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 'nt': None, 'c': 'c'},
            {'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 'nt': 'nt', 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'bounds': [consts.string.type.REAL], 'nt': 'nt', 'c': 'c'},
            {'suffix': consts.string.type.INTEGER, 'bounds': None, 'nt': 'nt', 'c': 'c'},
            {'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 'nt': 'hello', 'c': 'c'},
            {'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL], 'nt': 'nt', 'c': 'hello'},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Fu
        EXAMPLES_VALID = [consts.string.inp.data.FU]
        EXAMPLES_INVALID = ['hello']
