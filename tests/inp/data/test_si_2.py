import pymcnp
from ... import _utils


class Test_Si_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Si_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SiBuilder_2
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'option': _utils.string.type.STRING, 'information': [_utils.string.type.DESIGNATOR]},
            {'suffix': 1, 'option': _utils.string.type.STRING, 'information': [_utils.string.type.DESIGNATOR]},
            {'suffix': _utils.ast.type.INTEGER, 'option': _utils.ast.type.STRING, 'information': [_utils.ast.type.DESIGNATOR]},
            {'suffix': _utils.string.type.INTEGER, 'option': None, 'information': [_utils.string.type.DESIGNATOR]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': _utils.string.type.STRING, 'information': [_utils.string.type.DESIGNATOR]},
            {'suffix': _utils.string.type.INTEGER, 'option': _utils.string.type.STRING, 'information': None},
        ]
