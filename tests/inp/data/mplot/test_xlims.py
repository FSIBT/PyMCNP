import pymcnp
from .... import _utils


class Test_Xlims:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Xlims
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.XlimsBuilder
        EXAMPLES_VALID = [
            {'lower': '0.8', 'upper': _utils.string.type.REAL, 'nsteps': _utils.string.type.REAL},
            {'lower': 0.8, 'upper': 3.1, 'nsteps': 3.1},
            {'lower': pymcnp.utils.types.Real(0.8), 'upper': _utils.ast.type.REAL, 'nsteps': _utils.ast.type.REAL},
            {'lower': '0.8', 'upper': _utils.string.type.REAL, 'nsteps': None},
        ]
        EXAMPLES_INVALID = [
            {'lower': None, 'upper': _utils.string.type.REAL, 'nsteps': _utils.string.type.REAL},
            {'lower': '0.8', 'upper': None, 'nsteps': _utils.string.type.REAL},
            {'lower': '3.1', 'upper': _utils.string.type.REAL, 'nsteps': _utils.string.type.REAL},
            {'lower': '0.8', 'upper': _utils.string.type.REAL, 'nsteps': -3.1},
        ]
