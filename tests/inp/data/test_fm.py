import pymcnp
from ... import _utils


class Test_Fm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FmBuilder
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'bins': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': 1, 'bins': _utils.string.type.STRING},
            {'prefix': pymcnp.utils.types.String('*'), 'suffix': _utils.ast.type.INTEGER, 'bins': _utils.ast.type.STRING},
            {'prefix': None, 'suffix': _utils.string.type.INTEGER, 'bins': _utils.string.type.STRING},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'bins': _utils.string.type.STRING},
            {'prefix': '*', 'suffix': _utils.string.type.INTEGER, 'bins': None},
            {'prefix': 'hello', 'suffix': _utils.string.type.INTEGER, 'bins': _utils.string.type.STRING},
        ]
