import pymcnp
from .... import consts
from .... import classes


class Test_Wwn:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Wwn
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'bounds': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.ast.type.DESIGNATOR, 'bounds': [consts.ast.type.REAL]},
            {'suffix': consts.ast.type.INTEGER, 'designator': None, 'bounds': [consts.ast.type.REAL]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'bounds': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Wwn
        EXAMPLES_VALID = [consts.string.inp.data.WWN]
        EXAMPLES_INVALID = ['hello']


class Test_WwnBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.WwnBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'bounds': [consts.string.type.REAL]},
            {'suffix': 1, 'designator': consts.string.type.DESIGNATOR, 'bounds': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'bounds': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.type.DESIGNATOR, 'bounds': [consts.string.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'designator': None, 'bounds': [consts.string.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'bounds': None},
        ]
