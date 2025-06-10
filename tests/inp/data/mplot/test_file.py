import pymcnp
from .... import _utils


class Test_File:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mplot.File
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mplot.FileBuilder
        EXAMPLES_VALID = [{'aa': 'all'}, {'aa': pymcnp.utils.types.String('all')}, {'aa': None}]
        EXAMPLES_INVALID = [{'aa': 'hello'}]
