import pymcnp
from .... import _utils


class Test_Jints:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Jints
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.JintsBuilder
        EXAMPLES_VALID = [{'number': [_utils.string.type.INTEGER]}, {'number': [1]}, {'number': [_utils.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'number': None}]
