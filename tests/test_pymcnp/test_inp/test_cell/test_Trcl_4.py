import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_4:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Trcl_4
        EXAMPLES_VALID = [{'transformation': consts.ast.type.TRANSFORMATION_3}]
        EXAMPLES_INVALID = [{'transformation': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Trcl_4
        EXAMPLES_VALID = [consts.string.inp.cell.TRCL_4]
        EXAMPLES_INVALID = ['hello']


class Test_TrclBuilder_4:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_4
        EXAMPLES_VALID = [{'transformation': consts.string.type.TRANSFORMATION_3}, {'transformation': consts.ast.type.TRANSFORMATION_3}]
        EXAMPLES_INVALID = [{'transformation': None}]
