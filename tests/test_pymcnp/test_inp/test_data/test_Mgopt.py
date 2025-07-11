import pymcnp
from .... import consts
from .... import classes


class Test_Mgopt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Mgopt
        EXAMPLES_VALID = [
            {
                'mcal': 'a',
                'igm': consts.string.type.INTEGER,
                'iplt': consts.string.type.INTEGER,
                'iab': consts.string.type.INTEGER,
                'icw': consts.string.type.INTEGER,
                'fnw': consts.string.type.REAL,
                'rim': consts.string.type.REAL,
            },
            {'mcal': 'a', 'igm': 1, 'iplt': 1, 'iab': 1, 'icw': 1, 'fnw': 3.1, 'rim': 3.1},
            {
                'mcal': pymcnp.types.String('a'),
                'igm': consts.ast.type.INTEGER,
                'iplt': consts.ast.type.INTEGER,
                'iab': consts.ast.type.INTEGER,
                'icw': consts.ast.type.INTEGER,
                'fnw': consts.ast.type.REAL,
                'rim': consts.ast.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.type.INTEGER,
                'iplt': None,
                'iab': consts.string.type.INTEGER,
                'icw': consts.string.type.INTEGER,
                'fnw': consts.string.type.REAL,
                'rim': consts.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.type.INTEGER,
                'iplt': consts.string.type.INTEGER,
                'iab': None,
                'icw': consts.string.type.INTEGER,
                'fnw': consts.string.type.REAL,
                'rim': consts.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.type.INTEGER,
                'iplt': consts.string.type.INTEGER,
                'iab': consts.string.type.INTEGER,
                'icw': None,
                'fnw': consts.string.type.REAL,
                'rim': consts.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.type.INTEGER,
                'iplt': consts.string.type.INTEGER,
                'iab': consts.string.type.INTEGER,
                'icw': consts.string.type.INTEGER,
                'fnw': None,
                'rim': consts.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.type.INTEGER,
                'iplt': consts.string.type.INTEGER,
                'iab': consts.string.type.INTEGER,
                'icw': consts.string.type.INTEGER,
                'fnw': consts.string.type.REAL,
                'rim': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'mcal': None,
                'igm': consts.string.type.INTEGER,
                'iplt': consts.string.type.INTEGER,
                'iab': consts.string.type.INTEGER,
                'icw': consts.string.type.INTEGER,
                'fnw': consts.string.type.REAL,
                'rim': consts.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': None,
                'iplt': consts.string.type.INTEGER,
                'iab': consts.string.type.INTEGER,
                'icw': consts.string.type.INTEGER,
                'fnw': consts.string.type.REAL,
                'rim': consts.string.type.REAL,
            },
            {
                'mcal': 'hello',
                'igm': consts.string.type.INTEGER,
                'iplt': consts.string.type.INTEGER,
                'iab': consts.string.type.INTEGER,
                'icw': consts.string.type.INTEGER,
                'fnw': consts.string.type.REAL,
                'rim': consts.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.type.INTEGER,
                'iplt': -9999,
                'iab': consts.string.type.INTEGER,
                'icw': consts.string.type.INTEGER,
                'fnw': consts.string.type.REAL,
                'rim': consts.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': consts.string.type.INTEGER,
                'iplt': consts.string.type.INTEGER,
                'iab': -9999,
                'icw': consts.string.type.INTEGER,
                'fnw': consts.string.type.REAL,
                'rim': consts.string.type.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Mgopt
        EXAMPLES_VALID = [consts.string.inp.data.MGOPT]
        EXAMPLES_INVALID = ['hello']
