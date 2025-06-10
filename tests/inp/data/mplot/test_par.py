import pymcnp
from .... import _utils


class Test_Par:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Par
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ParBuilder
        EXAMPLES_VALID = [{'particle': _utils.string.type.DESIGNATOR}, {'particle': _utils.ast.type.DESIGNATOR}]
        EXAMPLES_INVALID = [{'particle': None}]
