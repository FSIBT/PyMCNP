import pymcnp
from ..... import consts
from ..... import classes


class Test_Refs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.m_0.Refs
        EXAMPLES_VALID = [{'coefficents': [consts.string.types.REAL]}, {'coefficents': [3.1]}, {'coefficents': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'coefficents': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.m_0.Refs
        EXAMPLES_VALID = [consts.string.inp.data.m_0.REFS]
        EXAMPLES_INVALID = ['hello']
