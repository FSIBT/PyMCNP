import pymcnp
from ... import _utils


class Test_Si_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Si_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SiBuilder_0
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'option': _utils.string.type.STRING, 'information': [_utils.string.type.DISTRIBUTIONNUMBER]},
            {'suffix': 1, 'option': _utils.string.type.STRING, 'information': [_utils.string.type.DISTRIBUTIONNUMBER]},
            {'suffix': _utils.ast.type.INTEGER, 'option': _utils.ast.type.STRING, 'information': [_utils.ast.type.DISTRIBUTIONNUMBER]},
            {'suffix': _utils.string.type.INTEGER, 'option': None, 'information': [_utils.string.type.DISTRIBUTIONNUMBER]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': _utils.string.type.STRING, 'information': [_utils.string.type.DISTRIBUTIONNUMBER]},
            {'suffix': _utils.string.type.INTEGER, 'option': _utils.string.type.STRING, 'information': None},
        ]
