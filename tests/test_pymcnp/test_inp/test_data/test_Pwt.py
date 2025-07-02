import pymcnp
from .... import consts
from .... import classes


class Test_Pwt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Pwt
        EXAMPLES_VALID = [{'weights': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'weights': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Pwt
        EXAMPLES_VALID = [consts.string.inp.data.PWT]
        EXAMPLES_INVALID = ['hello']


class Test_PwtBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.PwtBuilder
        EXAMPLES_VALID = [{'weights': [consts.string.type.REAL]}, {'weights': [3.1]}, {'weights': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'weights': None}]
