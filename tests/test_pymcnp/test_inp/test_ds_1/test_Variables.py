import pymcnp
from .... import consts
from .... import classes


class Test_Variables:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ds_1.Variables
        EXAMPLES_VALID = [
            {
                'independent': consts.string.types.REAL,
                'dependent': consts.string.types.REAL,
            },
            {
                'independent': 0.5,
                'dependent': 0.5,
            },
            {
                'independent': consts.ast.types.REAL,
                'dependent': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'independent': None,
                'dependent': consts.string.types.REAL,
            },
            {
                'independent': consts.string.types.REAL,
                'dependent': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ds_1.Variables
        EXAMPLES_VALID = [consts.string.inp.ds_1.VARIABLES]
        EXAMPLES_INVALID = ['hello']
