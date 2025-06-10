import pymcnp
from .... import _utils


class Test_Free:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.Free
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FreeBuilder
        EXAMPLES_VALID = [
            {'x': 't', 'y': 't', 'option': _utils.string.inp.data.mplot.free.ALL},
            {'x': 't', 'y': 't', 'option': _utils.builder.inp.data.mplot.free.ALL},
            {'x': pymcnp.utils.types.String('t'), 'y': pymcnp.utils.types.String('t'), 'option': _utils.ast.inp.data.mplot.free.ALL},
            {'x': 't', 'y': 't', 'option': None},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': 't', 'option': _utils.string.inp.data.mplot.free.ALL},
            {'x': 't', 'y': None, 'option': _utils.string.inp.data.mplot.free.ALL},
            {'x': 'hello', 'y': 't', 'option': _utils.string.inp.data.mplot.free.ALL},
            {'x': 't', 'y': 'hello', 'option': _utils.string.inp.data.mplot.free.ALL},
        ]
