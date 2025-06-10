import pymcnp
from .... import _utils


class Test_Debug:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Debug
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.DebugBuilder
        EXAMPLES_VALID = [{'parameter': 'echomesh'}, {'parameter': pymcnp.utils.types.String('echomesh')}]
        EXAMPLES_INVALID = [{'parameter': None}, {'parameter': 'hello'}]
