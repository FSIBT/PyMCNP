import pymcnp
from ..... import consts
from ..... import classes


class Test_Thresh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Thresh
        EXAMPLES_VALID = [{'fraction': pymcnp.types.Real(0.8)}]
        EXAMPLES_INVALID = [{'fraction': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Thresh
        EXAMPLES_VALID = [consts.string.inp.data.act.THRESH]
        EXAMPLES_INVALID = ['hello']


class Test_ThreshBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.act.ThreshBuilder
        EXAMPLES_VALID = [{'fraction': '0.8'}, {'fraction': 0.8}, {'fraction': pymcnp.types.Real(0.8)}]
        EXAMPLES_INVALID = [{'fraction': None}, {'fraction': '3.1'}]
