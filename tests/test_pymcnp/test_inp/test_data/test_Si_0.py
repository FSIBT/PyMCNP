import pymcnp
from .... import consts
from .... import classes


class Test_Si_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Si_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'option': consts.string.type.STRING, 'information': [consts.string.type.DISTRIBUTIONNUMBER]},
            {'suffix': 1, 'option': consts.string.type.STRING, 'information': [consts.string.type.DISTRIBUTIONNUMBER]},
            {'suffix': consts.ast.type.INTEGER, 'option': consts.ast.type.STRING, 'information': [consts.ast.type.DISTRIBUTIONNUMBER]},
            {'suffix': consts.string.type.INTEGER, 'option': None, 'information': [consts.string.type.DISTRIBUTIONNUMBER]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': consts.string.type.STRING, 'information': [consts.string.type.DISTRIBUTIONNUMBER]},
            {'suffix': consts.string.type.INTEGER, 'option': consts.string.type.STRING, 'information': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Si_0
        EXAMPLES_VALID = [consts.string.inp.data.SI_0]
        EXAMPLES_INVALID = ['hello']
