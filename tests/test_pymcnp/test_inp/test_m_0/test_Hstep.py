import pymcnp
from .... import consts
from .... import classes


class Test_Hstep:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.m_0.Hstep
        EXAMPLES_VALID = [{'step': consts.string.types.INTEGER}, {'step': 1}, {'step': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'step': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.m_0.Hstep
        EXAMPLES_VALID = [consts.string.inp.m_0.HSTEP]
        EXAMPLES_INVALID = ['hello']
