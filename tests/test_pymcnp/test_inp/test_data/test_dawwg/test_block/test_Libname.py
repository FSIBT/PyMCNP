import pymcnp
from ...... import consts
from ...... import classes


class Test_Libname:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Libname
        EXAMPLES_VALID = [{'setting': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Libname
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.LIBNAME]
        EXAMPLES_INVALID = ['hello']


class Test_LibnameBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.LibnameBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.STRING}, {'setting': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'setting': None}]
