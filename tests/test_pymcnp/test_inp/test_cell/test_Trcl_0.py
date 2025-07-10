import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Trcl_0
        EXAMPLES_VALID = [{'prefix': pymcnp.utils.types.String('*'), 'transformation': consts.ast.type.INTEGER}, {'prefix': None, 'transformation': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'prefix': consts.ast.type.STRING, 'transformation': consts.ast.type.INTEGER}, {'prefix': None, 'transformation': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Trcl_0
        EXAMPLES_VALID = [consts.string.inp.cell.TRCL_0]
        EXAMPLES_INVALID = ['hello']


class Test_TrclBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_0
        EXAMPLES_VALID = [{'prefix': '*', 'transformation': consts.string.type.INTEGER}, {'prefix': '*', 'transformation': 1}, {'prefix': None, 'transformation': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'prefix': '*', 'transformation': None}, {'prefix': consts.string.type.STRING, 'transformation': None}]
