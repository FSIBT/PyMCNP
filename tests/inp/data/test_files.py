import pymcnp
from ... import _utils


class Test_Files:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Files
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.FilesBuilder
        EXAMPLES_VALID = [{'creations': [_utils.string.type.FILE]}, {'creations': [_utils.ast.type.FILE]}]
        EXAMPLES_INVALID = [{'creations': None}]
