import pymcnp
from .... import consts
from .... import classes


class Test_Photonbias:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.pikmt.Photonbias
        EXAMPLES_VALID = [
            {
                'zaid': consts.string.types.ZAID,
                'ipiki': consts.string.types.INTEGER,
            },
            {
                'zaid': consts.string.types.ZAID,
                'ipiki': 1,
            },
            {
                'zaid': consts.ast.types.ZAID,
                'ipiki': consts.ast.types.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'zaid': None,
                'ipiki': consts.string.types.INTEGER,
            },
            {
                'zaid': consts.string.types.ZAID,
                'ipiki': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.pikmt.Photonbias
        EXAMPLES_VALID = [consts.string.inp.pikmt.PHOTONBIAS]
        EXAMPLES_INVALID = ['hello']
