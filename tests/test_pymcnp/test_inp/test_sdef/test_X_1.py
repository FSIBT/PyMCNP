import pymcnp
from .... import consts
from .... import classes


class Test_X_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.X_1
        EXAMPLES_VALID = [{'position': consts.string.types.DISTRIBUTION}, {'position': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'position': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.X_1
        EXAMPLES_VALID = [consts.string.inp.sdef.X_1]
        EXAMPLES_INVALID = ['hello']
