import pymcnp
from ..... import consts
from ..... import classes


class Test_Enorm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Enorm
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Enorm
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.ENORM]
        EXAMPLES_INVALID = ['hello']


class Test_EnormBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmesh.EnormBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
