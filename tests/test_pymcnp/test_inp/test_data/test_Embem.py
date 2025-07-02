import pymcnp
from .... import consts
from .... import classes


class Test_Embem:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Embem
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'multipliers': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'suffix': None, 'multipliers': [consts.ast.type.REAL]}, {'suffix': consts.ast.type.INTEGER, 'multipliers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Embem
        EXAMPLES_VALID = [consts.string.inp.data.EMBEM]
        EXAMPLES_INVALID = ['hello']


class Test_EmbemBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.EmbemBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'multipliers': [consts.string.type.REAL]},
            {'suffix': 1, 'multipliers': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'multipliers': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'multipliers': [consts.string.type.REAL]}, {'suffix': consts.string.type.INTEGER, 'multipliers': None}]
