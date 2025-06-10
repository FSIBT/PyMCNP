import pymcnp
from ... import _utils


class Test_Awtab:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Awtab
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.AwtabBuilder
        EXAMPLES_VALID = [{'weight_ratios': [_utils.string.type.SUBSTANCE]}, {'weight_ratios': [_utils.ast.type.SUBSTANCE]}]
        EXAMPLES_INVALID = [{'weight_ratios': None}]
