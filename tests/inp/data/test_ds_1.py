import pymcnp
from ... import _utils


class Test_Ds_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ds_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.DsBuilder_1
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'ijs': [_utils.string.type.INDEPENDENTDEPENDENT]},
            {'suffix': 1, 'ijs': [_utils.string.type.INDEPENDENTDEPENDENT]},
            {'suffix': _utils.ast.type.INTEGER, 'ijs': [_utils.ast.type.INDEPENDENTDEPENDENT]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'ijs': [_utils.string.type.INDEPENDENTDEPENDENT]}, {'suffix': _utils.string.type.INTEGER, 'ijs': None}]
