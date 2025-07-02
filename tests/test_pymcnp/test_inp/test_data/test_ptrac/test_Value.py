import pymcnp
from ..... import consts
from ..... import classes


class Test_Value:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.Value
        EXAMPLES_VALID = [{'cutoff': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.Value
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.VALUE]
        EXAMPLES_INVALID = ['hello']


class Test_ValueBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ptrac.ValueBuilder
        EXAMPLES_VALID = [{'cutoff': consts.string.type.REAL}, {'cutoff': 3.1}, {'cutoff': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]
