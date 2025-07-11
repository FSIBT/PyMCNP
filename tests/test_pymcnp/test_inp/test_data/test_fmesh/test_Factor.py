import pymcnp
from ..... import consts
from ..... import classes


class Test_Factor:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Factor
        EXAMPLES_VALID = [{'multiple': consts.string.type.REAL}, {'multiple': 3.1}, {'multiple': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'multiple': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Factor
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.FACTOR]
        EXAMPLES_INVALID = ['hello']
