import pymcnp
from ..... import consts
from ..... import classes


class Test_Alib:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.m_0.Alib
        EXAMPLES_VALID = [{'abx': consts.string.type.STRING}, {'abx': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'abx': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.m_0.Alib
        EXAMPLES_VALID = [consts.string.inp.data.m_0.ALIB]
        EXAMPLES_INVALID = ['hello']
