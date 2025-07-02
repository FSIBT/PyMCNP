import pymcnp
from ..... import consts
from ..... import classes


class Test_Cel:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssw.Cel
        EXAMPLES_VALID = [{'cfs': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'cfs': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssw.Cel
        EXAMPLES_VALID = [consts.string.inp.data.ssw.CEL]
        EXAMPLES_INVALID = ['hello']


class Test_CelBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ssw.CelBuilder
        EXAMPLES_VALID = [{'cfs': [consts.string.type.INTEGER]}, {'cfs': [1]}, {'cfs': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'cfs': None}]
