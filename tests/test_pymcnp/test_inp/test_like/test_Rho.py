import pymcnp
from .... import consts
from .... import classes


class Test_Rho:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Rho
        EXAMPLES_VALID = [{'density': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'density': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Rho
        EXAMPLES_VALID = [consts.string.inp.like.RHO]
        EXAMPLES_INVALID = ['hello']


class Test_RhoBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.like.RhoBuilder
        EXAMPLES_VALID = [{'density': consts.string.type.REAL}, {'density': 0.1}, {'density': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'density': None}]
