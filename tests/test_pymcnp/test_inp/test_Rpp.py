import pymcnp
from ... import consts
from ... import classes


class Test_Rpp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Rpp
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'xmin': 3.1, 'xmax': 3.1, 'ymin': 3.1, 'ymax': 3.1, 'zmin': 3.1, 'zmax': 3.1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'xmin': consts.ast.types.REAL,
                'xmax': consts.ast.types.REAL,
                'ymin': consts.ast.types.REAL,
                'ymax': consts.ast.types.REAL,
                'zmin': consts.ast.types.REAL,
                'zmax': consts.ast.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': None,
                'zmax': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': None,
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': None,
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': None,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': '1000',
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'xmin': None,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': None,
                'ymin': consts.string.types.REAL,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': None,
                'ymax': consts.string.types.REAL,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'xmin': consts.string.types.REAL,
                'xmax': consts.string.types.REAL,
                'ymin': consts.string.types.REAL,
                'ymax': None,
                'zmin': consts.string.types.REAL,
                'zmax': consts.string.types.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Rpp
        EXAMPLES_VALID = [
            # 3.2
            '5 rpp -2 0 -2 0 -1 1',
            '1 rpp 0 2 0 2 -1 1',
            # 3.3
            '20 rpp 0 50 -10 10 -5 5',
            '30 rpp 0 10 0 10',
            # 4.1
            '4 rpp 2 4 7.5 8.5 -2 2 $ Surface card',
            consts.string.inp.RPP,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Rpp
        EXAMPLES = [consts.string.inp.RPP]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.RPP, consts.ast.inp.RPP)]
