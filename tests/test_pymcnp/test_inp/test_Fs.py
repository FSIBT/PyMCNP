import pymcnp
from ... import consts
from ... import classes


class Test_Fs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Fs
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'numbers': [consts.string.types.INTEGER], 't': 't', 'c': 'c'},
            {'suffix': 1, 'numbers': [1], 't': 't', 'c': 'c'},
            {'suffix': consts.ast.types.INTEGER, 'numbers': [consts.ast.types.INTEGER], 't': pymcnp.types.String('t'), 'c': pymcnp.types.String('c')},
            {'suffix': consts.string.types.INTEGER, 'numbers': [consts.string.types.INTEGER], 't': None, 'c': 'c'},
            {'suffix': consts.string.types.INTEGER, 'numbers': [consts.string.types.INTEGER], 't': 't', 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'numbers': [consts.string.types.INTEGER], 't': 't', 'c': 'c'},
            {'suffix': consts.string.types.INTEGER, 'numbers': None, 't': 't', 'c': 'c'},
            {'suffix': consts.string.types.INTEGER, 'numbers': [consts.string.types.INTEGER], 't': 'hello', 'c': 'c'},
            {'suffix': consts.string.types.INTEGER, 'numbers': [consts.string.types.INTEGER], 't': 't', 'c': 'hello'},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Fs
        EXAMPLES_VALID = [consts.string.inp.FS]
        EXAMPLES_INVALID = ['hello']
