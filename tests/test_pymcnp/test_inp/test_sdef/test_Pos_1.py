import pymcnp
from .... import consts
from .... import classes


class Test_Pos_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Pos_1
        EXAMPLES_VALID = [{'vector': consts.string.types.DISTRIBUTION}, {'vector': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'vector': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Pos_1
        EXAMPLES_VALID = [consts.string.inp.sdef.POS_1]
        EXAMPLES_INVALID = ['hello']
