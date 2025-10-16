import pymcnp
from .... import consts
from .... import classes


class Test_Wgt_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Wgt_0
        EXAMPLES_VALID = [{'weight': consts.string.types.REAL}, {'weight': 3.1}, {'weight': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'weight': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Wgt_0
        EXAMPLES_VALID = [consts.string.inp.sdef.WGT_0]
        EXAMPLES_INVALID = ['hello']
