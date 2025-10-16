import pymcnp
from .... import consts
from .... import classes


class Test_Pd:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Pd
        EXAMPLES_VALID = [{'suffix': consts.string.types.INTEGER, 'probability': '0.8'}, {'suffix': 1, 'probability': 0.8}, {'suffix': consts.ast.types.INTEGER, 'probability': pymcnp.types.Real(0.8)}]
        EXAMPLES_INVALID = [{'suffix': None, 'probability': '0.8'}, {'suffix': consts.string.types.INTEGER, 'probability': None}, {'suffix': consts.string.types.INTEGER, 'probability': '3.1'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Pd
        EXAMPLES_VALID = [consts.string.inp.like.PD]
        EXAMPLES_INVALID = ['hello']
