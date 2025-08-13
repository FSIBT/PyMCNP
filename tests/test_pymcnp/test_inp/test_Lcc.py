import pymcnp
from ... import consts
from ... import classes


class Test_Lcc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Lcc
        EXAMPLES_VALID = [
            {
                'stincl': consts.string.types.REAL,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': consts.string.types.INTEGER,
                'nosurfincl': consts.string.types.INTEGER,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': consts.string.types.REAL,
            },
            {'stincl': 3.1, 'v0incl': 3.1, 'xfoisaincl': 3.1, 'npaulincl': 1, 'nosurfincl': 1, 'ecutincl': 3.1, 'ebankincl': 3.1, 'ebankabia': 3.1},
            {
                'stincl': consts.ast.types.REAL,
                'v0incl': consts.ast.types.REAL,
                'xfoisaincl': consts.ast.types.REAL,
                'npaulincl': consts.ast.types.INTEGER,
                'nosurfincl': consts.ast.types.INTEGER,
                'ecutincl': consts.ast.types.REAL,
                'ebankincl': consts.ast.types.REAL,
                'ebankabia': consts.ast.types.REAL,
            },
            {
                'stincl': None,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': consts.string.types.INTEGER,
                'nosurfincl': consts.string.types.INTEGER,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': consts.string.types.REAL,
            },
            {
                'stincl': consts.string.types.REAL,
                'v0incl': None,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': consts.string.types.INTEGER,
                'nosurfincl': consts.string.types.INTEGER,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': consts.string.types.REAL,
            },
            {
                'stincl': consts.string.types.REAL,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': None,
                'npaulincl': consts.string.types.INTEGER,
                'nosurfincl': consts.string.types.INTEGER,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': consts.string.types.REAL,
            },
            {
                'stincl': consts.string.types.REAL,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': None,
                'nosurfincl': consts.string.types.INTEGER,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': consts.string.types.REAL,
            },
            {
                'stincl': consts.string.types.REAL,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': consts.string.types.INTEGER,
                'nosurfincl': None,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': consts.string.types.REAL,
            },
            {
                'stincl': consts.string.types.REAL,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': consts.string.types.INTEGER,
                'nosurfincl': consts.string.types.INTEGER,
                'ecutincl': None,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': consts.string.types.REAL,
            },
            {
                'stincl': consts.string.types.REAL,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': consts.string.types.INTEGER,
                'nosurfincl': consts.string.types.INTEGER,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': None,
                'ebankabia': consts.string.types.REAL,
            },
            {
                'stincl': consts.string.types.REAL,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': consts.string.types.INTEGER,
                'nosurfincl': consts.string.types.INTEGER,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'stincl': consts.string.types.REAL,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': -9999,
                'nosurfincl': consts.string.types.INTEGER,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': consts.string.types.REAL,
            },
            {
                'stincl': consts.string.types.REAL,
                'v0incl': consts.string.types.REAL,
                'xfoisaincl': consts.string.types.REAL,
                'npaulincl': consts.string.types.INTEGER,
                'nosurfincl': -9999,
                'ecutincl': consts.string.types.REAL,
                'ebankincl': consts.string.types.REAL,
                'ebankabia': consts.string.types.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Lcc
        EXAMPLES_VALID = [consts.string.inp.LCC]
        EXAMPLES_INVALID = ['hello']
