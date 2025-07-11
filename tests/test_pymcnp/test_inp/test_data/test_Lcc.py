import pymcnp
from .... import consts
from .... import classes


class Test_Lcc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Lcc
        EXAMPLES_VALID = [
            {
                'stincl': consts.string.type.REAL,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': consts.string.type.INTEGER,
                'nosurfincl': consts.string.type.INTEGER,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': consts.string.type.REAL,
            },
            {'stincl': 3.1, 'v0incl': 3.1, 'xfoisaincl': 3.1, 'npaulincl': 1, 'nosurfincl': 1, 'ecutincl': 3.1, 'ebankincl': 3.1, 'ebankabia': 3.1},
            {
                'stincl': consts.ast.type.REAL,
                'v0incl': consts.ast.type.REAL,
                'xfoisaincl': consts.ast.type.REAL,
                'npaulincl': consts.ast.type.INTEGER,
                'nosurfincl': consts.ast.type.INTEGER,
                'ecutincl': consts.ast.type.REAL,
                'ebankincl': consts.ast.type.REAL,
                'ebankabia': consts.ast.type.REAL,
            },
            {
                'stincl': None,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': consts.string.type.INTEGER,
                'nosurfincl': consts.string.type.INTEGER,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': consts.string.type.REAL,
            },
            {
                'stincl': consts.string.type.REAL,
                'v0incl': None,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': consts.string.type.INTEGER,
                'nosurfincl': consts.string.type.INTEGER,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': consts.string.type.REAL,
            },
            {
                'stincl': consts.string.type.REAL,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': None,
                'npaulincl': consts.string.type.INTEGER,
                'nosurfincl': consts.string.type.INTEGER,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': consts.string.type.REAL,
            },
            {
                'stincl': consts.string.type.REAL,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': None,
                'nosurfincl': consts.string.type.INTEGER,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': consts.string.type.REAL,
            },
            {
                'stincl': consts.string.type.REAL,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': consts.string.type.INTEGER,
                'nosurfincl': None,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': consts.string.type.REAL,
            },
            {
                'stincl': consts.string.type.REAL,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': consts.string.type.INTEGER,
                'nosurfincl': consts.string.type.INTEGER,
                'ecutincl': None,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': consts.string.type.REAL,
            },
            {
                'stincl': consts.string.type.REAL,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': consts.string.type.INTEGER,
                'nosurfincl': consts.string.type.INTEGER,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': None,
                'ebankabia': consts.string.type.REAL,
            },
            {
                'stincl': consts.string.type.REAL,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': consts.string.type.INTEGER,
                'nosurfincl': consts.string.type.INTEGER,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'stincl': consts.string.type.REAL,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': -9999,
                'nosurfincl': consts.string.type.INTEGER,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': consts.string.type.REAL,
            },
            {
                'stincl': consts.string.type.REAL,
                'v0incl': consts.string.type.REAL,
                'xfoisaincl': consts.string.type.REAL,
                'npaulincl': consts.string.type.INTEGER,
                'nosurfincl': -9999,
                'ecutincl': consts.string.type.REAL,
                'ebankincl': consts.string.type.REAL,
                'ebankabia': consts.string.type.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Lcc
        EXAMPLES_VALID = [consts.string.inp.data.LCC]
        EXAMPLES_INVALID = ['hello']
