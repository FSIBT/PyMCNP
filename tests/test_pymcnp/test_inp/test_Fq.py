import pymcnp
from ... import consts
from ... import classes


class Test_Fq:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Fq
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': 1, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {
                'suffix': consts.ast.types.INTEGER,
                'a1': pymcnp.types.String('t'),
                'a2': pymcnp.types.String('t'),
                'a3': pymcnp.types.String('t'),
                'a4': pymcnp.types.String('t'),
                'a5': pymcnp.types.String('t'),
                'a6': pymcnp.types.String('t'),
                'a7': pymcnp.types.String('t'),
                'a8': pymcnp.types.String('t'),
            },
            {'suffix': None, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': None, 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': None, 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': None, 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': None, 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': None, 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': None, 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': None, 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': 100000000, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 'hello', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 'hello', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 'hello', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 'hello', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 'hello', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 'hello', 'a7': 't', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 'hello', 'a8': 't'},
            {'suffix': consts.string.types.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 'hello'},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Fq
        EXAMPLES_VALID = [consts.string.inp.FQ]
        EXAMPLES_INVALID = ['hello']
