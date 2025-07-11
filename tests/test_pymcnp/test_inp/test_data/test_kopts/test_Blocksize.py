import pymcnp
from ..... import consts
from ..... import classes


class Test_Blocksize:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kopts.Blocksize
        EXAMPLES_VALID = [{'ncy': '99'}, {'ncy': 99}, {'ncy': pymcnp.types.Integer(99)}]
        EXAMPLES_INVALID = [{'ncy': None}, {'ncy': '1'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kopts.Blocksize
        EXAMPLES_VALID = [consts.string.inp.data.kopts.BLOCKSIZE]
        EXAMPLES_INVALID = ['hello']
