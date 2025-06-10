import pymcnp
from ... import _utils


class Test_Sb_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Sb_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SbBuilder_1
        EXAMPLES_VALID = [
            {'function': '-2', 'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL},
            {'function': -2, 'a': 3.1, 'b': 3.1},
            {'function': pymcnp.utils.types.Integer(-2), 'a': _utils.ast.type.REAL, 'b': _utils.ast.type.REAL},
            {'function': '-2', 'a': _utils.string.type.REAL, 'b': None},
        ]
        EXAMPLES_INVALID = [
            {'function': None, 'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL},
            {'function': '-2', 'a': None, 'b': _utils.string.type.REAL},
            {'function': '1', 'a': _utils.string.type.REAL, 'b': _utils.string.type.REAL},
        ]
