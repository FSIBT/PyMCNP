import pymcnp
from .... import consts
from .... import classes


class Test_Vol:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Vol
        EXAMPLES_VALID = [{'no': pymcnp.types.String('no'), 'volumes': [consts.ast.type.REAL]}, {'no': None, 'volumes': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'no': pymcnp.types.String('no'), 'volumes': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Vol
        EXAMPLES_VALID = [consts.string.inp.data.VOL]
        EXAMPLES_INVALID = ['hello']


class Test_VolBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.VolBuilder
        EXAMPLES_VALID = [
            {'no': 'no', 'volumes': [consts.string.type.REAL]},
            {'no': 'no', 'volumes': [3.1]},
            {'no': pymcnp.types.String('no'), 'volumes': [consts.ast.type.REAL]},
            {'no': None, 'volumes': [consts.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'no': 'no', 'volumes': None}, {'no': 'hello', 'volumes': [consts.string.type.REAL]}]
