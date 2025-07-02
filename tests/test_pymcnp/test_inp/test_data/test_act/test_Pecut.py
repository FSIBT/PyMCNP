import pymcnp
from ..... import consts
from ..... import classes


class Test_Pecut:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Pecut
        EXAMPLES_VALID = [{'cutoff': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Pecut
        EXAMPLES_VALID = [consts.string.inp.data.act.PECUT]
        EXAMPLES_INVALID = ['hello']


class Test_PecutBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.act.PecutBuilder
        EXAMPLES_VALID = [{'cutoff': consts.string.type.REAL}, {'cutoff': 3.1}, {'cutoff': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'cutoff': None}]
