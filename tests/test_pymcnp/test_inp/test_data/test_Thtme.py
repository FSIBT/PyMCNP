import pymcnp
from .... import consts
from .... import classes


class Test_Thtme:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Thtme
        EXAMPLES_VALID = [{'times': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'times': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Thtme
        EXAMPLES_VALID = [consts.string.inp.data.THTME]
        EXAMPLES_INVALID = ['hello']


class Test_ThtmeBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ThtmeBuilder
        EXAMPLES_VALID = [{'times': [consts.string.type.REAL]}, {'times': [3.1]}, {'times': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'times': None}]
