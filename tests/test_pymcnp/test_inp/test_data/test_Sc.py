import pymcnp
from .... import consts
from .... import classes


class Test_Sc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Sc
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'comment': [consts.string.type.STRING]},
            {'suffix': 1, 'comment': [consts.string.type.STRING]},
            {'suffix': consts.ast.type.INTEGER, 'comment': [consts.ast.type.STRING]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'comment': [consts.string.type.STRING]}, {'suffix': consts.string.type.INTEGER, 'comment': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Sc
        EXAMPLES_VALID = [consts.string.inp.data.SC]
        EXAMPLES_INVALID = ['hello']
