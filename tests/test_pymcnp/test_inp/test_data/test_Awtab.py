import pymcnp
from .... import consts
from .... import classes


class Test_Awtab:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Awtab
        EXAMPLES_VALID = [{'weight_ratios': [consts.string.types.SUBSTANCE]}, {'weight_ratios': [consts.ast.types.SUBSTANCE]}]
        EXAMPLES_INVALID = [{'weight_ratios': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Awtab
        EXAMPLES_VALID = [consts.string.inp.data.AWTAB]
        EXAMPLES_INVALID = ['hello']
