import pymcnp
from ..... import consts
from ..... import classes


class Test_Mtype:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embee.Mtype
        EXAMPLES_VALID = [{'kind': pymcnp.types.String('flux')}]
        EXAMPLES_INVALID = [{'kind': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embee.Mtype
        EXAMPLES_VALID = [consts.string.inp.data.embee.MTYPE]
        EXAMPLES_INVALID = ['hello']


class Test_MtypeBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.embee.MtypeBuilder
        EXAMPLES_VALID = [{'kind': 'flux'}, {'kind': pymcnp.types.String('flux')}]
        EXAMPLES_INVALID = [{'kind': None}, {'kind': 'hello'}]
