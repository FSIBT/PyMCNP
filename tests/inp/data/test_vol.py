import pymcnp
from ... import _utils


class Test_Vol:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Vol
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.VolBuilder
        EXAMPLES_VALID = [
            {'no': 'no', 'volumes': [_utils.string.type.REAL]},
            {'no': 'no', 'volumes': [3.1]},
            {'no': pymcnp.utils.types.String('no'), 'volumes': [_utils.ast.type.REAL]},
            {'no': None, 'volumes': [_utils.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'no': 'no', 'volumes': None}, {'no': 'hello', 'volumes': [_utils.string.type.REAL]}]
