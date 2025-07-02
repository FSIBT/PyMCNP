import pymcnp
from ..... import consts
from ..... import classes


class Test_Gas:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.m_0.Gas
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.m_0.Gas
        EXAMPLES_VALID = [consts.string.inp.data.m_0.GAS]
        EXAMPLES_INVALID = ['hello']


class Test_GasBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.m_0.GasBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
