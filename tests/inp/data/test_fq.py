import pymcnp
from ... import _utils


class Test_Fq:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Fq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FqBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': 1, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {
                'suffix': _utils.ast.type.INTEGER,
                'a1': pymcnp.utils.types.String('t'),
                'a2': pymcnp.utils.types.String('t'),
                'a3': pymcnp.utils.types.String('t'),
                'a4': pymcnp.utils.types.String('t'),
                'a5': pymcnp.utils.types.String('t'),
                'a6': pymcnp.utils.types.String('t'),
                'a7': pymcnp.utils.types.String('t'),
                'a8': pymcnp.utils.types.String('t'),
            },
            {'suffix': None, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': None, 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': None, 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': None, 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': None, 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': None, 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': None, 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': None, 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': 100000000, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 'hello', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 'hello', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 'hello', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 'hello', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 'hello', 'a6': 't', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 'hello', 'a7': 't', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 'hello', 'a8': 't'},
            {'suffix': _utils.string.type.INTEGER, 'a1': 't', 'a2': 't', 'a3': 't', 'a4': 't', 'a5': 't', 'a6': 't', 'a7': 't', 'a8': 'hello'},
        ]
