import pymcnp
from ... import consts
from ... import classes


class Test_Header:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.Header
        EXAMPLES_VALID = [
            {
                'code': consts.ast.types.STRING,
                'version': consts.ast.types.STRING,
                'code_date': consts.ast.types.STRING,
                'run_datetime': consts.ast.types.STRING,
                'title': consts.ast.types.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            }
        ]
        EXAMPLES_INVALID = [
            {
                'code': None,
                'version': consts.ast.types.STRING,
                'code_date': consts.ast.types.STRING,
                'run_datetime': consts.ast.types.STRING,
                'title': consts.ast.types.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.types.STRING,
                'version': None,
                'code_date': consts.ast.types.STRING,
                'run_datetime': consts.ast.types.STRING,
                'title': consts.ast.types.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.types.STRING,
                'version': consts.ast.types.STRING,
                'code_date': None,
                'run_datetime': consts.ast.types.STRING,
                'title': consts.ast.types.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.types.STRING,
                'version': consts.ast.types.STRING,
                'code_date': consts.ast.types.STRING,
                'run_datetime': None,
                'title': consts.ast.types.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.types.STRING,
                'version': consts.ast.types.STRING,
                'code_date': consts.ast.types.STRING,
                'run_datetime': consts.ast.types.STRING,
                'title': None,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.types.STRING,
                'version': consts.ast.types.STRING,
                'code_date': consts.ast.types.STRING,
                'run_datetime': consts.ast.types.STRING,
                'title': consts.ast.types.STRING,
                'v_line': None,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.types.STRING,
                'version': consts.ast.types.STRING,
                'code_date': consts.ast.types.STRING,
                'run_datetime': consts.ast.types.STRING,
                'title': consts.ast.types.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': None,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.types.STRING,
                'version': consts.ast.types.STRING,
                'code_date': consts.ast.types.STRING,
                'run_datetime': consts.ast.types.STRING,
                'title': consts.ast.types.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.Header
        EXAMPLES_VALID = [consts.string.ptrac.HEADER]
        EXAMPLES_INVALID = ['hello']
