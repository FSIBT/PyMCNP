import pymcnp
from .... import consts
from .... import classes


class Test_Ref:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mesh.Ref
        EXAMPLES_VALID = [{'point': [consts.string.types.REAL]}, {'point': [3.1]}, {'point': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'point': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mesh.Ref
        EXAMPLES_VALID = [consts.string.inp.mesh.REF]
        EXAMPLES_INVALID = ['hello']
