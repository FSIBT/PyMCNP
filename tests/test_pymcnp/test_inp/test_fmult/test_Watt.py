import pymcnp
from .... import consts
from .... import classes


class Test_Watt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmult.Watt
        EXAMPLES_VALID = [{'a': consts.string.types.REAL, 'b': consts.string.types.REAL}, {'a': 3.1, 'b': 3.1}, {'a': consts.ast.types.REAL, 'b': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'a': None, 'b': consts.string.types.REAL}, {'a': consts.string.types.REAL, 'b': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmult.Watt
        EXAMPLES_VALID = [consts.string.inp.fmult.WATT]
        EXAMPLES_INVALID = ['hello']
