import pymcnp
from .... import consts
from .... import classes


class Test_Cond:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.m_0.Cond
        EXAMPLES_VALID = [{'setting': consts.string.types.REAL}, {'setting': 3.1}, {'setting': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.m_0.Cond
        EXAMPLES_VALID = [consts.string.inp.m_0.COND]
        EXAMPLES_INVALID = ['hello']
