import pymcnp
from .... import consts
from .... import classes


class Test_Ext:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Ext
        EXAMPLES_VALID = [{'designator': consts.string.types.DESIGNATOR, 'stretch': consts.string.types.STRING}, {'designator': consts.ast.types.DESIGNATOR, 'stretch': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'designator': None, 'stretch': consts.string.types.STRING}, {'designator': consts.string.types.DESIGNATOR, 'stretch': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Ext
        EXAMPLES_VALID = [consts.string.inp.cell.EXT]
        EXAMPLES_INVALID = ['hello']
