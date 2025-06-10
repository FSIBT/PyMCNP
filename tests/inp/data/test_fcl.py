import pymcnp
from ... import _utils


class Test_Fcl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fcl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FclBuilder
        EXAMPLES_VALID = [
            {'designator': _utils.string.type.DESIGNATOR, 'control': [_utils.string.type.REAL]},
            {'designator': _utils.string.type.DESIGNATOR, 'control': [3.1]},
            {'designator': _utils.ast.type.DESIGNATOR, 'control': [_utils.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'control': [_utils.string.type.REAL]}, {'designator': _utils.string.type.DESIGNATOR, 'control': None}]
