import pymcnp
from ... import _utils


class Test_Pd:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Pd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.PdBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'probability': '0.8'},
            {'suffix': 1, 'probability': 0.8},
            {'suffix': _utils.ast.type.INTEGER, 'probability': pymcnp.utils.types.Real(0.8)},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'probability': '0.8'}, {'suffix': _utils.string.type.INTEGER, 'probability': None}, {'suffix': _utils.string.type.INTEGER, 'probability': '3.1'}]
