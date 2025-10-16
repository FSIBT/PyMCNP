import pymcnp
from .... import consts
from .... import classes


class Test_Rad_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Rad_0
        EXAMPLES_VALID = [{'radial_distance': consts.string.types.REAL}, {'radial_distance': 3.1}, {'radial_distance': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'radial_distance': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Rad_0
        EXAMPLES_VALID = [consts.string.inp.sdef.RAD_0]
        EXAMPLES_INVALID = ['hello']
