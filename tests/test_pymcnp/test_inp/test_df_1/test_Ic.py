import pymcnp
from .... import consts
from .... import classes


class Test_Ic:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.df_1.Ic
        EXAMPLES_VALID = [{'function': '99'}, {'function': 99}, {'function': pymcnp.types.Integer(99)}]
        EXAMPLES_INVALID = [{'function': None}, {'function': '1'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.df_1.Ic
        EXAMPLES_VALID = [consts.string.inp.df_1.IC]
        EXAMPLES_INVALID = ['hello']
