import pymcnp
from ... import _utils


class Test_Leb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Leb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.LebBuilder
        EXAMPLES_VALID = [
            {'yzere': _utils.string.type.REAL, 'bzere': _utils.string.type.REAL, 'yzero': _utils.string.type.REAL, 'bzero': _utils.string.type.REAL},
            {'yzere': 3.1, 'bzere': 3.1, 'yzero': 3.1, 'bzero': 3.1},
            {'yzere': _utils.ast.type.REAL, 'bzere': _utils.ast.type.REAL, 'yzero': _utils.ast.type.REAL, 'bzero': _utils.ast.type.REAL},
            {'yzere': None, 'bzere': _utils.string.type.REAL, 'yzero': _utils.string.type.REAL, 'bzero': _utils.string.type.REAL},
            {'yzere': _utils.string.type.REAL, 'bzere': None, 'yzero': _utils.string.type.REAL, 'bzero': _utils.string.type.REAL},
            {'yzere': _utils.string.type.REAL, 'bzere': _utils.string.type.REAL, 'yzero': None, 'bzero': _utils.string.type.REAL},
            {'yzere': _utils.string.type.REAL, 'bzere': _utils.string.type.REAL, 'yzero': _utils.string.type.REAL, 'bzero': None},
        ]
        EXAMPLES_INVALID = [
            {'yzere': -3.1, 'bzere': _utils.string.type.REAL, 'yzero': _utils.string.type.REAL, 'bzero': _utils.string.type.REAL},
            {'yzere': _utils.string.type.REAL, 'bzere': -3.1, 'yzero': _utils.string.type.REAL, 'bzero': _utils.string.type.REAL},
            {'yzere': _utils.string.type.REAL, 'bzere': _utils.string.type.REAL, 'yzero': -3.1, 'bzero': _utils.string.type.REAL},
            {'yzere': _utils.string.type.REAL, 'bzere': _utils.string.type.REAL, 'yzero': _utils.string.type.REAL, 'bzero': -3.1},
        ]
