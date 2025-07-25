import pymcnp
from ..... import consts
from ..... import classes


class Test_Ext:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Ext
        EXAMPLES_VALID = [{'number': consts.string.types.DISTRIBUTION}, {'number': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Ext
        EXAMPLES_VALID = [consts.string.inp.data.ssr.EXT]
        EXAMPLES_INVALID = ['hello']
