import pymcnp
from ..... import consts
from ..... import classes


class Test_Eloss:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.tropt.Eloss
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('off')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.tropt.Eloss
        EXAMPLES_VALID = [consts.string.inp.data.tropt.ELOSS]
        EXAMPLES_INVALID = ['hello']


class Test_ElossBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.tropt.ElossBuilder
        EXAMPLES_VALID = [{'setting': 'off'}, {'setting': pymcnp.types.String('off')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
