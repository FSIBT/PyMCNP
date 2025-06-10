import pymcnp
from ... import _utils


class Test_Fill_5:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_5
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FillBuilder_5
        EXAMPLES_VALID = [
            {'prefix': '*', 'universe': _utils.string.type.INTEGER, 'transformation': _utils.string.type.TRANSFORMATION_4},
            {'prefix': '*', 'universe': 1, 'transformation': _utils.string.type.TRANSFORMATION_4},
            {'prefix': pymcnp.utils.types.String('*'), 'universe': _utils.ast.type.INTEGER, 'transformation': _utils.ast.type.TRANSFORMATION_4},
            {'prefix': None, 'universe': _utils.string.type.INTEGER, 'transformation': _utils.string.type.TRANSFORMATION_4},
            {'prefix': '*', 'universe': _utils.string.type.INTEGER, 'transformation': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'universe': None, 'transformation': _utils.string.type.TRANSFORMATION_4},
            {'prefix': 'hello', 'universe': _utils.string.type.INTEGER, 'transformation': _utils.string.type.TRANSFORMATION_4},
        ]
