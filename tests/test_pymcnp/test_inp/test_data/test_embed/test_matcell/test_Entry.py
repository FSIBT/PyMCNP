import pymcnp
from ...... import consts
from ...... import classes


class Test_Entry:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.matcell.Entry
        EXAMPLES_VALID = [
            {
                'material': consts.string.type.INTEGER,
                'cell': consts.string.type.INTEGER,
            },
            {
                'material': 1,
                'cell': 1,
            },
            {
                'material': consts.ast.type.INTEGER,
                'cell': consts.ast.type.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'material': None,
                'cell': consts.string.type.INTEGER,
            },
            {
                'material': consts.string.type.INTEGER,
                'cell': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.matcell.Entry
        EXAMPLES_VALID = [consts.string.inp.data.embed.matcell.ENTRY]
        EXAMPLES_INVALID = ['hello']
