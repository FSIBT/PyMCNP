import pymcnp
from .... import consts
from .... import classes


class Test_Totnu:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Totnu
        EXAMPLES_VALID = [{'no': pymcnp.types.String('no')}, {'no': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Totnu
        EXAMPLES_VALID = [consts.string.inp.data.TOTNU]
        EXAMPLES_INVALID = ['hello']


class Test_TotnuBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.TotnuBuilder
        EXAMPLES_VALID = [{'no': 'no'}, {'no': pymcnp.types.String('no')}, {'no': None}]
        EXAMPLES_INVALID = [{'no': 'hello'}]
