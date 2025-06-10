import pymcnp
from .... import _utils


class Test_Erg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ksen.Erg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ksen.ErgBuilder
        EXAMPLES_VALID = [{'energies': [_utils.string.type.REAL]}, {'energies': [3.1]}, {'energies': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]
