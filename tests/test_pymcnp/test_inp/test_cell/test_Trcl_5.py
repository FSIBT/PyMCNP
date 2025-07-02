import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_5:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Trcl_5
        EXAMPLES_VALID = [{'transformation': consts.ast.type.TRANSFORMATION_4}]
        EXAMPLES_INVALID = [{'transformation': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Trcl_5
        EXAMPLES_VALID = [consts.string.inp.cell.TRCL_5]
        EXAMPLES_INVALID = ['hello']


class Test_TrclBuilder_5:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_5
        EXAMPLES_VALID = [{'transformation': consts.string.type.TRANSFORMATION_4}, {'transformation': consts.ast.type.TRANSFORMATION_4}]
        EXAMPLES_INVALID = [{'transformation': None}]
