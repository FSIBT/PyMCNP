import pymcnp
from .... import consts
from .... import classes


class Test_Ext_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Ext_1
        EXAMPLES_VALID = [{'distance_cosine': consts.string.types.DISTRIBUTION}, {'distance_cosine': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'distance_cosine': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Ext_1
        EXAMPLES_VALID = [consts.string.inp.sdef.EXT_1]
        EXAMPLES_INVALID = ['hello']
