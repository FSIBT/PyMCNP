import pymcnp
from .... import _utils


class Test_Erg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.pert.ErgBuilder
        EXAMPLES_VALID = [
            {'energy_lower_bound': _utils.string.type.REAL, 'energy_upper_bound': _utils.string.type.REAL},
            {'energy_lower_bound': 3.1, 'energy_upper_bound': 3.1},
            {'energy_lower_bound': _utils.ast.type.REAL, 'energy_upper_bound': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [{'energy_lower_bound': None, 'energy_upper_bound': _utils.string.type.REAL}, {'energy_lower_bound': _utils.string.type.REAL, 'energy_upper_bound': None}]
