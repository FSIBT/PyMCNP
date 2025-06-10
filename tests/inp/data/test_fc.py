import pymcnp
from ... import _utils


class Test_Fc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FcBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'info': _utils.string.type.STRING},
            {'suffix': 1, 'info': _utils.string.type.STRING},
            {'suffix': _utils.ast.type.INTEGER, 'info': _utils.ast.type.STRING},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'info': _utils.string.type.STRING}, {'suffix': _utils.string.type.INTEGER, 'info': None}]
