import pymcnp
from .... import consts
from .... import classes


class Test_Diagnostic:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dd.Diagnostic
        EXAMPLES_VALID = [
            {
                'playing_setting': consts.string.types.REAL,
                'printing_setting': consts.string.types.REAL,
            },
            {
                'playing_setting': 0.5,
                'printing_setting': 0.5,
            },
            {
                'playing_setting': consts.ast.types.REAL,
                'printing_setting': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'playing_setting': None,
                'printing_setting': consts.string.types.REAL,
            },
            {
                'playing_setting': consts.string.types.REAL,
                'printing_setting': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dd.Diagnostic
        EXAMPLES_VALID = [consts.string.inp.dd.DIAGNOSTIC]
        EXAMPLES_INVALID = ['hello']
