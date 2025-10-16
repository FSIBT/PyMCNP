import pymcnp
from ..... import consts
from ..... import classes


class Test_Line:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.tally.subtally.Line
        EXAMPLES_VALID = [
            {
                'bucket': consts.string.types.STRING,
                'count': consts.string.types.STRING,
                'error': consts.string.types.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'bucket': None,
                'count': consts.string.types.STRING,
                'error': consts.string.types.STRING,
            },
            {
                'bucket': consts.string.types.STRING,
                'count': None,
                'error': consts.string.types.STRING,
            },
            {
                'bucket': consts.string.types.STRING,
                'count': consts.string.types.STRING,
                'error': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.outp.tally.subtally.Line
        EXAMPLES_VALID = [consts.string.outp.tally.subtally.LINE]
        EXAMPLES_INVALID = [
            'hello',
        ]

    class Test_Dataframe(classes.Test_Dataframe):
        element = pymcnp.outp.tally.subtally.Line
        EXAMPLES = [
            consts.string.outp.tally.subtally.LINE,
        ]
