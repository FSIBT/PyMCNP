import pymcnp
from ...... import consts
from ...... import classes


class Test_Trcor:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Trcor
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('diag')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Trcor
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.TRCOR]
        EXAMPLES_INVALID = ['hello']


class Test_TrcorBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.TrcorBuilder
        EXAMPLES_VALID = [{'setting': 'diag'}, {'setting': pymcnp.types.String('diag')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
