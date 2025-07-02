import pymcnp
from .... import consts
from .... import classes


class Test_Fs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Fs
        EXAMPLES_VALID = [
            {'suffix': consts.ast.type.INTEGER, 'numbers': [consts.ast.type.INTEGER], 't': pymcnp.types.String('t'), 'c': pymcnp.types.String('c')},
            {'suffix': consts.ast.type.INTEGER, 'numbers': [consts.ast.type.INTEGER], 't': None, 'c': pymcnp.types.String('c')},
            {'suffix': consts.ast.type.INTEGER, 'numbers': [consts.ast.type.INTEGER], 't': pymcnp.types.String('t'), 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'numbers': [consts.ast.type.INTEGER], 't': pymcnp.types.String('t'), 'c': pymcnp.types.String('c')},
            {'suffix': consts.ast.type.INTEGER, 'numbers': None, 't': pymcnp.types.String('t'), 'c': pymcnp.types.String('c')},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Fs
        EXAMPLES_VALID = [consts.string.inp.data.FS]
        EXAMPLES_INVALID = ['hello']


class Test_FsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.FsBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'numbers': [consts.string.type.INTEGER], 't': 't', 'c': 'c'},
            {'suffix': 1, 'numbers': [1], 't': 't', 'c': 'c'},
            {'suffix': consts.ast.type.INTEGER, 'numbers': [consts.ast.type.INTEGER], 't': pymcnp.types.String('t'), 'c': pymcnp.types.String('c')},
            {'suffix': consts.string.type.INTEGER, 'numbers': [consts.string.type.INTEGER], 't': None, 'c': 'c'},
            {'suffix': consts.string.type.INTEGER, 'numbers': [consts.string.type.INTEGER], 't': 't', 'c': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'numbers': [consts.string.type.INTEGER], 't': 't', 'c': 'c'},
            {'suffix': consts.string.type.INTEGER, 'numbers': None, 't': 't', 'c': 'c'},
            {'suffix': consts.string.type.INTEGER, 'numbers': [consts.string.type.INTEGER], 't': 'hello', 'c': 'c'},
            {'suffix': consts.string.type.INTEGER, 'numbers': [consts.string.type.INTEGER], 't': 't', 'c': 'hello'},
        ]
