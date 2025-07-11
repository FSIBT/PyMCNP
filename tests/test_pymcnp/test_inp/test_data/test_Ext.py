import pymcnp
from .... import consts
from .... import classes


class Test_Ext:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ext
        EXAMPLES_VALID = [{'designator': consts.string.type.DESIGNATOR, 'stretching': [consts.string.type.STRING]}, {'designator': consts.ast.type.DESIGNATOR, 'stretching': [consts.ast.type.STRING]}]
        EXAMPLES_INVALID = [{'designator': None, 'stretching': [consts.string.type.STRING]}, {'designator': consts.string.type.DESIGNATOR, 'stretching': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ext
        EXAMPLES_VALID = [consts.string.inp.data.EXT]
        EXAMPLES_INVALID = ['hello']
