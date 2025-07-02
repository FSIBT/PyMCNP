import pymcnp
from ..... import consts
from ..... import classes


class Test_Origin:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mesh.Origin
        EXAMPLES_VALID = [{'point': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'point': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mesh.Origin
        EXAMPLES_VALID = [consts.string.inp.data.mesh.ORIGIN]
        EXAMPLES_INVALID = ['hello']


class Test_OriginBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mesh.OriginBuilder
        EXAMPLES_VALID = [{'point': [consts.string.type.REAL]}, {'point': [3.1]}, {'point': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'point': None}]
