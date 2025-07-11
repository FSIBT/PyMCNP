import pymcnp
from ..... import consts
from ..... import classes


class Test_Nrm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Nrm
        EXAMPLES_VALID = [{'sign': consts.string.type.INTEGER}, {'sign': 1}, {'sign': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'sign': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Nrm
        EXAMPLES_VALID = [consts.string.inp.data.sdef.NRM]
        EXAMPLES_INVALID = ['hello']
