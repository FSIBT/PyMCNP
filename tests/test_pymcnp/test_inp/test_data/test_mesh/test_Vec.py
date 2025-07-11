import pymcnp
from ..... import consts
from ..... import classes


class Test_Vec:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mesh.Vec
        EXAMPLES_VALID = [{'vector': [consts.string.type.REAL]}, {'vector': [3.1]}, {'vector': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mesh.Vec
        EXAMPLES_VALID = [consts.string.inp.data.mesh.VEC]
        EXAMPLES_INVALID = ['hello']
