import pymcnp
from .... import consts
from .... import classes


class Test_Variables:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ds_2.Variables
        EXAMPLES_VALID = [
            {
                'independent': consts.string.types.DISTRIBUTION,
                'dependent': consts.string.types.REAL,
            },
            {
                'independent': 3.1,
                'dependent': 0.5,
            },
            {
                'independent': consts.ast.types.DISTRIBUTION,
                'dependent': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'independent': None,
                'dependent': consts.string.types.REAL,
            },
            {
                'independent': consts.string.types.DISTRIBUTION,
                'dependent': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ds_2.Variables
        EXAMPLES_VALID = [consts.string.inp.ds_2.VARIABLES]
        EXAMPLES_INVALID = ['hello']
