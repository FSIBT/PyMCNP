import pymcnp
from ... import _utils


class Test_Mgopt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mgopt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.MgoptBuilder
        EXAMPLES_VALID = [
            {
                'mcal': 'a',
                'igm': _utils.string.type.INTEGER,
                'iplt': _utils.string.type.INTEGER,
                'iab': _utils.string.type.INTEGER,
                'icw': _utils.string.type.INTEGER,
                'fnw': _utils.string.type.REAL,
                'rim': _utils.string.type.REAL,
            },
            {'mcal': 'a', 'igm': 1, 'iplt': 1, 'iab': 1, 'icw': 1, 'fnw': 3.1, 'rim': 3.1},
            {
                'mcal': pymcnp.utils.types.String('a'),
                'igm': _utils.ast.type.INTEGER,
                'iplt': _utils.ast.type.INTEGER,
                'iab': _utils.ast.type.INTEGER,
                'icw': _utils.ast.type.INTEGER,
                'fnw': _utils.ast.type.REAL,
                'rim': _utils.ast.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': _utils.string.type.INTEGER,
                'iplt': None,
                'iab': _utils.string.type.INTEGER,
                'icw': _utils.string.type.INTEGER,
                'fnw': _utils.string.type.REAL,
                'rim': _utils.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': _utils.string.type.INTEGER,
                'iplt': _utils.string.type.INTEGER,
                'iab': None,
                'icw': _utils.string.type.INTEGER,
                'fnw': _utils.string.type.REAL,
                'rim': _utils.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': _utils.string.type.INTEGER,
                'iplt': _utils.string.type.INTEGER,
                'iab': _utils.string.type.INTEGER,
                'icw': None,
                'fnw': _utils.string.type.REAL,
                'rim': _utils.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': _utils.string.type.INTEGER,
                'iplt': _utils.string.type.INTEGER,
                'iab': _utils.string.type.INTEGER,
                'icw': _utils.string.type.INTEGER,
                'fnw': None,
                'rim': _utils.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': _utils.string.type.INTEGER,
                'iplt': _utils.string.type.INTEGER,
                'iab': _utils.string.type.INTEGER,
                'icw': _utils.string.type.INTEGER,
                'fnw': _utils.string.type.REAL,
                'rim': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'mcal': None,
                'igm': _utils.string.type.INTEGER,
                'iplt': _utils.string.type.INTEGER,
                'iab': _utils.string.type.INTEGER,
                'icw': _utils.string.type.INTEGER,
                'fnw': _utils.string.type.REAL,
                'rim': _utils.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': None,
                'iplt': _utils.string.type.INTEGER,
                'iab': _utils.string.type.INTEGER,
                'icw': _utils.string.type.INTEGER,
                'fnw': _utils.string.type.REAL,
                'rim': _utils.string.type.REAL,
            },
            {
                'mcal': 'hello',
                'igm': _utils.string.type.INTEGER,
                'iplt': _utils.string.type.INTEGER,
                'iab': _utils.string.type.INTEGER,
                'icw': _utils.string.type.INTEGER,
                'fnw': _utils.string.type.REAL,
                'rim': _utils.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': _utils.string.type.INTEGER,
                'iplt': -9999,
                'iab': _utils.string.type.INTEGER,
                'icw': _utils.string.type.INTEGER,
                'fnw': _utils.string.type.REAL,
                'rim': _utils.string.type.REAL,
            },
            {
                'mcal': 'a',
                'igm': _utils.string.type.INTEGER,
                'iplt': _utils.string.type.INTEGER,
                'iab': -9999,
                'icw': _utils.string.type.INTEGER,
                'fnw': _utils.string.type.REAL,
                'rim': _utils.string.type.REAL,
            },
        ]
