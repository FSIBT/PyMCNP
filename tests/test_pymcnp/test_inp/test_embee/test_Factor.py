import pymcnp
from .... import consts
from .... import classes


class Test_Factor:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embee.Factor
        EXAMPLES_VALID = [{'constant': consts.string.types.REAL}, {'constant': 3.1}, {'constant': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'constant': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embee.Factor
        EXAMPLES_VALID = [consts.string.inp.embee.FACTOR]
        EXAMPLES_INVALID = ['hello']
