import pymcnp
from .... import consts
from .... import classes


class Test_Fill_3:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Fill_3
        EXAMPLES_VALID = [
            {'prefix': pymcnp.types.String('*'), 'universe': consts.ast.type.INTEGER, 'transformation': consts.ast.type.TRANSFORMATION_2},
            {'prefix': None, 'universe': consts.ast.type.INTEGER, 'transformation': consts.ast.type.TRANSFORMATION_2},
            {'prefix': pymcnp.types.String('*'), 'universe': consts.ast.type.INTEGER, 'transformation': None},
        ]
        EXAMPLES_INVALID = [{'prefix': pymcnp.types.String('*'), 'universe': None, 'transformation': consts.ast.type.TRANSFORMATION_2}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Fill_3
        EXAMPLES_VALID = [consts.string.inp.cell.FILL_3]
        EXAMPLES_INVALID = ['hello']


class Test_FillBuilder_3:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.cell.FillBuilder_3
        EXAMPLES_VALID = [
            {'prefix': '*', 'universe': consts.string.type.INTEGER, 'transformation': consts.string.type.TRANSFORMATION_2},
            {'prefix': '*', 'universe': 1, 'transformation': consts.string.type.TRANSFORMATION_2},
            {'prefix': pymcnp.types.String('*'), 'universe': consts.ast.type.INTEGER, 'transformation': consts.ast.type.TRANSFORMATION_2},
            {'prefix': None, 'universe': consts.string.type.INTEGER, 'transformation': consts.string.type.TRANSFORMATION_2},
            {'prefix': '*', 'universe': consts.string.type.INTEGER, 'transformation': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'universe': None, 'transformation': consts.string.type.TRANSFORMATION_2},
            {'prefix': 'hello', 'universe': consts.string.type.INTEGER, 'transformation': consts.string.type.TRANSFORMATION_2},
        ]
