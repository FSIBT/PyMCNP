import pymcnp
from ..... import consts
from ..... import classes


class Test_Wash:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Wash
        EXAMPLES_VALID = [{'aa': pymcnp.types.String('off')}]
        EXAMPLES_INVALID = [{'aa': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Wash
        EXAMPLES_VALID = [consts.string.inp.data.mplot.WASH]
        EXAMPLES_INVALID = ['hello']


class Test_WashBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.WashBuilder
        EXAMPLES_VALID = [{'aa': 'off'}, {'aa': pymcnp.types.String('off')}]
        EXAMPLES_INVALID = [{'aa': None}, {'aa': 'hello'}]
