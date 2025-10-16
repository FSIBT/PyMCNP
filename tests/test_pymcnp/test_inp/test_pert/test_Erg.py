import pymcnp
from .... import consts
from .... import classes


class Test_Erg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.pert.Erg
        EXAMPLES_VALID = [
            {'energy_lower_bound': consts.string.types.REAL, 'energy_upper_bound': consts.string.types.REAL},
            {'energy_lower_bound': 3.1, 'energy_upper_bound': 3.1},
            {'energy_lower_bound': consts.ast.types.REAL, 'energy_upper_bound': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [{'energy_lower_bound': None, 'energy_upper_bound': consts.string.types.REAL}, {'energy_lower_bound': consts.string.types.REAL, 'energy_upper_bound': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.pert.Erg
        EXAMPLES_VALID = [consts.string.inp.pert.ERG]
        EXAMPLES_INVALID = ['hello']
