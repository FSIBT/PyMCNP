import pymcnp
from ..... import consts
from ..... import classes


class Test_File:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.files.File
        EXAMPLES_VALID = [
            {
                'unit': consts.string.type.INTEGER,
                'filename': consts.string.type.STRING,
                'access': 's',
                'form': 'f',
                'length': consts.string.type.INTEGER,
            },
            {
                'unit': 1,
                'filename': consts.string.type.STRING,
                'access': 's',
                'form': 'f',
                'length': 1,
            },
            {
                'unit': consts.ast.type.INTEGER,
                'filename': consts.ast.type.STRING,
                'access': pymcnp.utils.types.String('s'),
                'form': pymcnp.utils.types.String('f'),
                'length': consts.ast.type.INTEGER,
            },
            {
                'unit': consts.string.type.INTEGER,
                'filename': consts.string.type.STRING,
                'access': None,
                'form': 'f',
                'length': consts.string.type.INTEGER,
            },
            {
                'unit': consts.string.type.INTEGER,
                'filename': consts.string.type.STRING,
                'access': 's',
                'form': None,
                'length': consts.string.type.INTEGER,
            },
            {
                'unit': consts.string.type.INTEGER,
                'filename': consts.string.type.STRING,
                'access': 's',
                'form': 'f',
                'length': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'unit': None,
                'filename': consts.string.type.STRING,
                'access': 's',
                'form': 'f',
                'length': consts.string.type.INTEGER,
            },
            {
                'unit': consts.string.type.INTEGER,
                'filename': None,
                'access': 's',
                'form': 'f',
                'length': consts.string.type.INTEGER,
            },
            {
                'unit': consts.string.type.INTEGER,
                'filename': consts.string.type.STRING,
                'access': 'hello',
                'form': 'f',
                'length': consts.string.type.INTEGER,
            },
            {
                'unit': consts.string.type.INTEGER,
                'filename': consts.string.type.STRING,
                'access': 's',
                'form': 'hello',
                'length': consts.string.type.INTEGER,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.files.File
        EXAMPLES_VALID = [consts.string.inp.data.files.FILE]
        EXAMPLES_INVALID = ['hello']
