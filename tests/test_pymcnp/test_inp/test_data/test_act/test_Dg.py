import pymcnp
from ..... import consts
from ..... import classes


class Test_Dg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Dg
        EXAMPLES_VALID = [{'source': consts.string.types.STRING}, {'source': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'source': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Dg
        EXAMPLES_VALID = [consts.string.inp.data.act.DG]
        EXAMPLES_INVALID = ['hello']
