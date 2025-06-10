import pymcnp
from ... import _utils


class Test_Xs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Xs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.XsBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'weight_ratios': [_utils.string.type.SUBSTANCE]},
            {'suffix': 1, 'weight_ratios': [_utils.string.type.SUBSTANCE]},
            {'suffix': _utils.ast.type.INTEGER, 'weight_ratios': [_utils.ast.type.SUBSTANCE]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'weight_ratios': [_utils.string.type.SUBSTANCE]}, {'suffix': _utils.string.type.INTEGER, 'weight_ratios': None}]
