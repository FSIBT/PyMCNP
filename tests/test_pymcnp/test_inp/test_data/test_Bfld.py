import pymcnp
from .... import consts
from .... import classes


class Test_Bfld:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Bfld
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'kind': 'const', 'options': [consts.string.inp.data.bfld.AXS]},
            {'suffix': 1, 'kind': 'const', 'options': [consts.ast.inp.data.bfld.AXS]},
            {'suffix': consts.ast.types.INTEGER, 'kind': pymcnp.types.String('const'), 'options': [consts.ast.inp.data.bfld.AXS]},
            {'suffix': consts.string.types.INTEGER, 'kind': 'const', 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'kind': 'const', 'options': [consts.string.inp.data.bfld.AXS]},
            {'suffix': consts.string.types.INTEGER, 'kind': None, 'options': [consts.string.inp.data.bfld.AXS]},
            {'suffix': consts.string.types.INTEGER, 'kind': 'hello', 'options': [consts.string.inp.data.bfld.AXS]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Bfld
        EXAMPLES_VALID = [consts.string.inp.data.BFLD]
        EXAMPLES_INVALID = ['hello']
