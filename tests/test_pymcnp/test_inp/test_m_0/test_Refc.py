import pymcnp
from .... import consts
from .... import classes


class Test_Refc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.m_0.Refc
        EXAMPLES_VALID = [{'coefficents': [consts.string.types.REAL]}, {'coefficents': [3.1]}, {'coefficents': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'coefficents': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.m_0.Refc
        EXAMPLES_VALID = [consts.string.inp.m_0.REFC]
        EXAMPLES_INVALID = ['hello']
