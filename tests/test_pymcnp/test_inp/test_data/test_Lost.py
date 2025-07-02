import pymcnp
from .... import consts
from .... import classes


class Test_Lost:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Lost
        EXAMPLES_VALID = [{'lost1': consts.ast.type.INTEGER, 'lost2': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'lost1': None, 'lost2': consts.ast.type.INTEGER}, {'lost1': consts.ast.type.INTEGER, 'lost2': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Lost
        EXAMPLES_VALID = [consts.string.inp.data.LOST]
        EXAMPLES_INVALID = ['hello']


class Test_LostBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.LostBuilder
        EXAMPLES_VALID = [{'lost1': consts.string.type.INTEGER, 'lost2': consts.string.type.INTEGER}, {'lost1': 1, 'lost2': 1}, {'lost1': consts.ast.type.INTEGER, 'lost2': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'lost1': None, 'lost2': consts.string.type.INTEGER}, {'lost1': consts.string.type.INTEGER, 'lost2': None}]
