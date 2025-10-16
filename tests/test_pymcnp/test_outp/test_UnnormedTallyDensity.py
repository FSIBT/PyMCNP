import pymcnp
from ... import consts
from ... import classes


class Test_UnnormedTallyDensity:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.UnnormedTallyDensity
        EXAMPLES_VALID = [
            {
                'tally': consts.string.types.STRING,
                'mean': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'chart': consts.string.types.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'tally': None,
                'mean': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'chart': consts.string.types.STRING,
            },
            {
                'tally': consts.string.types.STRING,
                'mean': None,
                'nps': consts.string.types.STRING,
                'chart': consts.string.types.STRING,
            },
            {
                'tally': consts.string.types.STRING,
                'mean': consts.string.types.STRING,
                'nps': None,
                'chart': consts.string.types.STRING,
            },
            {
                'tally': consts.string.types.STRING,
                'mean': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'chart': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.outp.UnnormedTallyDensity
        EXAMPLES_VALID = [consts.string.outp.UNNORMED_TALLY_DENSITY]
        EXAMPLES_INVALID = [
            'hello',
        ]
