import pymcnp
from ... import _utils


class Test_Ds_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ds_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.DsBuilder_2
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'vss': [_utils.string.type.INDEPENDENTDEPENDENT]},
            {'suffix': 1, 'vss': [_utils.string.type.INDEPENDENTDEPENDENT]},
            {'suffix': _utils.ast.type.INTEGER, 'vss': [_utils.ast.type.INDEPENDENTDEPENDENT]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'vss': [_utils.string.type.INDEPENDENTDEPENDENT]}, {'suffix': _utils.string.type.INTEGER, 'vss': None}]
