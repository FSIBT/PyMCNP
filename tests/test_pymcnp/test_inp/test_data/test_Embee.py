import pymcnp
from .... import consts
from .... import classes


class Test_Embee:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Embee
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'options': [consts.string.inp.data.embee.ATOM]},
            {'suffix': 1, 'designator': consts.string.types.DESIGNATOR, 'options': [consts.ast.inp.data.embee.ATOM]},
            {'suffix': consts.ast.types.INTEGER, 'designator': consts.ast.types.DESIGNATOR, 'options': [consts.ast.inp.data.embee.ATOM]},
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'options': [consts.string.inp.data.embee.ATOM]},
            {'suffix': consts.string.types.INTEGER, 'designator': None, 'options': [consts.string.inp.data.embee.ATOM]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Embee
        EXAMPLES_VALID = [consts.string.inp.data.EMBEE]
        EXAMPLES_INVALID = ['hello']
