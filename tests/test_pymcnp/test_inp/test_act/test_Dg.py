import pymcnp
from .... import consts
from .... import classes


class Test_Dg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.act.Dg
        EXAMPLES_VALID = [{'source': consts.string.types.STRING}, {'source': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'source': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.act.Dg
        EXAMPLES_VALID = [consts.string.inp.act.DG]
        EXAMPLES_INVALID = ['hello']
