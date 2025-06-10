import pymcnp
from .... import _utils


class Test_Ic:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.df_1.Ic
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.df_1.IcBuilder
        EXAMPLES_VALID = [{'function': '99'}, {'function': 99}, {'function': pymcnp.utils.types.Integer(99)}]
        EXAMPLES_INVALID = [{'function': None}, {'function': '1'}]
