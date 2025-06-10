import pymcnp
from ... import _utils


class Test_Kpert:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Kpert
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.KpertBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'options': [_utils.string.inp.data.kpert.CELL]},
            {'suffix': 1, 'options': [_utils.builder.inp.data.kpert.CELL]},
            {'suffix': _utils.ast.type.INTEGER, 'options': [_utils.ast.inp.data.kpert.CELL]},
            {'suffix': _utils.string.type.INTEGER, 'options': None},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [_utils.string.inp.data.kpert.CELL]}]
