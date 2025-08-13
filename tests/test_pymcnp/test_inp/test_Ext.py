import pymcnp
from ... import consts
from ... import classes


class Test_Ext:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ext
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'stretching': [consts.string.types.STRING]},
            {'designator': consts.ast.types.DESIGNATOR, 'stretching': [consts.ast.types.STRING]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'stretching': [consts.string.types.STRING]}, {'designator': consts.string.types.DESIGNATOR, 'stretching': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ext
        EXAMPLES_VALID = [consts.string.inp.EXT]
        EXAMPLES_INVALID = ['hello']
