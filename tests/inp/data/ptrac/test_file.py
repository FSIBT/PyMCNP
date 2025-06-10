import pymcnp
from .... import _utils


class Test_File:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.ptrac.File
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ptrac.FileBuilder
        EXAMPLES_VALID = [{'setting': 'asc'}, {'setting': pymcnp.utils.types.String('asc')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
