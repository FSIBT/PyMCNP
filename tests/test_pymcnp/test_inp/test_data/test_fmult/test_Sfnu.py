import pymcnp
from ..... import consts
from ..... import classes


class Test_Sfnu:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmult.Sfnu
        EXAMPLES_VALID = [{'distribution': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'distribution': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmult.Sfnu
        EXAMPLES_VALID = [consts.string.inp.data.fmult.SFNU]
        EXAMPLES_INVALID = ['hello']


class Test_SfnuBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmult.SfnuBuilder
        EXAMPLES_VALID = [{'distribution': [consts.string.type.REAL]}, {'distribution': [3.1]}, {'distribution': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'distribution': None}]
