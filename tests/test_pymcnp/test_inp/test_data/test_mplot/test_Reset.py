import pymcnp
from ..... import consts
from ..... import classes


class Test_Reset:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Reset
        EXAMPLES_VALID = [{'aa': pymcnp.types.String('all')}, {'aa': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Reset
        EXAMPLES_VALID = [consts.string.inp.data.mplot.RESET]
        EXAMPLES_INVALID = ['hello']


class Test_ResetBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.ResetBuilder
        EXAMPLES_VALID = [{'aa': 'all'}, {'aa': pymcnp.types.String('all')}, {'aa': None}]
        EXAMPLES_INVALID = [{'aa': 'hello'}]
