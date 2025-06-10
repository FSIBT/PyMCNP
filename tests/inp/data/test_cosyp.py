import pymcnp
from ... import _utils


class Test_Cosyp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Cosyp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.CosypBuilder
        EXAMPLES_VALID = [
            {'pre': _utils.string.type.INTEGER, 'axsh': _utils.string.type.INTEGER, 'axsv': _utils.string.type.INTEGER, 'emaps': [_utils.string.type.REAL]},
            {'pre': 1, 'axsh': 1, 'axsv': 1, 'emaps': [3.1]},
            {'pre': _utils.ast.type.INTEGER, 'axsh': _utils.ast.type.INTEGER, 'axsv': _utils.ast.type.INTEGER, 'emaps': [_utils.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'pre': None, 'axsh': _utils.string.type.INTEGER, 'axsv': _utils.string.type.INTEGER, 'emaps': [_utils.string.type.REAL]},
            {'pre': _utils.string.type.INTEGER, 'axsh': None, 'axsv': _utils.string.type.INTEGER, 'emaps': [_utils.string.type.REAL]},
            {'pre': _utils.string.type.INTEGER, 'axsh': _utils.string.type.INTEGER, 'axsv': None, 'emaps': [_utils.string.type.REAL]},
            {'pre': _utils.string.type.INTEGER, 'axsh': _utils.string.type.INTEGER, 'axsv': _utils.string.type.INTEGER, 'emaps': None},
        ]
