import pymcnp
from .... import _utils


class Test_Rho:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kpert.Rho
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kpert.RhoBuilder
        EXAMPLES_VALID = [{'densities': [_utils.string.type.REAL]}, {'densities': [3.1]}, {'densities': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'densities': None}]
