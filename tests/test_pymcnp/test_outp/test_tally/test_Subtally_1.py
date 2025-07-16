import pymcnp
from .... import consts
from .... import classes


class Test_Subtally_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.tally.Subtally_1
        EXAMPLES_VALID = [
            {
                'surface': consts.string.types.STRING,
                'angle_from': consts.string.types.STRING,
                'angle_to': consts.string.types.STRING,
                'lines': [consts.string.types.STRING],
                'total': consts.string.types.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'surface': None,
                'angle_from': consts.string.types.STRING,
                'angle_to': consts.string.types.STRING,
                'lines': [consts.string.types.STRING],
                'total': consts.string.types.STRING,
            },
            {
                'surface': consts.string.types.STRING,
                'angle_from': None,
                'angle_to': consts.string.types.STRING,
                'lines': [consts.string.types.STRING],
                'total': consts.string.types.STRING,
            },
            {
                'surface': consts.string.types.STRING,
                'angle_from': consts.string.types.STRING,
                'angle_to': None,
                'lines': [consts.string.types.STRING],
                'total': consts.string.types.STRING,
            },
            {
                'surface': consts.string.types.STRING,
                'angle_from': consts.string.types.STRING,
                'angle_to': consts.string.types.STRING,
                'lines': None,
                'total': consts.string.types.STRING,
            },
            {
                'surface': consts.string.types.STRING,
                'angle_from': consts.string.types.STRING,
                'angle_to': consts.string.types.STRING,
                'lines': [consts.string.types.STRING],
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
