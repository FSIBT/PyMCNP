import pymcnp
from .... import consts
from .... import classes


class Test_Emesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmesh.Emesh
        EXAMPLES_VALID = [{'energy': consts.string.types.REAL}, {'energy': 3.1}, {'energy': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'energy': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmesh.Emesh
        EXAMPLES_VALID = [consts.string.inp.fmesh.EMESH]
        EXAMPLES_INVALID = ['hello']
