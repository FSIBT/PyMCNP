import pymcnp
from ... import consts
from ... import classes


class Test_Stop:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Stop
        EXAMPLES_VALID = [{'options': [consts.string.inp.stop.CTME]}, {'options': [consts.ast.inp.stop.CTME]}, {'options': [consts.ast.inp.stop.CTME]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Stop
        EXAMPLES_VALID = [consts.string.inp.STOP]
        EXAMPLES_INVALID = ['hello']
