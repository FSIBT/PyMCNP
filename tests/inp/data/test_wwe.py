import pymcnp
from ... import _utils


class Test_Wwe:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwe
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.WweBuilder
        EXAMPLES_VALID = [
            {'designator': _utils.string.type.DESIGNATOR, 'bounds': [_utils.string.type.REAL]},
            {'designator': _utils.string.type.DESIGNATOR, 'bounds': [3.1]},
            {'designator': _utils.ast.type.DESIGNATOR, 'bounds': [_utils.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'bounds': [_utils.string.type.REAL]}, {'designator': _utils.string.type.DESIGNATOR, 'bounds': None}]
