import pymcnp
from .... import _utils


class Test_Dat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.sdef.Dat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.sdef.DatBuilder
        EXAMPLES_VALID = [
            {'month': _utils.string.type.INTEGER, 'day': _utils.string.type.INTEGER, 'year': _utils.string.type.INTEGER},
            {'month': 1, 'day': 1, 'year': 1},
            {'month': _utils.ast.type.INTEGER, 'day': _utils.ast.type.INTEGER, 'year': _utils.ast.type.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'month': None, 'day': _utils.string.type.INTEGER, 'year': _utils.string.type.INTEGER},
            {'month': _utils.string.type.INTEGER, 'day': None, 'year': _utils.string.type.INTEGER},
            {'month': _utils.string.type.INTEGER, 'day': _utils.string.type.INTEGER, 'year': None},
        ]
