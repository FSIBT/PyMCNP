import pymcnp
from .... import consts
from .... import classes


class Test_Uran:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Uran
        EXAMPLES_VALID = [{'transformations': [consts.ast.type.STOCHASTIC]}]
        EXAMPLES_INVALID = [{'transformations': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Uran
        EXAMPLES_VALID = [consts.string.inp.data.URAN]
        EXAMPLES_INVALID = ['hello']


class Test_UranBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.UranBuilder
        EXAMPLES_VALID = [{'transformations': [consts.string.type.STOCHASTIC]}, {'transformations': [consts.ast.type.STOCHASTIC]}]
        EXAMPLES_INVALID = [{'transformations': None}]
