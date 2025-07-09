import pymcnp
from ... import consts
from ... import classes


class Test_Header:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.Header
        EXAMPLES_VALID = [
            {
                'code': consts.ast.type.STRING,
                'version': consts.ast.type.STRING,
                'code_date': consts.ast.type.STRING,
                'run_datetime': consts.ast.type.STRING,
                'title': consts.ast.type.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            }
        ]
        EXAMPLES_INVALID = [
            {
                'code': None,
                'version': consts.ast.type.STRING,
                'code_date': consts.ast.type.STRING,
                'run_datetime': consts.ast.type.STRING,
                'title': consts.ast.type.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.type.STRING,
                'version': None,
                'code_date': consts.ast.type.STRING,
                'run_datetime': consts.ast.type.STRING,
                'title': consts.ast.type.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.type.STRING,
                'version': consts.ast.type.STRING,
                'code_date': None,
                'run_datetime': consts.ast.type.STRING,
                'title': consts.ast.type.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.type.STRING,
                'version': consts.ast.type.STRING,
                'code_date': consts.ast.type.STRING,
                'run_datetime': None,
                'title': consts.ast.type.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.type.STRING,
                'version': consts.ast.type.STRING,
                'code_date': consts.ast.type.STRING,
                'run_datetime': consts.ast.type.STRING,
                'title': None,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.type.STRING,
                'version': consts.ast.type.STRING,
                'code_date': consts.ast.type.STRING,
                'run_datetime': consts.ast.type.STRING,
                'title': consts.ast.type.STRING,
                'v_line': None,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.type.STRING,
                'version': consts.ast.type.STRING,
                'code_date': consts.ast.type.STRING,
                'run_datetime': consts.ast.type.STRING,
                'title': consts.ast.type.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': None,
                'l_line': consts.ast.ptrac.header.L,
            },
            {
                'code': consts.ast.type.STRING,
                'version': consts.ast.type.STRING,
                'code_date': consts.ast.type.STRING,
                'run_datetime': consts.ast.type.STRING,
                'title': consts.ast.type.STRING,
                'v_line': consts.ast.ptrac.header.V,
                'n_line': consts.ast.ptrac.header.N,
                'l_line': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.Header
        EXAMPLES_VALID = [consts.string.ptrac.HEADER]
        EXAMPLES_INVALID = ['hello']
