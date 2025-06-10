import pymcnp
from ..... import _utils


class Test_Trcor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Trcor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.TrcorBuilder
        EXAMPLES_VALID = [{'setting': 'diag'}, {'setting': pymcnp.utils.types.String('diag')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
