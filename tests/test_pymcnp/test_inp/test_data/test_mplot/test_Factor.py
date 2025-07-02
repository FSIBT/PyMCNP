import pymcnp
from ..... import consts
from ..... import classes


class Test_Factor:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Factor
        EXAMPLES_VALID = [{'a': pymcnp.types.String('x'), 'f': consts.ast.type.REAL, 's': consts.ast.type.REAL}, {'a': pymcnp.types.String('x'), 'f': consts.ast.type.REAL, 's': None}]
        EXAMPLES_INVALID = [{'a': None, 'f': consts.ast.type.REAL, 's': consts.ast.type.REAL}, {'a': pymcnp.types.String('x'), 'f': None, 's': consts.ast.type.REAL}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Factor
        EXAMPLES_VALID = [consts.string.inp.data.mplot.FACTOR]
        EXAMPLES_INVALID = ['hello']


class Test_FactorBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.FactorBuilder
        EXAMPLES_VALID = [
            {'a': 'x', 'f': consts.string.type.REAL, 's': consts.string.type.REAL},
            {'a': 'x', 'f': 3.1, 's': 3.1},
            {'a': pymcnp.types.String('x'), 'f': consts.ast.type.REAL, 's': consts.ast.type.REAL},
            {'a': 'x', 'f': consts.string.type.REAL, 's': None},
        ]
        EXAMPLES_INVALID = [
            {'a': None, 'f': consts.string.type.REAL, 's': consts.string.type.REAL},
            {'a': 'x', 'f': None, 's': consts.string.type.REAL},
            {'a': 'hello', 'f': consts.string.type.REAL, 's': consts.string.type.REAL},
        ]
