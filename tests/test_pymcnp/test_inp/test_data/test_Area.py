import pymcnp
from .... import consts
from .... import classes


class Test_Area:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Area
        EXAMPLES_VALID = [{'areas': [consts.string.types.REAL]}, {'areas': [3.1]}, {'areas': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'areas': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Area
        EXAMPLES_VALID = [consts.string.inp.data.AREA]
        EXAMPLES_INVALID = ['hello']
