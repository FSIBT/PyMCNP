import pymcnp
from ..... import consts
from ..... import classes


class Test_Out:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Out
        EXAMPLES_VALID = [{'setting': consts.string.types.STRING}, {'setting': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Out
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.OUT]
        EXAMPLES_INVALID = ['hello']
