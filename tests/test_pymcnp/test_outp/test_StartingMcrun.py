import pymcnp
from ... import consts
from ... import classes


class Test_StartingMcrun:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.StartingMcrun
        EXAMPLES_VALID = [
            {
                'cp0': consts.string.type.STRING,
                'title': consts.string.type.STRING,
                'data': consts.string.type.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'cp0': None,
                'title': consts.string.type.STRING,
                'data': consts.string.type.STRING,
            },
            {
                'cp0': consts.string.type.STRING,
                'title': None,
                'data': consts.string.type.STRING,
            },
            {
                'cp0': consts.string.type.STRING,
                'title': consts.string.type.STRING,
                'data': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.outp.StartingMcrun
        EXAMPLES_VALID = [consts.string.outp.STARTING_MCRUN]
        EXAMPLES_INVALID = [
            'hello',
        ]
