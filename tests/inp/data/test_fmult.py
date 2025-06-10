import pymcnp
from ... import _utils


class Test_Fmult:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fmult
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FmultBuilder
        EXAMPLES_VALID = [
            {'zaid': _utils.string.type.ZAID, 'options': [_utils.string.inp.data.fmult.DATA]},
            {'zaid': _utils.string.type.ZAID, 'options': [_utils.builder.inp.data.fmult.DATA]},
            {'zaid': _utils.ast.type.ZAID, 'options': [_utils.ast.inp.data.fmult.DATA]},
            {'zaid': _utils.string.type.ZAID, 'options': None},
        ]
        EXAMPLES_INVALID = [{'zaid': None, 'options': [_utils.string.inp.data.fmult.DATA]}]
