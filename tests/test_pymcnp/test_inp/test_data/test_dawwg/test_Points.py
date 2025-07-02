import pymcnp
from ..... import consts
from ..... import classes


class Test_Points:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.Points
        EXAMPLES_VALID = [{'name': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'name': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.Points
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.POINTS]
        EXAMPLES_INVALID = ['hello']


class Test_PointsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.PointsBuilder
        EXAMPLES_VALID = [{'name': consts.string.type.STRING}, {'name': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'name': None}]
