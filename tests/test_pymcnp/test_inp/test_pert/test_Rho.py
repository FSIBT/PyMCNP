import pymcnp
from .... import consts
from .... import classes


class Test_Rho:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.pert.Rho
        EXAMPLES_VALID = [{'density': consts.string.types.REAL}, {'density': 3.1}, {'density': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'density': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.pert.Rho
        EXAMPLES_VALID = [consts.string.inp.pert.RHO]
        EXAMPLES_INVALID = ['hello']
