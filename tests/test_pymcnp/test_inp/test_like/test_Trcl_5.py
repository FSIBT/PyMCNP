import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_5:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Trcl_5
        EXAMPLES_VALID = [{'prefix': pymcnp.utils.types.String('*'), 'transformation': consts.ast.type.TRANSFORMATION_4}, {'prefix': None, 'transformation': consts.ast.type.TRANSFORMATION_4}]
        EXAMPLES_INVALID = [{'prefix': pymcnp.utils.types.String('a'), 'transformation': consts.ast.type.TRANSFORMATION_4}, {'prefix': None, 'transformation': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Trcl_5
        EXAMPLES_VALID = [consts.string.inp.like.TRCL_5]
        EXAMPLES_INVALID = ['hello']


class Test_TrclBuilder_5:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.like.TrclBuilder_5
        EXAMPLES_VALID = [{'prefix': '*', 'transformation': consts.string.type.TRANSFORMATION_4}, {'prefix': None, 'transformation': consts.ast.type.TRANSFORMATION_4}]
        EXAMPLES_INVALID = [{'prefix': 'a', 'transformation': consts.string.type.TRANSFORMATION_4}, {'prefix': '*', 'transformation': None}]
