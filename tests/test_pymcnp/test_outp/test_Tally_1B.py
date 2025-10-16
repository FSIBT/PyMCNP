import pymcnp
from ... import consts
from ... import classes


class Test_Tally_1B:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.Tally_1B
        EXAMPLES_VALID = [
            {
                'number': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'tally_type': consts.string.types.STRING,
                'particles': consts.string.types.STRING,
                'subtallies': consts.string.types.STRING,
                'stats_desired': consts.string.types.STRING,
                'stats_observed': consts.string.types.STRING,
                'stats_passed': consts.string.types.STRING,
                'fails': consts.string.types.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'number': None,
                'nps': consts.string.types.STRING,
                'tally_type': consts.string.types.STRING,
                'particles': consts.string.types.STRING,
                'subtallies': consts.string.types.STRING,
                'stats_desired': consts.string.types.STRING,
                'stats_observed': consts.string.types.STRING,
                'stats_passed': consts.string.types.STRING,
                'fails': consts.string.types.STRING,
            },
            {
                'number': consts.string.types.STRING,
                'nps': None,
                'tally_type': consts.string.types.STRING,
                'particles': consts.string.types.STRING,
                'subtallies': consts.string.types.STRING,
                'stats_desired': consts.string.types.STRING,
                'stats_observed': consts.string.types.STRING,
                'stats_passed': consts.string.types.STRING,
                'fails': consts.string.types.STRING,
            },
            {
                'number': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'tally_type': None,
                'particles': consts.string.types.STRING,
                'subtallies': consts.string.types.STRING,
                'stats_desired': consts.string.types.STRING,
                'stats_observed': consts.string.types.STRING,
                'stats_passed': consts.string.types.STRING,
                'fails': consts.string.types.STRING,
            },
            {
                'number': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'tally_type': consts.string.types.STRING,
                'particles': None,
                'subtallies': consts.string.types.STRING,
                'stats_desired': consts.string.types.STRING,
                'stats_observed': consts.string.types.STRING,
                'stats_passed': consts.string.types.STRING,
                'fails': consts.string.types.STRING,
            },
            {
                'number': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'tally_type': consts.string.types.STRING,
                'particles': consts.string.types.STRING,
                'subtallies': None,
                'stats_desired': consts.string.types.STRING,
                'stats_observed': consts.string.types.STRING,
                'stats_passed': consts.string.types.STRING,
                'fails': consts.string.types.STRING,
            },
            {
                'number': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'tally_type': consts.string.types.STRING,
                'particles': consts.string.types.STRING,
                'subtallies': consts.string.types.STRING,
                'stats_desired': None,
                'stats_observed': consts.string.types.STRING,
                'stats_passed': consts.string.types.STRING,
                'fails': consts.string.types.STRING,
            },
            {
                'number': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'tally_type': consts.string.types.STRING,
                'particles': consts.string.types.STRING,
                'subtallies': consts.string.types.STRING,
                'stats_desired': consts.string.types.STRING,
                'stats_observed': None,
                'stats_passed': consts.string.types.STRING,
                'fails': consts.string.types.STRING,
            },
            {
                'number': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'tally_type': consts.string.types.STRING,
                'particles': consts.string.types.STRING,
                'subtallies': consts.string.types.STRING,
                'stats_desired': consts.string.types.STRING,
                'stats_observed': consts.string.types.STRING,
                'stats_passed': None,
                'fails': consts.string.types.STRING,
            },
            {
                'number': consts.string.types.STRING,
                'nps': consts.string.types.STRING,
                'tally_type': consts.string.types.STRING,
                'particles': consts.string.types.STRING,
                'subtallies': consts.string.types.STRING,
                'stats_desired': consts.string.types.STRING,
                'stats_observed': consts.string.types.STRING,
                'stats_passed': consts.string.types.STRING,
                'fails': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.outp.Tally_1B
        EXAMPLES_VALID = [consts.string.outp.TALLY_1B]
        EXAMPLES_INVALID = [
            'hello',
        ]

    class Test_Dataframe(classes.Test_Dataframe):
        element = pymcnp.outp.Tally_1B
        EXAMPLES = [
            consts.string.outp.TALLY_1B,
        ]
