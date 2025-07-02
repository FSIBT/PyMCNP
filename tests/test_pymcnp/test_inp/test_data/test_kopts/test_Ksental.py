import pymcnp
from ..... import consts
from ..... import classes


class Test_Ksental:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kopts.Ksental
        EXAMPLES_VALID = [{'fileopt': pymcnp.types.String('mctal')}]
        EXAMPLES_INVALID = [{'fileopt': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kopts.Ksental
        EXAMPLES_VALID = [consts.string.inp.data.kopts.KSENTAL]
        EXAMPLES_INVALID = ['hello']


class Test_KsentalBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.kopts.KsentalBuilder
        EXAMPLES_VALID = [{'fileopt': 'mctal'}, {'fileopt': pymcnp.types.String('mctal')}]
        EXAMPLES_INVALID = [{'fileopt': None}, {'fileopt': 'hello'}]
