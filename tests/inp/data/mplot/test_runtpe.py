import pymcnp
from .... import _utils


class Test_Runtpe:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Runtpe
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.RuntpeBuilder
        EXAMPLES_VALID = [
            {'filename': _utils.string.type.STRING, 'n': _utils.string.type.INTEGER},
            {'filename': _utils.string.type.STRING, 'n': 1},
            {'filename': _utils.ast.type.STRING, 'n': _utils.ast.type.INTEGER},
            {'filename': _utils.string.type.STRING, 'n': None},
        ]
        EXAMPLES_INVALID = [{'filename': None, 'n': _utils.string.type.INTEGER}]
