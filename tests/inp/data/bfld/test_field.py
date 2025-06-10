import pymcnp
from .... import _utils


class Test_Field:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.bfld.Field
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.bfld.FieldBuilder
        EXAMPLES_VALID = [{'strength_gradient': _utils.string.type.REAL}, {'strength_gradient': 3.1}, {'strength_gradient': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'strength_gradient': None}]
