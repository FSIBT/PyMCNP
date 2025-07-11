import pymcnp
from ..... import consts
from ..... import classes


class Test_Hstep:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.m_0.Hstep
        EXAMPLES_VALID = [{'step': consts.string.type.INTEGER}, {'step': 1}, {'step': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'step': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.m_0.Hstep
        EXAMPLES_VALID = [consts.string.inp.data.m_0.HSTEP]
        EXAMPLES_INVALID = ['hello']
