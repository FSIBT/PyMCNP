import pymcnp
from ..... import consts
from ..... import classes


class Test_Conic:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.Conic
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('col')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.Conic
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.CONIC]
        EXAMPLES_INVALID = ['hello']


class Test_ConicBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ptrac.ConicBuilder
        EXAMPLES_VALID = [{'setting': 'col'}, {'setting': pymcnp.types.String('col')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
