import pymcnp
from .... import consts
from .... import classes


class Test_Ext:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Ext
        EXAMPLES_VALID = [{'designator': consts.string.type.DESIGNATOR, 'stretch': consts.string.type.STRING}, {'designator': consts.ast.type.DESIGNATOR, 'stretch': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'designator': None, 'stretch': consts.string.type.STRING}, {'designator': consts.string.type.DESIGNATOR, 'stretch': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Ext
        EXAMPLES_VALID = [consts.string.inp.cell.EXT]
        EXAMPLES_INVALID = ['hello']
