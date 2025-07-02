import pymcnp
from ..... import consts
from ..... import classes


class Test_Estep:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.m_0.Estep
        EXAMPLES_VALID = [{'step': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'step': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.m_0.Estep
        EXAMPLES_VALID = [consts.string.inp.data.m_0.ESTEP]
        EXAMPLES_INVALID = ['hello']


class Test_EstepBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.m_0.EstepBuilder
        EXAMPLES_VALID = [{'step': consts.string.type.INTEGER}, {'step': 1}, {'step': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'step': None}]
