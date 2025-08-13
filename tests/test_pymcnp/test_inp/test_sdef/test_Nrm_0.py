import pymcnp
from .... import consts
from .... import classes


class Test_Nrm_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Nrm_0
        EXAMPLES_VALID = [{'sign': consts.string.types.INTEGER}, {'sign': 1}, {'sign': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'sign': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Nrm_0
        EXAMPLES_VALID = [consts.string.inp.sdef.NRM_0]
        EXAMPLES_INVALID = ['hello']
