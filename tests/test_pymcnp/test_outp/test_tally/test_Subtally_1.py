import pymcnp
from .... import consts
from .... import classes


class Test_Subtally_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.tally.Subtally_1
        EXAMPLES_VALID = [
            {
                'surface': consts.string.type.STRING,
                'angles': consts.string.type.STRING,
                'lines': [consts.string.type.STRING],
                'total': consts.string.type.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'surface': None,
                'angles': consts.string.type.STRING,
                'lines': [consts.string.type.STRING],
                'total': consts.string.type.STRING,
            },
            {
                'surface': consts.string.type.STRING,
                'angles': None,
                'lines': [consts.string.type.STRING],
                'total': consts.string.type.STRING,
            },
            {
                'surface': consts.string.type.STRING,
                'angles': consts.string.type.STRING,
                'lines': None,
                'total': consts.string.type.STRING,
            },
            {
                'surface': consts.string.type.STRING,
                'angles': consts.string.type.STRING,
                'lines': [consts.string.type.STRING],
                'total': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.outp.tally.Subtally_1
        EXAMPLES_VALID = [consts.string.outp.tally.SUBTALLY_1]
        EXAMPLES_INVALID = [
            'hello',
        ]

    class Test_Dataframe(classes.Test_Dataframe):
        element = pymcnp.outp.tally.Subtally_1
        EXAMPLES = [
            consts.string.outp.tally.SUBTALLY_1,
        ]
