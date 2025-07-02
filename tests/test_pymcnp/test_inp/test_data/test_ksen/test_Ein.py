import pymcnp
from ..... import consts
from ..... import classes


class Test_Ein:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ksen.Ein
        EXAMPLES_VALID = [{'energies': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ksen.Ein
        EXAMPLES_VALID = [consts.string.inp.data.ksen.EIN]
        EXAMPLES_INVALID = ['hello']


class Test_EinBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ksen.EinBuilder
        EXAMPLES_VALID = [{'energies': [consts.string.type.REAL]}, {'energies': [3.1]}, {'energies': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]
