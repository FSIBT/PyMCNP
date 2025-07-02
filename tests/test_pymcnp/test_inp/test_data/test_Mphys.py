import pymcnp
from .... import consts
from .... import classes


class Test_Mphys:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Mphys
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('off')}, {'setting': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Mphys
        EXAMPLES_VALID = [consts.string.inp.data.MPHYS]
        EXAMPLES_INVALID = ['hello']


class Test_MphysBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.MphysBuilder
        EXAMPLES_VALID = [{'setting': 'off'}, {'setting': pymcnp.types.String('off')}, {'setting': None}]
        EXAMPLES_INVALID = [{'setting': 'hello'}]
