import pymcnp
from ..... import consts
from ..... import classes


class Test_Linear:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kpert.Linear
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kpert.Linear
        EXAMPLES_VALID = [consts.string.inp.data.kpert.LINEAR]
        EXAMPLES_INVALID = ['hello']


class Test_LinearBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.kpert.LinearBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
