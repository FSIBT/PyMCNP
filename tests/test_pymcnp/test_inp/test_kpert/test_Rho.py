import pymcnp
from .... import consts
from .... import classes


class Test_Rho:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kpert.Rho
        EXAMPLES_VALID = [{'densities': [consts.string.types.REAL]}, {'densities': [3.1]}, {'densities': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'densities': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kpert.Rho
        EXAMPLES_VALID = [consts.string.inp.kpert.RHO]
        EXAMPLES_INVALID = ['hello']
