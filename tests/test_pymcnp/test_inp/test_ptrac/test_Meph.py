import pymcnp
from .... import consts
from .... import classes


class Test_Meph:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.Meph
        EXAMPLES_VALID = [{'events': consts.string.types.INTEGER}, {'events': 1}, {'events': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'events': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.Meph
        EXAMPLES_VALID = [consts.string.inp.ptrac.MEPH]
        EXAMPLES_INVALID = ['hello']
