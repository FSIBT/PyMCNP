import pymcnp
from ..... import consts
from ..... import classes


class Test_Xs_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Xs_2
        EXAMPLES_VALID = [{'m': pymcnp.types.String('?')}]
        EXAMPLES_INVALID = [{'m': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Xs_2
        EXAMPLES_VALID = [consts.string.inp.data.mplot.XS_2]
        EXAMPLES_INVALID = ['hello']


class Test_XsBuilder_2:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.XsBuilder_2
        EXAMPLES_VALID = [{'m': '?'}, {'m': pymcnp.types.String('?')}]
        EXAMPLES_INVALID = [{'m': None}, {'m': 'hello'}]
