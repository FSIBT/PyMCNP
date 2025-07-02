import pymcnp
from ..... import consts
from ..... import classes


class Test_Nescat:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.tropt.Nescat
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('off')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.tropt.Nescat
        EXAMPLES_VALID = [consts.string.inp.data.tropt.NESCAT]
        EXAMPLES_INVALID = ['hello']


class Test_NescatBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.tropt.NescatBuilder
        EXAMPLES_VALID = [{'setting': 'off'}, {'setting': pymcnp.types.String('off')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
