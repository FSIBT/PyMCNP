import pymcnp
from ..... import consts
from ..... import classes


class Test_Emesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Emesh
        EXAMPLES_VALID = [{'energy': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'energy': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Emesh
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.EMESH]
        EXAMPLES_INVALID = ['hello']


class Test_EmeshBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmesh.EmeshBuilder
        EXAMPLES_VALID = [{'energy': consts.string.type.REAL}, {'energy': 3.1}, {'energy': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'energy': None}]
