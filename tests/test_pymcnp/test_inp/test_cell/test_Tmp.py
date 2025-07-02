import pymcnp
from .... import consts
from .... import classes


class Test_Tmp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Tmp
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'temperature': [consts.ast.type.REAL]}, {'suffix': None, 'temperature': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'suffix': consts.ast.type.INTEGER, 'temperature': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Tmp
        EXAMPLES_VALID = [consts.string.inp.cell.TMP]
        EXAMPLES_INVALID = ['hello']


class Test_TmpBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.cell.TmpBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'temperature': [consts.string.type.REAL]},
            {'suffix': 1, 'temperature': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'temperature': [consts.ast.type.REAL]},
            {'suffix': None, 'temperature': [consts.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': consts.string.type.INTEGER, 'temperature': None}]
