import pymcnp
from .... import _utils


class Test_Blocksize:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Blocksize
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.BlocksizeBuilder
        EXAMPLES_VALID = [{'ncy': '99'}, {'ncy': 99}, {'ncy': pymcnp.utils.types.Integer(99)}]
        EXAMPLES_INVALID = [{'ncy': None}, {'ncy': '1'}]
