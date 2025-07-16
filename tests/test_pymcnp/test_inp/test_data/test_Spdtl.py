import pymcnp
from .... import consts
from .... import classes


class Test_Spdtl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Spdtl
        EXAMPLES_VALID = [{'keyword': consts.string.types.STRING}, {'keyword': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'keyword': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Spdtl
        EXAMPLES_VALID = [consts.string.inp.data.SPDTL]
        EXAMPLES_INVALID = ['hello']
