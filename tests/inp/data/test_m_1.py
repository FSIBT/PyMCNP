import pymcnp
from ... import _utils


class Test_M_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.M_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.MBuilder_1
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'abx': _utils.string.type.STRING},
            {'suffix': 1, 'abx': _utils.string.type.STRING},
            {'suffix': _utils.ast.type.INTEGER, 'abx': _utils.ast.type.STRING},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'abx': _utils.string.type.STRING}, {'suffix': _utils.string.type.INTEGER, 'abx': None}]
