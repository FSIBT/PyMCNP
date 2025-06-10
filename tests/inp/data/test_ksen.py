import pymcnp
from ... import _utils


class Test_Ksen:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ksen
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.KsenBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'sen': _utils.string.type.STRING, 'options': [_utils.string.inp.data.ksen.CONSTRAIN]},
            {'suffix': 1, 'sen': _utils.string.type.STRING, 'options': [_utils.builder.inp.data.ksen.CONSTRAIN]},
            {'suffix': _utils.ast.type.INTEGER, 'sen': _utils.ast.type.STRING, 'options': [_utils.ast.inp.data.ksen.CONSTRAIN]},
            {'suffix': _utils.string.type.INTEGER, 'sen': _utils.string.type.STRING, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'sen': _utils.string.type.STRING, 'options': [_utils.string.inp.data.ksen.CONSTRAIN]},
            {'suffix': _utils.string.type.INTEGER, 'sen': None, 'options': [_utils.string.inp.data.ksen.CONSTRAIN]},
        ]
