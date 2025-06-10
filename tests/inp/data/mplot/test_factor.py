import pymcnp
from .... import _utils


class Test_Factor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FactorBuilder
        EXAMPLES_VALID = [
            {'a': 'x', 'f': _utils.string.type.REAL, 's': _utils.string.type.REAL},
            {'a': 'x', 'f': 3.1, 's': 3.1},
            {'a': pymcnp.utils.types.String('x'), 'f': _utils.ast.type.REAL, 's': _utils.ast.type.REAL},
            {'a': 'x', 'f': _utils.string.type.REAL, 's': None},
        ]
        EXAMPLES_INVALID = [
            {'a': None, 'f': _utils.string.type.REAL, 's': _utils.string.type.REAL},
            {'a': 'x', 'f': None, 's': _utils.string.type.REAL},
            {'a': 'hello', 'f': _utils.string.type.REAL, 's': _utils.string.type.REAL},
        ]
