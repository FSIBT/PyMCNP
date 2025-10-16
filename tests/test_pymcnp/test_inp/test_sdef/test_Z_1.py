import pymcnp
from .... import consts
from .... import classes


class Test_Z_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Z_1
        EXAMPLES_VALID = [{'position': consts.string.types.DISTRIBUTION}, {'position': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'position': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Z_1
        EXAMPLES_VALID = [consts.string.inp.sdef.Z_1]
        EXAMPLES_INVALID = ['hello']
