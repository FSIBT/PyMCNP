import pymcnp
from ... import _utils


class Test_Lcc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Lcc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.LccBuilder
        EXAMPLES_VALID = [
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': _utils.string.type.INTEGER,
                'nosurfincl': _utils.string.type.INTEGER,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': _utils.string.type.REAL,
            },
            {'stincl': 3.1, 'v0incl': 3.1, 'xfoisaincl': 3.1, 'npaulincl': 1, 'nosurfincl': 1, 'ecutincl': 3.1, 'ebankincl': 3.1, 'ebankabia': 3.1},
            {
                'stincl': _utils.ast.type.REAL,
                'v0incl': _utils.ast.type.REAL,
                'xfoisaincl': _utils.ast.type.REAL,
                'npaulincl': _utils.ast.type.INTEGER,
                'nosurfincl': _utils.ast.type.INTEGER,
                'ecutincl': _utils.ast.type.REAL,
                'ebankincl': _utils.ast.type.REAL,
                'ebankabia': _utils.ast.type.REAL,
            },
            {
                'stincl': None,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': _utils.string.type.INTEGER,
                'nosurfincl': _utils.string.type.INTEGER,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': _utils.string.type.REAL,
            },
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': None,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': _utils.string.type.INTEGER,
                'nosurfincl': _utils.string.type.INTEGER,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': _utils.string.type.REAL,
            },
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': None,
                'npaulincl': _utils.string.type.INTEGER,
                'nosurfincl': _utils.string.type.INTEGER,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': _utils.string.type.REAL,
            },
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': None,
                'nosurfincl': _utils.string.type.INTEGER,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': _utils.string.type.REAL,
            },
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': _utils.string.type.INTEGER,
                'nosurfincl': None,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': _utils.string.type.REAL,
            },
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': _utils.string.type.INTEGER,
                'nosurfincl': _utils.string.type.INTEGER,
                'ecutincl': None,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': _utils.string.type.REAL,
            },
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': _utils.string.type.INTEGER,
                'nosurfincl': _utils.string.type.INTEGER,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': None,
                'ebankabia': _utils.string.type.REAL,
            },
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': _utils.string.type.INTEGER,
                'nosurfincl': _utils.string.type.INTEGER,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': -9999,
                'nosurfincl': _utils.string.type.INTEGER,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': _utils.string.type.REAL,
            },
            {
                'stincl': _utils.string.type.REAL,
                'v0incl': _utils.string.type.REAL,
                'xfoisaincl': _utils.string.type.REAL,
                'npaulincl': _utils.string.type.INTEGER,
                'nosurfincl': -9999,
                'ecutincl': _utils.string.type.REAL,
                'ebankincl': _utils.string.type.REAL,
                'ebankabia': _utils.string.type.REAL,
            },
        ]
