import pymcnp
from .... import _utils


class Test_Title:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Title
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.TitleBuilder
        EXAMPLES_VALID = [{'n': _utils.string.type.INTEGER, 'aa': _utils.string.type.STRING}, {'n': 1, 'aa': _utils.string.type.STRING}, {'n': _utils.ast.type.INTEGER, 'aa': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'n': None, 'aa': _utils.string.type.STRING}, {'n': _utils.string.type.INTEGER, 'aa': None}]
