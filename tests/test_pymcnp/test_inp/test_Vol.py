import pymcnp
from ... import consts
from ... import classes


class Test_Vol:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Vol
        EXAMPLES_VALID = [
            {'no': 'no', 'volumes': [consts.string.types.REAL]},
            {'no': 'no', 'volumes': [3.1]},
            {'no': pymcnp.types.String('no'), 'volumes': [consts.ast.types.REAL]},
            {'no': None, 'volumes': [consts.string.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'no': 'no', 'volumes': None}, {'no': 'hello', 'volumes': [consts.string.types.REAL]}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Vol
        EXAMPLES_VALID = [consts.string.inp.VOL]
        EXAMPLES_INVALID = ['hello']
