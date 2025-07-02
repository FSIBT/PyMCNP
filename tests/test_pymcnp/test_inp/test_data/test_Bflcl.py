import pymcnp
from .... import consts
from .... import classes


class Test_Bflcl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Bflcl
        EXAMPLES_VALID = [{'numbers': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Bflcl
        EXAMPLES_VALID = [consts.string.inp.data.BFLCL]
        EXAMPLES_INVALID = ['hello']


class Test_BflclBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.BflclBuilder
        EXAMPLES_VALID = [{'numbers': [consts.string.type.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]
