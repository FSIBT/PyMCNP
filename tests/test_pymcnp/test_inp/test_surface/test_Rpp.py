import pymcnp
from .... import consts
from .... import classes


class Test_Rpp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES_VALID = [
            {
                'xmin': consts.string.type.REAL,
                'xmax': consts.string.type.REAL,
                'ymin': consts.string.type.REAL,
                'ymax': consts.string.type.REAL,
                'zmin': consts.string.type.REAL,
                'zmax': consts.string.type.REAL,
            },
            {'xmin': 3.1, 'xmax': 3.1, 'ymin': 3.1, 'ymax': 3.1, 'zmin': 3.1, 'zmax': 3.1},
            {'xmin': consts.ast.type.REAL, 'xmax': consts.ast.type.REAL, 'ymin': consts.ast.type.REAL, 'ymax': consts.ast.type.REAL, 'zmin': consts.ast.type.REAL, 'zmax': consts.ast.type.REAL},
            {'xmin': consts.string.type.REAL, 'xmax': consts.string.type.REAL, 'ymin': consts.string.type.REAL, 'ymax': consts.string.type.REAL, 'zmin': None, 'zmax': consts.string.type.REAL},
            {'xmin': consts.string.type.REAL, 'xmax': consts.string.type.REAL, 'ymin': consts.string.type.REAL, 'ymax': consts.string.type.REAL, 'zmin': consts.string.type.REAL, 'zmax': None},
        ]
        EXAMPLES_INVALID = [
            {'xmin': None, 'xmax': consts.string.type.REAL, 'ymin': consts.string.type.REAL, 'ymax': consts.string.type.REAL, 'zmin': consts.string.type.REAL, 'zmax': consts.string.type.REAL},
            {'xmin': consts.string.type.REAL, 'xmax': None, 'ymin': consts.string.type.REAL, 'ymax': consts.string.type.REAL, 'zmin': consts.string.type.REAL, 'zmax': consts.string.type.REAL},
            {'xmin': consts.string.type.REAL, 'xmax': consts.string.type.REAL, 'ymin': None, 'ymax': consts.string.type.REAL, 'zmin': consts.string.type.REAL, 'zmax': consts.string.type.REAL},
            {'xmin': consts.string.type.REAL, 'xmax': consts.string.type.REAL, 'ymin': consts.string.type.REAL, 'ymax': None, 'zmin': consts.string.type.REAL, 'zmax': consts.string.type.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES_VALID = [consts.string.inp.surface.RPP]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES = [consts.string.inp.surface.RPP]
