import pymcnp
from .... import consts
from .... import classes


class Test_Tlib:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.m_0.Tlib
        EXAMPLES_VALID = [{'abx': consts.string.types.STRING}, {'abx': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'abx': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.m_0.Tlib
        EXAMPLES_VALID = [consts.string.inp.m_0.TLIB]
        EXAMPLES_INVALID = ['hello']
