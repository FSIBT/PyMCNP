import pymcnp
from .... import _utils


class Test_Subtitle:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Subtitle
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.SubtitleBuilder
        EXAMPLES_VALID = [
            {'x': _utils.string.type.INTEGER, 'y': _utils.string.type.INTEGER, 'aa': _utils.string.type.STRING},
            {'x': 1, 'y': 1, 'aa': _utils.string.type.STRING},
            {'x': _utils.ast.type.INTEGER, 'y': _utils.ast.type.INTEGER, 'aa': _utils.ast.type.STRING},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': _utils.string.type.INTEGER, 'aa': _utils.string.type.STRING},
            {'x': _utils.string.type.INTEGER, 'y': None, 'aa': _utils.string.type.STRING},
            {'x': _utils.string.type.INTEGER, 'y': _utils.string.type.INTEGER, 'aa': None},
        ]
