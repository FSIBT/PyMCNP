import pymcnp
from ... import consts
from ... import classes


class Test_NeutronActivity:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.NeutronActivity
        EXAMPLES_VALID = [
            {
                'cells': consts.string.types.STRING,
                'total_tracks': consts.string.types.STRING,
                'total_population': consts.string.types.STRING,
                'total_collisions': consts.string.types.STRING,
                'total_weighted_collisions': consts.string.types.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'cells': None,
                'total_tracks': consts.string.types.STRING,
                'total_population': consts.string.types.STRING,
                'total_collisions': consts.string.types.STRING,
                'total_weighted_collisions': consts.string.types.STRING,
            },
            {
                'cells': consts.string.types.STRING,
                'total_tracks': None,
                'total_population': consts.string.types.STRING,
                'total_collisions': consts.string.types.STRING,
                'total_weighted_collisions': consts.string.types.STRING,
            },
            {
                'cells': consts.string.types.STRING,
                'total_tracks': consts.string.types.STRING,
                'total_population': None,
                'total_collisions': consts.string.types.STRING,
                'total_weighted_collisions': consts.string.types.STRING,
            },
            {
                'cells': consts.string.types.STRING,
                'total_tracks': consts.string.types.STRING,
                'total_population': consts.string.types.STRING,
                'total_collisions': None,
                'total_weighted_collisions': consts.string.types.STRING,
            },
            {
                'cells': consts.string.types.STRING,
                'total_tracks': consts.string.types.STRING,
                'total_population': consts.string.types.STRING,
                'total_collisions': consts.string.types.STRING,
                'total_weighted_collisions': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.outp.NeutronActivity
        EXAMPLES_VALID = [consts.string.outp.NEUTRON_ACTIVITY]
        EXAMPLES_INVALID = [
            'hello',
        ]
