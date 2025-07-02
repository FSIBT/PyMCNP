import pymcnp
from ..... import consts
from ..... import classes


class Test_Constrain:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ksen.Constrain
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ksen.Constrain
        EXAMPLES_VALID = [consts.string.inp.data.ksen.CONSTRAIN]
        EXAMPLES_INVALID = ['hello']


class Test_ConstrainBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ksen.ConstrainBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
