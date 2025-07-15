import pymcnp
from ..... import consts
from ..... import classes


class Test_Diagnostic:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dd.Diagnostic
        EXAMPLES_VALID = [
            {
                'playing_setting': consts.string.type.REAL,
                'printing_setting': consts.string.type.REAL,
            },
            {
                'playing_setting': 0.5,
                'printing_setting': 0.5,
            },
            {
                'playing_setting': consts.ast.type.REAL,
                'printing_setting': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'playing_setting': None,
                'printing_setting': consts.string.type.REAL,
            },
            {
                'playing_setting': consts.string.type.REAL,
                'printing_setting': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dd.Diagnostic
        EXAMPLES_VALID = [consts.string.inp.data.dd.DIAGNOSTIC]
        EXAMPLES_INVALID = ['hello']
