import pymcnp
from .... import consts
from .... import classes


class Test_Sc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Sc
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'comment': [consts.string.types.STRING]},
            {'suffix': 1, 'comment': [consts.string.types.STRING]},
            {'suffix': consts.ast.types.INTEGER, 'comment': [consts.ast.types.STRING]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'comment': [consts.string.types.STRING]}, {'suffix': consts.string.types.INTEGER, 'comment': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Sc
        EXAMPLES_VALID = [consts.string.inp.data.SC]
        EXAMPLES_INVALID = ['hello']
