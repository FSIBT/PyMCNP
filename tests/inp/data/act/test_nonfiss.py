import pymcnp
from .... import _utils


class Test_Nonfiss:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.act.Nonfiss
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.act.NonfissBuilder
        EXAMPLES_VALID = [{'kind': _utils.string.type.STRING}, {'kind': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'kind': None}]
