import pymcnp
from ..... import consts
from ..... import classes


class Test_Lin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.df_1.Lin
        EXAMPLES_VALID = [{}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.df_1.Lin
        EXAMPLES_VALID = [consts.string.inp.data.df_1.LIN]
        EXAMPLES_INVALID = ['hello']


class Test_LinBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.df_1.LinBuilder
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []
