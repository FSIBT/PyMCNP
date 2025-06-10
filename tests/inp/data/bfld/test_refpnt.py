import pymcnp
from .... import _utils


class Test_Refpnt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Refpnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.RefpntBuilder
        EXAMPLES_VALID = [{'point': [_utils.string.type.REAL]}, {'point': [3.1]}, {'point': [_utils.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'point': None}]
