import pymcnp
from .... import consts
from .... import classes


class Test_Lat:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Lat
        EXAMPLES_VALID = [{'type': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'type': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Lat
        EXAMPLES_VALID = [consts.string.inp.data.LAT]
        EXAMPLES_INVALID = ['hello']


class Test_LatBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.LatBuilder
        EXAMPLES_VALID = [{'type': [consts.string.type.INTEGER]}, {'type': [1]}, {'type': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'type': None}]
