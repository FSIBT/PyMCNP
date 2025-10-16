import pymcnp
from ... import consts
from ... import classes


class Test_Mgopt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Mgopt
        EXAMPLES_VALID = [
            {
                'mcal': 'a',
                'igm': consts.string.types.INTEGER,
                'iplt': consts.string.types.INTEGER,
                'iab': consts.string.types.INTEGER,
                'icw': consts.string.types.INTEGER,
                'fnw': consts.string.types.REAL,
                'rim': consts.string.types.REAL,
            },
            {'mcal': 'a', 'igm': 1, 'iplt': 1, 'iab': 1, 'icw': 1, 'fnw': 3.1, 'rim': 3.1},
            {
                'mcal': pymcnp.types.String('a'),
                'igm': consts.ast.types.INTEGER,
                'iplt': consts.ast.types.INTEGER,
                'iab': consts.ast.types.INTEGER,
                'icw': consts.ast.types.INTEGER,
                'fnw': consts.ast.types.REAL,
                'rim': consts.ast.types.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.types.INTEGER,
                'iplt': None,
                'iab': consts.string.types.INTEGER,
                'icw': consts.string.types.INTEGER,
                'fnw': consts.string.types.REAL,
                'rim': consts.string.types.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.types.INTEGER,
                'iplt': consts.string.types.INTEGER,
                'iab': None,
                'icw': consts.string.types.INTEGER,
                'fnw': consts.string.types.REAL,
                'rim': consts.string.types.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.types.INTEGER,
                'iplt': consts.string.types.INTEGER,
                'iab': consts.string.types.INTEGER,
                'icw': None,
                'fnw': consts.string.types.REAL,
                'rim': consts.string.types.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.types.INTEGER,
                'iplt': consts.string.types.INTEGER,
                'iab': consts.string.types.INTEGER,
                'icw': consts.string.types.INTEGER,
                'fnw': None,
                'rim': consts.string.types.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.types.INTEGER,
                'iplt': consts.string.types.INTEGER,
                'iab': consts.string.types.INTEGER,
                'icw': consts.string.types.INTEGER,
                'fnw': consts.string.types.REAL,
                'rim': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'mcal': None,
                'igm': consts.string.types.INTEGER,
                'iplt': consts.string.types.INTEGER,
                'iab': consts.string.types.INTEGER,
                'icw': consts.string.types.INTEGER,
                'fnw': consts.string.types.REAL,
                'rim': consts.string.types.REAL,
            },
            {
                'mcal': 'a',
                'igm': None,
                'iplt': consts.string.types.INTEGER,
                'iab': consts.string.types.INTEGER,
                'icw': consts.string.types.INTEGER,
                'fnw': consts.string.types.REAL,
                'rim': consts.string.types.REAL,
            },
            {
                'mcal': 'hello',
                'igm': consts.string.types.INTEGER,
                'iplt': consts.string.types.INTEGER,
                'iab': consts.string.types.INTEGER,
                'icw': consts.string.types.INTEGER,
                'fnw': consts.string.types.REAL,
                'rim': consts.string.types.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.types.INTEGER,
                'iplt': -9999,
                'iab': consts.string.types.INTEGER,
                'icw': consts.string.types.INTEGER,
                'fnw': consts.string.types.REAL,
                'rim': consts.string.types.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.types.INTEGER,
                'iplt': consts.string.types.INTEGER,
                'iab': -9999,
                'icw': consts.string.types.INTEGER,
                'fnw': consts.string.types.REAL,
                'rim': consts.string.types.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Mgopt
        EXAMPLES_VALID = [consts.string.inp.MGOPT]
        EXAMPLES_INVALID = ['hello']
