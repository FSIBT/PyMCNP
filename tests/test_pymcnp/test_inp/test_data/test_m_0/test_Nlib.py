import pymcnp
from ..... import consts
from ..... import classes


class Test_Nlib:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.m_0.Nlib
        EXAMPLES_VALID = [{'abx': consts.string.types.STRING}, {'abx': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'abx': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.m_0.Nlib
        EXAMPLES_VALID = [consts.string.inp.data.m_0.NLIB]
        EXAMPLES_INVALID = ['hello']
