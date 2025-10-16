import pymcnp
from ... import consts
from ... import classes


class Test_Drxs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Drxs
        EXAMPLES_VALID = [{'zaids': [consts.string.types.ZAID]}, {'zaids': [consts.ast.types.ZAID]}, {'zaids': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Drxs
        EXAMPLES_VALID = [consts.string.inp.DRXS]
        EXAMPLES_INVALID = ['hello']
