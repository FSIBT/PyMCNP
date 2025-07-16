import pymcnp
from ...... import consts
from ...... import classes


class Test_Libname:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Libname
        EXAMPLES_VALID = [{'setting': consts.string.types.STRING}, {'setting': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Libname
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.LIBNAME]
        EXAMPLES_INVALID = ['hello']
