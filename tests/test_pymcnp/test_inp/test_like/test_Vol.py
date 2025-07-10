import pymcnp
from .... import consts
from .... import classes


class Test_Vol:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Vol
        EXAMPLES_VALID = [{'volume': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'volume': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Vol
        EXAMPLES_VALID = [consts.string.inp.like.VOL]
        EXAMPLES_INVALID = ['hello']


class Test_VolBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.like.VolBuilder
        EXAMPLES_VALID = [{'volume': consts.string.type.REAL}, {'volume': 3.1}, {'volume': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'volume': None}]
