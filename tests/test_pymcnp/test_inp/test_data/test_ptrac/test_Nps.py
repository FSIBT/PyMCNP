import pymcnp
from ..... import consts
from ..... import classes


class Test_Nps:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.Nps
        EXAMPLES_VALID = [{'particles': [consts.string.type.INTEGER]}, {'particles': [1]}, {'particles': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'particles': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.Nps
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.NPS]
        EXAMPLES_INVALID = ['hello']
