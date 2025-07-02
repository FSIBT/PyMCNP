import pymcnp
from ...... import consts
from ...... import classes


class Test_Srcacc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Srcacc
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Srcacc
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.SRCACC]
        EXAMPLES_INVALID = ['hello']


class Test_SrcaccBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.SrcaccBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
