import pymcnp
from .... import consts
from .... import classes


class Test_SubtallyNps1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.tallynps.SubtallyNps1
        EXAMPLES_VALID = [
            {
                'surface': consts.string.type.STRING,
                'angles': consts.string.type.STRING,
                'tallies': consts.string.type.STRING,
                'total': consts.string.type.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'surface': None,
                'angles': consts.string.type.STRING,
                'tallies': consts.string.type.STRING,
                'total': consts.string.type.STRING,
            },
            {
                'surface': consts.string.type.STRING,
                'angles': None,
                'tallies': consts.string.type.STRING,
                'total': consts.string.type.STRING,
            },
            {
                'surface': consts.string.type.STRING,
                'angles': consts.string.type.STRING,
                'tallies': None,
                'total': consts.string.type.STRING,
            },
            {
                'surface': consts.string.type.STRING,
                'angles': consts.string.type.STRING,
                'tallies': consts.string.type.STRING,
                'total': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.outp.tallynps.SubtallyNps1
        EXAMPLES_VALID = [consts.string.outp.tallynps.SUBTALLY_NPS_1]
        EXAMPLES_INVALID = [
            'hello',
        ]
