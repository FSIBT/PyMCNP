import pymcnp
from ..... import consts
from ..... import classes


class Test_Cond:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.m_0.Cond
        EXAMPLES_VALID = [{'setting': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.m_0.Cond
        EXAMPLES_VALID = [consts.string.inp.data.m_0.COND]
        EXAMPLES_INVALID = ['hello']


class Test_CondBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.m_0.CondBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.REAL}, {'setting': 3.1}, {'setting': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]
