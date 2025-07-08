import pymcnp
from ... import consts
from ... import classes


class Test_Tally_1B:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.Tally_1B
        EXAMPLES_VALID = [
            {
                'number': consts.string.type.STRING,
                'nps': consts.string.type.STRING,
                'tally_type': consts.string.type.STRING,
                'particles': consts.string.type.STRING,
                'subtallies': consts.string.type.STRING,
                'stats_desired': consts.string.type.STRING,
                'stats_observed': consts.string.type.STRING,
                'stats_passed': consts.string.type.STRING,
                'fails': consts.string.type.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'number': None,
                'nps': consts.string.type.STRING,
                'tally_type': consts.string.type.STRING,
                'particles': consts.string.type.STRING,
                'subtallies': consts.string.type.STRING,
                'stats_desired': consts.string.type.STRING,
                'stats_observed': consts.string.type.STRING,
                'stats_passed': consts.string.type.STRING,
                'fails': consts.string.type.STRING,
            },
            {
                'number': consts.string.type.STRING,
                'nps': None,
                'tally_type': consts.string.type.STRING,
                'particles': consts.string.type.STRING,
                'subtallies': consts.string.type.STRING,
                'stats_desired': consts.string.type.STRING,
                'stats_observed': consts.string.type.STRING,
                'stats_passed': consts.string.type.STRING,
                'fails': consts.string.type.STRING,
            },
            {
                'number': consts.string.type.STRING,
                'nps': consts.string.type.STRING,
                'tally_type': None,
                'particles': consts.string.type.STRING,
                'subtallies': consts.string.type.STRING,
                'stats_desired': consts.string.type.STRING,
                'stats_observed': consts.string.type.STRING,
                'stats_passed': consts.string.type.STRING,
                'fails': consts.string.type.STRING,
            },
            {
                'number': consts.string.type.STRING,
                'nps': consts.string.type.STRING,
                'tally_type': consts.string.type.STRING,
                'particles': None,
                'subtallies': consts.string.type.STRING,
                'stats_desired': consts.string.type.STRING,
                'stats_observed': consts.string.type.STRING,
                'stats_passed': consts.string.type.STRING,
                'fails': consts.string.type.STRING,
            },
            {
                'number': consts.string.type.STRING,
                'nps': consts.string.type.STRING,
                'tally_type': consts.string.type.STRING,
                'particles': consts.string.type.STRING,
                'subtallies': None,
                'stats_desired': consts.string.type.STRING,
                'stats_observed': consts.string.type.STRING,
                'stats_passed': consts.string.type.STRING,
                'fails': consts.string.type.STRING,
            },
            {
                'number': consts.string.type.STRING,
                'nps': consts.string.type.STRING,
                'tally_type': consts.string.type.STRING,
                'particles': consts.string.type.STRING,
                'subtallies': consts.string.type.STRING,
                'stats_desired': None,
                'stats_observed': consts.string.type.STRING,
                'stats_passed': consts.string.type.STRING,
                'fails': consts.string.type.STRING,
            },
            {
                'number': consts.string.type.STRING,
                'nps': consts.string.type.STRING,
                'tally_type': consts.string.type.STRING,
                'particles': consts.string.type.STRING,
                'subtallies': consts.string.type.STRING,
                'stats_desired': consts.string.type.STRING,
                'stats_observed': None,
                'stats_passed': consts.string.type.STRING,
                'fails': consts.string.type.STRING,
            },
            {
                'number': consts.string.type.STRING,
                'nps': consts.string.type.STRING,
                'tally_type': consts.string.type.STRING,
                'particles': consts.string.type.STRING,
                'subtallies': consts.string.type.STRING,
                'stats_desired': consts.string.type.STRING,
                'stats_observed': consts.string.type.STRING,
                'stats_passed': None,
                'fails': consts.string.type.STRING,
            },
            {
                'number': consts.string.type.STRING,
                'nps': consts.string.type.STRING,
                'tally_type': consts.string.type.STRING,
                'particles': consts.string.type.STRING,
                'subtallies': consts.string.type.STRING,
                'stats_desired': consts.string.type.STRING,
                'stats_observed': consts.string.type.STRING,
                'stats_passed': consts.string.type.STRING,
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
