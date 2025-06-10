import pymcnp
from .... import _utils


class Test_Genxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.tropt.Genxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.tropt.GenxsBuilder
        EXAMPLES_VALID = [{'filename': _utils.string.type.STRING}, {'filename': _utils.ast.type.STRING}, {'filename': None}]
        EXAMPLES_INVALID = []
