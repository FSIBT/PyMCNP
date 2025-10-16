import pymcnp
from .... import consts
from .... import classes


class Test_Par_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Par_0
        EXAMPLES_VALID = [{'kind': consts.string.types.STRING}, {'kind': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'kind': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Par_0
        EXAMPLES_VALID = [consts.string.inp.sdef.PAR_0]
        EXAMPLES_INVALID = ['hello']
