import pymcnp
from .... import _utils


class Test_Rho:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.pert.Rho
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.pert.RhoBuilder
        EXAMPLES_VALID = [{'density': _utils.string.type.REAL}, {'density': 3.1}, {'density': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'density': None}]
