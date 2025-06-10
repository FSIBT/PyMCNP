import pymcnp
from ... import _utils


class Test_Sf:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SfBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'numbers': [_utils.string.type.INTEGER]},
            {'suffix': 1, 'numbers': [1]},
            {'suffix': _utils.ast.type.INTEGER, 'numbers': [_utils.ast.type.INTEGER]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'numbers': [_utils.string.type.INTEGER]}, {'suffix': _utils.string.type.INTEGER, 'numbers': None}]
