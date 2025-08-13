import pymcnp
from .... import consts
from .... import classes


class Test_File:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.files.File
        EXAMPLES_VALID = [
            {
                'unit': consts.string.types.INTEGER,
                'filename': consts.string.types.STRING,
                'access': 's',
                'form': 'f',
                'length': consts.string.types.INTEGER,
            },
            {
                'unit': 1,
                'filename': consts.string.types.STRING,
                'access': 's',
                'form': 'f',
                'length': 1,
            },
            {
                'unit': consts.ast.types.INTEGER,
                'filename': consts.ast.types.STRING,
                'access': pymcnp.types.String('s'),
                'form': pymcnp.types.String('f'),
                'length': consts.ast.types.INTEGER,
            },
            {
                'unit': consts.string.types.INTEGER,
                'filename': consts.string.types.STRING,
                'access': None,
                'form': 'f',
                'length': consts.string.types.INTEGER,
            },
            {
                'unit': consts.string.types.INTEGER,
                'filename': consts.string.types.STRING,
                'access': 's',
                'form': None,
                'length': consts.string.types.INTEGER,
            },
            {
                'unit': consts.string.types.INTEGER,
                'filename': consts.string.types.STRING,
                'access': 's',
                'form': 'f',
                'length': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'unit': None,
                'filename': consts.string.types.STRING,
                'access': 's',
                'form': 'f',
                'length': consts.string.types.INTEGER,
            },
            {
                'unit': consts.string.types.INTEGER,
                'filename': None,
                'access': 's',
                'form': 'f',
                'length': consts.string.types.INTEGER,
            },
            {
                'unit': consts.string.types.INTEGER,
                'filename': consts.string.types.STRING,
                'access': 'hello',
                'form': 'f',
                'length': consts.string.types.INTEGER,
            },
            {
                'unit': consts.string.types.INTEGER,
                'filename': consts.string.types.STRING,
                'access': 's',
                'form': 'hello',
                'length': consts.string.types.INTEGER,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.files.File
        EXAMPLES_VALID = [consts.string.inp.files.FILE]
        EXAMPLES_INVALID = ['hello']
