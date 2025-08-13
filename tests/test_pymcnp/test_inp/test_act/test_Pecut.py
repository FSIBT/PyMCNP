import pymcnp
from .... import consts
from .... import classes


class Test_Pecut:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.act.Pecut
        EXAMPLES_VALID = [{'cutoff': consts.string.types.REAL}, {'cutoff': 3.1}, {'cutoff': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.act.Pecut
        EXAMPLES_VALID = [consts.string.inp.act.PECUT]
        EXAMPLES_INVALID = ['hello']
