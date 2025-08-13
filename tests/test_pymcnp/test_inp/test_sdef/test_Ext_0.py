import pymcnp
from .... import consts
from .... import classes


class Test_Ext_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Ext_0
        EXAMPLES_VALID = [{'distance_cosine': consts.string.types.REAL}, {'distance_cosine': 3.1}, {'distance_cosine': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'distance_cosine': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Ext_0
        EXAMPLES_VALID = [consts.string.inp.sdef.EXT_0]
        EXAMPLES_INVALID = ['hello']
