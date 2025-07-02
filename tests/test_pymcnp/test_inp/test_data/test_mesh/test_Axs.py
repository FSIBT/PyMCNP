import pymcnp
from ..... import consts
from ..... import classes


class Test_Axs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mesh.Axs
        EXAMPLES_VALID = [{'vector': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mesh.Axs
        EXAMPLES_VALID = [consts.string.inp.data.mesh.AXS]
        EXAMPLES_INVALID = ['hello']


class Test_AxsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mesh.AxsBuilder
        EXAMPLES_VALID = [{'vector': [consts.string.type.REAL]}, {'vector': [3.1]}, {'vector': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'vector': None}]
