import pymcnp
from ..... import consts
from ..... import classes


class Test_Hlib:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.m_0.Hlib
        EXAMPLES_VALID = [{'abx': consts.string.type.STRING}, {'abx': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'abx': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.m_0.Hlib
        EXAMPLES_VALID = [consts.string.inp.data.m_0.HLIB]
        EXAMPLES_INVALID = ['hello']
