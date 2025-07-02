import pymcnp
from ..... import consts
from ..... import classes


class Test_Kmesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Kmesh
        EXAMPLES_VALID = [{'locations': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'locations': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Kmesh
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.KMESH]
        EXAMPLES_INVALID = ['hello']


class Test_KmeshBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmesh.KmeshBuilder
        EXAMPLES_VALID = [{'locations': [consts.string.type.REAL]}, {'locations': [3.1]}, {'locations': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'locations': None}]
