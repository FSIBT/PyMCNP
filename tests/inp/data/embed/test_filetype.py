import pymcnp
from .... import _utils


class Test_Filetype:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Filetype
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.FiletypeBuilder
        EXAMPLES_VALID = [{'kind': 'ascii'}, {'kind': pymcnp.utils.types.String('ascii')}]
        EXAMPLES_INVALID = [{'kind': None}, {'kind': 'hello'}]
