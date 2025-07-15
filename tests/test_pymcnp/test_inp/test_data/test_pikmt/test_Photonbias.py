import pymcnp
from ..... import consts
from ..... import classes


class Test_Photonbias:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.pikmt.Photonbias
        EXAMPLES_VALID = [
            {
                'zaid': consts.string.type.ZAID,
                'ipiki': consts.string.type.INTEGER,
            },
            {
                'zaid': consts.string.type.ZAID,
                'ipiki': 1,
            },
            {
                'zaid': consts.ast.type.ZAID,
                'ipiki': consts.ast.type.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'zaid': None,
                'ipiki': consts.string.type.INTEGER,
            },
            {
                'zaid': consts.string.type.ZAID,
                'ipiki': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.pikmt.Photonbias
        EXAMPLES_VALID = [consts.string.inp.data.pikmt.PHOTONBIAS]
        EXAMPLES_INVALID = ['hello']
