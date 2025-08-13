import pymcnp
from .... import consts
from .... import classes


class Test_Imesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mesh.Imesh
        EXAMPLES_VALID = [{'vector': [consts.string.types.REAL]}, {'vector': [3.1]}, {'vector': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mesh.Imesh
        EXAMPLES_VALID = [consts.string.inp.mesh.IMESH]
        EXAMPLES_INVALID = ['hello']
