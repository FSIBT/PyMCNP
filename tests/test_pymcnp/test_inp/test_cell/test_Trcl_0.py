import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Trcl_0
        EXAMPLES_VALID = [{'transformation': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'transformation': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Trcl_0
        EXAMPLES_VALID = [consts.string.inp.cell.TRCL_0]
        EXAMPLES_INVALID = ['hello']


class Test_TrclBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_0
        EXAMPLES_VALID = [{'transformation': consts.string.type.INTEGER}, {'transformation': 1}, {'transformation': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'transformation': None}]
