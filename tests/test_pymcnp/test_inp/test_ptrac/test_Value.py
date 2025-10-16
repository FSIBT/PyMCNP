import pymcnp
from .... import consts
from .... import classes


class Test_Value:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.Value
        EXAMPLES_VALID = [{'cutoff': consts.string.types.REAL}, {'cutoff': 3.1}, {'cutoff': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.Value
        EXAMPLES_VALID = [consts.string.inp.ptrac.VALUE]
        EXAMPLES_INVALID = ['hello']
