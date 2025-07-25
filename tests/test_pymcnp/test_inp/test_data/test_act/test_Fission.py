import pymcnp
from ..... import consts
from ..... import classes


class Test_Fission:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Fission
        EXAMPLES_VALID = [{'kind': consts.string.types.STRING}, {'kind': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'kind': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Fission
        EXAMPLES_VALID = [consts.string.inp.data.act.FISSION]
        EXAMPLES_INVALID = ['hello']
