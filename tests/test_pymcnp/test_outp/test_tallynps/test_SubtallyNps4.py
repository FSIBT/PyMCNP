import pymcnp
from .... import consts
from .... import classes


class Test_SubtallyNps1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.outp.tallynps.SubtallyNps4
        EXAMPLES_VALID = [
            {
                'cell': consts.string.type.STRING,
                'energies': consts.string.type.STRING,
                'total': consts.string.type.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'cell': None,
                'energies': consts.string.type.STRING,
                'total': consts.string.type.STRING,
            },
            {
                'cell': consts.string.type.STRING,
                'energies': None,
                'total': consts.string.type.STRING,
            },
            {
                'cell': consts.string.type.STRING,
                'energies': consts.string.type.STRING,
                'total': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.outp.tallynps.SubtallyNps4
        EXAMPLES_VALID = [consts.string.outp.tallynps.SUBTALLY_NPS_4]
        EXAMPLES_INVALID = [
            'hello',
        ]
