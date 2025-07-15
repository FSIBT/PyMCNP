import pymcnp
from ..... import consts
from ..... import classes


class Test_Variables:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ds_2.Variables
        EXAMPLES_VALID = [
            {
                'independent': consts.string.type.REAL,
                'dependent': consts.string.type.REAL,
            },
            {
                'independent': 0.5,
                'dependent': 0.5,
            },
            {
                'independent': consts.ast.type.REAL,
                'dependent': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'independent': None,
                'dependent': consts.string.type.REAL,
            },
            {
                'independent': consts.string.type.REAL,
                'dependent': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ds_2.Variables
        EXAMPLES_VALID = [consts.string.inp.data.ds_2.VARIABLES]
        EXAMPLES_INVALID = ['hello']
