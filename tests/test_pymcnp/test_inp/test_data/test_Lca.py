import pymcnp
from .... import consts
from .... import classes


class Test_Lca:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Lca
        EXAMPLES_VALID = [
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {'ielas': 1, 'ipreg': 1, 'iexisa': 1, 'ichoic': 1, 'jcoul': 1, 'nexite': 1, 'npidk': 1, 'noact': 1, 'icem': 1, 'ilaq': 1, 'nevtype': 1},
            {
                'ielas': consts.ast.types.INTEGER,
                'ipreg': consts.ast.types.INTEGER,
                'iexisa': consts.ast.types.INTEGER,
                'ichoic': consts.ast.types.INTEGER,
                'jcoul': consts.ast.types.INTEGER,
                'nexite': consts.ast.types.INTEGER,
                'npidk': consts.ast.types.INTEGER,
                'noact': consts.ast.types.INTEGER,
                'icem': consts.ast.types.INTEGER,
                'ilaq': consts.ast.types.INTEGER,
                'nevtype': consts.ast.types.INTEGER,
            },
            {
                'ielas': None,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': None,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': None,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': None,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': None,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': None,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': None,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': None,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': None,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': None,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'ielas': -9999,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': -9999,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': -9999,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': -9999,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': -9999,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': -9999,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': -9999,
                'icem': consts.string.types.INTEGER,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': -9999,
                'ilaq': consts.string.types.INTEGER,
                'nevtype': consts.string.types.INTEGER,
            },
            {
                'ielas': consts.string.types.INTEGER,
                'ipreg': consts.string.types.INTEGER,
                'iexisa': consts.string.types.INTEGER,
                'ichoic': consts.string.types.INTEGER,
                'jcoul': consts.string.types.INTEGER,
                'nexite': consts.string.types.INTEGER,
                'npidk': consts.string.types.INTEGER,
                'noact': consts.string.types.INTEGER,
                'icem': consts.string.types.INTEGER,
                'ilaq': -9999,
                'nevtype': consts.string.types.INTEGER,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Lca
        EXAMPLES_VALID = [consts.string.inp.data.LCA]
        EXAMPLES_INVALID = ['hello']
