import pymcnp
from .... import consts
from .... import classes


class Test_Gas:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.m_0.Gas
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.m_0.Gas
        EXAMPLES_VALID = [consts.string.inp.m_0.GAS]
        EXAMPLES_INVALID = ['hello']
