import pymcnp
from ... import consts
from ... import classes


class Test_Nps:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Nps
        EXAMPLES_VALID = [
            {'npp': consts.string.types.INTEGER, 'npsmg': consts.string.types.INTEGER},
            {'npp': 1, 'npsmg': 1},
            {'npp': consts.ast.types.INTEGER, 'npsmg': consts.ast.types.INTEGER},
            {'npp': consts.string.types.INTEGER, 'npsmg': None},
        ]
        EXAMPLES_INVALID = [{'npp': None, 'npsmg': consts.string.types.INTEGER}, {'npp': consts.string.types.INTEGER, 'npsmg': -9999}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Nps
        EXAMPLES_VALID = [consts.string.inp.NPS]
        EXAMPLES_INVALID = ['hello']
