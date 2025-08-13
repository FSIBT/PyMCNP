import pymcnp
from .... import consts
from .... import classes


class Test_Factor:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmesh.Factor
        EXAMPLES_VALID = [{'multiple': consts.string.types.REAL}, {'multiple': 3.1}, {'multiple': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'multiple': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmesh.Factor
        EXAMPLES_VALID = [consts.string.inp.fmesh.FACTOR]
        EXAMPLES_INVALID = ['hello']
