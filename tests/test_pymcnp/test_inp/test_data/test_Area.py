import pymcnp
from .... import consts
from .... import classes


class Test_Area:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Area
        EXAMPLES_VALID = [{'areas': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'areas': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Area
        EXAMPLES_VALID = [consts.string.inp.data.AREA]
        EXAMPLES_INVALID = ['hello']


class Test_AreaBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.AreaBuilder
        EXAMPLES_VALID = [{'areas': [consts.string.type.REAL]}, {'areas': [3.1]}, {'areas': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'areas': None}]
