import pymcnp
from ..... import consts
from ..... import classes


class Test_Kinetics:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kopts.Kinetics
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kopts.Kinetics
        EXAMPLES_VALID = [consts.string.inp.data.kopts.KINETICS]
        EXAMPLES_INVALID = ['hello']


class Test_KineticsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.kopts.KineticsBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
