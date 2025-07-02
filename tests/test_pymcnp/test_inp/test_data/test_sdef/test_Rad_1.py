import pymcnp
from ..... import consts
from ..... import classes


class Test_Rad_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Rad_1
        EXAMPLES_VALID = [{'radial_distance': consts.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'radial_distance': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Rad_1
        EXAMPLES_VALID = [consts.string.inp.data.sdef.RAD_1]
        EXAMPLES_INVALID = ['hello']


class Test_RadBuilder_1:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.RadBuilder_1
        EXAMPLES_VALID = [{'radial_distance': consts.string.type.DISTRIBUTIONNUMBER}, {'radial_distance': consts.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'radial_distance': None}]
