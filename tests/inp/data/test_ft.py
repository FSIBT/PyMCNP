import pymcnp
from ... import _utils


class Test_Ft:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ft
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FtBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'treatments': _utils.string.type.STRING},
            {'suffix': 1, 'treatments': _utils.string.type.STRING},
            {'suffix': _utils.ast.type.INTEGER, 'treatments': _utils.ast.type.STRING},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'treatments': _utils.string.type.STRING}, {'suffix': _utils.string.type.INTEGER, 'treatments': None}]
