import pymcnp
from .... import _utils


class Test_Contour:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Contour
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.ContourBuilder
        EXAMPLES_VALID = [
            {'cmin': _utils.string.type.REAL, 'cmax': _utils.string.type.REAL, 'cstep': _utils.string.type.REAL, 'options': [_utils.string.inp.data.mplot.contour.ALL]},
            {'cmin': 3.1, 'cmax': 3.1, 'cstep': 3.1, 'options': [_utils.builder.inp.data.mplot.contour.ALL]},
            {'cmin': _utils.ast.type.REAL, 'cmax': _utils.ast.type.REAL, 'cstep': _utils.ast.type.REAL, 'options': [_utils.ast.inp.data.mplot.contour.ALL]},
            {'cmin': _utils.string.type.REAL, 'cmax': _utils.string.type.REAL, 'cstep': _utils.string.type.REAL, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'cmin': None, 'cmax': _utils.string.type.REAL, 'cstep': _utils.string.type.REAL, 'options': [_utils.string.inp.data.mplot.contour.ALL]},
            {'cmin': _utils.string.type.REAL, 'cmax': None, 'cstep': _utils.string.type.REAL, 'options': [_utils.string.inp.data.mplot.contour.ALL]},
            {'cmin': _utils.string.type.REAL, 'cmax': _utils.string.type.REAL, 'cstep': None, 'options': [_utils.string.inp.data.mplot.contour.ALL]},
        ]
