import pymcnp
from .... import consts
from .... import classes


class Test_Refi:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.m_0.Refi
        EXAMPLES_VALID = [{'refractive_index': consts.string.types.REAL}, {'refractive_index': 3.1}, {'refractive_index': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'refractive_index': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.m_0.Refi
        EXAMPLES_VALID = [consts.string.inp.m_0.REFI]
        EXAMPLES_INVALID = ['hello']
