import pymcnp
from ..... import consts
from ..... import classes


class Test_Nrm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Nrm
        EXAMPLES_VALID = [{'sign': consts.string.types.INTEGER}, {'sign': 1}, {'sign': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'sign': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Nrm
        EXAMPLES_VALID = [consts.string.inp.data.sdef.NRM]
        EXAMPLES_INVALID = ['hello']
