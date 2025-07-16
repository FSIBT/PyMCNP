import pymcnp
from ... import consts
from ... import classes


class Test_Header:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.Header
        EXAMPLES_VALID = [
            {
                'name': consts.string.types.STRING,
                'logo': consts.string.types.STRING,
                'box': consts.string.types.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'name': None,
                'logo': consts.string.types.STRING,
                'box': consts.string.types.STRING,
            },
            {
                'name': consts.string.types.STRING,
                'logo': None,
                'box': consts.string.types.STRING,
            },
            {'name': consts.string.types.STRING, 'logo': consts.string.types.STRING, 'box': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.outp.Header
        EXAMPLES_VALID = [consts.string.outp.HEADER]
        EXAMPLES_INVALID = [
            'hello',
        ]
