import pymcnp
from ... import consts
from ... import classes


class Test_Fu:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Fu
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 'nt': 'nt', 'c': 'c'},
            {'suffix': 1, 'bounds': [3.1], 'nt': 'nt', 'c': 'c'},
            {'suffix': consts.ast.types.INTEGER, 'bounds': [consts.ast.types.REAL], 'nt': pymcnp.types.String('nt'), 'c': pymcnp.types.String('c')},
            {'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 'nt': None, 'c': 'c'},
            {'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 'nt': 'nt', 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'bounds': [consts.string.types.REAL], 'nt': 'nt', 'c': 'c'},
            {'suffix': consts.string.types.INTEGER, 'bounds': None, 'nt': 'nt', 'c': 'c'},
            {'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 'nt': 'hello', 'c': 'c'},
            {'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL], 'nt': 'nt', 'c': 'hello'},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Fu
        EXAMPLES_VALID = [consts.string.inp.FU]
        EXAMPLES_INVALID = ['hello']
