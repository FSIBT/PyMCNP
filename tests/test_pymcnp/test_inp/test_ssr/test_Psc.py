import pymcnp
from .... import consts
from .... import classes


class Test_Psc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ssr.Psc
        EXAMPLES_VALID = [{'constant': consts.string.types.REAL}, {'constant': 3.1}, {'constant': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'constant': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ssr.Psc
        EXAMPLES_VALID = [consts.string.inp.ssr.PSC]
        EXAMPLES_INVALID = ['hello']
