import pymcnp
from .... import consts
from .... import classes


class Test_Bflcl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Bflcl
        EXAMPLES_VALID = [{'number': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Bflcl
        EXAMPLES_VALID = [consts.string.inp.like.BFLCL]
        EXAMPLES_INVALID = ['hello']


class Test_BflclBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.like.BflclBuilder
        EXAMPLES_VALID = [{'number': consts.string.type.INTEGER}, {'number': 1}, {'number': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]
