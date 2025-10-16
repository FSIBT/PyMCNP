import pymcnp
from .... import consts
from .... import classes


class Test_Nps:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.Nps
        EXAMPLES_VALID = [{'particles': [consts.string.types.INTEGER]}, {'particles': [1]}, {'particles': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'particles': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.Nps
        EXAMPLES_VALID = [consts.string.inp.ptrac.NPS]
        EXAMPLES_INVALID = ['hello']
