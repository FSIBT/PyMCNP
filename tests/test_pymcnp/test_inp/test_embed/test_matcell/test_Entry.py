import pymcnp
from ..... import consts
from ..... import classes


class Test_Entry:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embed.matcell.Entry
        EXAMPLES_VALID = [
            {
                'material': consts.string.types.INTEGER,
                'cell': consts.string.types.INTEGER,
            },
            {
                'material': 1,
                'cell': 1,
            },
            {
                'material': consts.ast.types.INTEGER,
                'cell': consts.ast.types.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'material': None,
                'cell': consts.string.types.INTEGER,
            },
            {
                'material': consts.string.types.INTEGER,
                'cell': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embed.matcell.Entry
        EXAMPLES_VALID = [consts.string.inp.embed.matcell.ENTRY]
        EXAMPLES_INVALID = ['hello']
