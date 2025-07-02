import pymcnp
from .... import consts
from .... import classes


class Test_Drxs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Drxs
        EXAMPLES_VALID = [{'zaids': [consts.ast.type.ZAID]}, {'zaids': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Drxs
        EXAMPLES_VALID = [consts.string.inp.data.DRXS]
        EXAMPLES_INVALID = ['hello']


class Test_DrxsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.DrxsBuilder
        EXAMPLES_VALID = [{'zaids': [consts.string.type.ZAID]}, {'zaids': [consts.ast.type.ZAID]}, {'zaids': None}]
        EXAMPLES_INVALID = []
