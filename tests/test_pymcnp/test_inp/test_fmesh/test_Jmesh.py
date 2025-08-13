import pymcnp
from .... import consts
from .... import classes


class Test_Jmesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmesh.Jmesh
        EXAMPLES_VALID = [{'locations': [consts.string.types.REAL]}, {'locations': [3.1]}, {'locations': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'locations': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmesh.Jmesh
        EXAMPLES_VALID = [consts.string.inp.fmesh.JMESH]
        EXAMPLES_INVALID = ['hello']
