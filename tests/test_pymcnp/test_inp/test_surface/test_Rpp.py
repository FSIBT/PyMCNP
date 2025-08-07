import pymcnp
from .... import consts
from .... import classes


class Test_Rpp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES_VALID = [
            {
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {'xmin': 3.1, 'xmax': 3.1, 'ymin': 3.1, 'ymax': 3.1, 'zmin': 3.1, 'zmax': 3.1},
            {'xmin': consts.ast.types.REAL, 'xmax': consts.ast.types.REAL, 'ymin': consts.ast.types.REAL, 'ymax': consts.ast.types.REAL, 'zmin': consts.ast.types.REAL, 'zmax': consts.ast.types.REAL},
            {'xmin': consts.string.types.REAL, 'xmax': consts.string.types.REAL, 'ymin': consts.string.types.REAL, 'ymax': consts.string.types.REAL, 'zmin': None, 'zmax': consts.string.types.REAL},
            {'xmin': consts.string.types.REAL, 'xmax': consts.string.types.REAL, 'ymin': consts.string.types.REAL, 'ymax': consts.string.types.REAL, 'zmin': consts.string.types.REAL, 'zmax': None},
        ]
        EXAMPLES_INVALID = [
            {'xmin': None, 'xmax': consts.string.types.REAL, 'ymin': consts.string.types.REAL, 'ymax': consts.string.types.REAL, 'zmin': consts.string.types.REAL, 'zmax': consts.string.types.REAL},
            {'xmin': consts.string.types.REAL, 'xmax': None, 'ymin': consts.string.types.REAL, 'ymax': consts.string.types.REAL, 'zmin': consts.string.types.REAL, 'zmax': consts.string.types.REAL},
            {'xmin': consts.string.types.REAL, 'xmax': consts.string.types.REAL, 'ymin': None, 'ymax': consts.string.types.REAL, 'zmin': consts.string.types.REAL, 'zmax': consts.string.types.REAL},
            {'xmin': consts.string.types.REAL, 'xmax': consts.string.types.REAL, 'ymin': consts.string.types.REAL, 'ymax': None, 'zmin': consts.string.types.REAL, 'zmax': consts.string.types.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES_VALID = [consts.string.inp.surface.RPP]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES = [consts.string.inp.surface.RPP]
