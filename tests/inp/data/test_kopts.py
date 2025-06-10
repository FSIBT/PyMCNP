import pymcnp
from ... import _utils


class Test_Kopts:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Kopts
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.KoptsBuilder
        EXAMPLES_VALID = [
            {'options': [_utils.string.inp.data.kopts.BLOCKSIZE]},
            {'options': [_utils.builder.inp.data.kopts.BLOCKSIZE]},
            {'options': [_utils.ast.inp.data.kopts.BLOCKSIZE]},
            {'options': None},
        ]
        EXAMPLES_INVALID = []
