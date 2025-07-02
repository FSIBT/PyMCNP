import pymcnp
from ..... import consts
from ..... import classes


class Test_Tnorm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Tnorm
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Tnorm
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.TNORM]
        EXAMPLES_INVALID = ['hello']


class Test_TnormBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmesh.TnormBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
