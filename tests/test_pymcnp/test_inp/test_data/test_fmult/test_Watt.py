import pymcnp
from ..... import consts
from ..... import classes


class Test_Watt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmult.Watt
        EXAMPLES_VALID = [{'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'a': None, 'b': consts.ast.type.REAL}, {'a': consts.ast.type.REAL, 'b': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmult.Watt
        EXAMPLES_VALID = [consts.string.inp.data.fmult.WATT]
        EXAMPLES_INVALID = ['hello']


class Test_WattBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmult.WattBuilder
        EXAMPLES_VALID = [{'a': consts.string.type.REAL, 'b': consts.string.type.REAL}, {'a': 3.1, 'b': 3.1}, {'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'a': None, 'b': consts.string.type.REAL}, {'a': consts.string.type.REAL, 'b': None}]
