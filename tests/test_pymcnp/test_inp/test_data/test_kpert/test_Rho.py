import pymcnp
from ..... import consts
from ..... import classes


class Test_Rho:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kpert.Rho
        EXAMPLES_VALID = [{'densities': [consts.string.type.REAL]}, {'densities': [3.1]}, {'densities': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'densities': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kpert.Rho
        EXAMPLES_VALID = [consts.string.inp.data.kpert.RHO]
        EXAMPLES_INVALID = ['hello']
