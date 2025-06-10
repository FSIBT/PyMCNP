import pymcnp
from .... import _utils


class Test_Nrm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Nrm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.NrmBuilder
        EXAMPLES_VALID = [{'sign': _utils.string.type.INTEGER}, {'sign': 1}, {'sign': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'sign': None}]
