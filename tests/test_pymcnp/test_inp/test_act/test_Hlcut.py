import pymcnp
from .... import consts
from .... import classes


class Test_Hlcut:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.act.Hlcut
        EXAMPLES_VALID = [{'cutoff': consts.string.types.REAL}, {'cutoff': 3.1}, {'cutoff': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.act.Hlcut
        EXAMPLES_VALID = [consts.string.inp.act.HLCUT]
        EXAMPLES_INVALID = ['hello']
