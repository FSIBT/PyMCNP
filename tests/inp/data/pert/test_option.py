import pymcnp
from .... import _utils


class Test_Cell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Cell
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.pert.CellBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]


class Test_Mat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Mat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.pert.MatBuilder
        EXAMPLES_VALID = [{'material': '1'}, {'material': 1}, {'material': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'material': None}]


class Test_Rho:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Rho
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.pert.RhoBuilder
        EXAMPLES_VALID = [{'density': '1.0'}, {'density': 1.0}, {'density': _utils.REAL}]
        EXAMPLES_INVALID = [{'density': None}]


class Test_Method:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Method
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.pert.MethodBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Erg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.pert.ErgBuilder
        EXAMPLES_VALID = [
            {'energy_lower_bound': '1.0', 'energy_upper_bound': '1.0'},
            {'energy_lower_bound': 1.0, 'energy_upper_bound': 1.0},
            {'energy_lower_bound': _utils.REAL, 'energy_upper_bound': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'energy_lower_bound': None, 'energy_upper_bound': '1.0'},
            {'energy_lower_bound': '1.0', 'energy_upper_bound': None},
        ]


class Test_Rxn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Rxn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.pert.RxnBuilder
        EXAMPLES_VALID = [{'numbers': ['1']}, {'numbers': [1]}, {'numbers': [_utils.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]
