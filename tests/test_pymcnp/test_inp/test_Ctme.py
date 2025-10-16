import pymcnp
from ... import consts
from ... import classes


class Test_Ctme:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ctme
        EXAMPLES_VALID = [{'tme': consts.string.types.INTEGER}, {'tme': 1}, {'tme': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'tme': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ctme
        EXAMPLES_VALID = [consts.string.inp.CTME]
        EXAMPLES_INVALID = ['hello']
