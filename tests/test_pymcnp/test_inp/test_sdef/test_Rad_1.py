import pymcnp
from .... import consts
from .... import classes


class Test_Rad_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Rad_1
        EXAMPLES_VALID = [{'radial_distance': consts.string.types.DISTRIBUTION}, {'radial_distance': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'radial_distance': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Rad_1
        EXAMPLES_VALID = [consts.string.inp.sdef.RAD_1]
        EXAMPLES_INVALID = ['hello']
