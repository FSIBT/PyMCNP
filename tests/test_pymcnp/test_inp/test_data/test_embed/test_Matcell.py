import pymcnp
from ..... import consts
from ..... import classes


class Test_Matcell:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Matcell
        EXAMPLES_VALID = [{'pairs': [consts.ast.type.MATCELL]}]
        EXAMPLES_INVALID = [{'pairs': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Matcell
        EXAMPLES_VALID = [consts.string.inp.data.embed.MATCELL]
        EXAMPLES_INVALID = ['hello']


class Test_MatcellBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.embed.MatcellBuilder
        EXAMPLES_VALID = [{'pairs': [consts.string.type.MATCELL]}, {'pairs': [consts.ast.type.MATCELL]}]
        EXAMPLES_INVALID = [{'pairs': None}]
