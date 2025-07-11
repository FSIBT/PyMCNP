import pymcnp
from ..... import consts
from ..... import classes


class Test_Wash:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Wash
        EXAMPLES_VALID = [{'aa': 'off'}, {'aa': pymcnp.types.String('off')}]
        EXAMPLES_INVALID = [{'aa': None}, {'aa': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Wash
        EXAMPLES_VALID = [consts.string.inp.data.mplot.WASH]
        EXAMPLES_INVALID = ['hello']
