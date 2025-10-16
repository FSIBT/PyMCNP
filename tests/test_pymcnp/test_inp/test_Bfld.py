import pymcnp
from ... import consts
from ... import classes


class Test_Bfld:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Bfld
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'kind': 'const', 'options': [consts.string.inp.bfld.AXS]},
            {'suffix': 1, 'kind': 'const', 'options': [consts.ast.inp.bfld.AXS]},
            {'suffix': consts.ast.types.INTEGER, 'kind': pymcnp.types.String('const'), 'options': [consts.ast.inp.bfld.AXS]},
            {'suffix': consts.string.types.INTEGER, 'kind': 'const', 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'kind': 'const', 'options': [consts.string.inp.bfld.AXS]},
            {'suffix': consts.string.types.INTEGER, 'kind': None, 'options': [consts.string.inp.bfld.AXS]},
            {'suffix': consts.string.types.INTEGER, 'kind': 'hello', 'options': [consts.string.inp.bfld.AXS]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Bfld
        EXAMPLES_VALID = [consts.string.inp.BFLD]
        EXAMPLES_INVALID = ['hello']
