import pymcnp
from ..... import consts
from ..... import classes


class Test_Log:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.df_1.Log
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.df_1.Log
        EXAMPLES_VALID = [consts.string.inp.data.df_1.LOG]
        EXAMPLES_INVALID = ['hello']


class Test_LogBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.df_1.LogBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
