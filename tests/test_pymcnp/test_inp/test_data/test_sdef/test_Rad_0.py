import pymcnp
from ..... import consts
from ..... import classes


class Test_Rad_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Rad_0
        EXAMPLES_VALID = [{'radial_distance': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'radial_distance': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Rad_0
        EXAMPLES_VALID = [consts.string.inp.data.sdef.RAD_0]
        EXAMPLES_INVALID = ['hello']


class Test_RadBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.RadBuilder_0
        EXAMPLES_VALID = [{'radial_distance': consts.string.type.REAL}, {'radial_distance': 3.1}, {'radial_distance': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'radial_distance': None}]
