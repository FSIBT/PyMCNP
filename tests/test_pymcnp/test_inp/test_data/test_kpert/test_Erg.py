import pymcnp
from ..... import consts
from ..... import classes


class Test_Erg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kpert.Erg
        EXAMPLES_VALID = [{'energies': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kpert.Erg
        EXAMPLES_VALID = [consts.string.inp.data.kpert.ERG]
        EXAMPLES_INVALID = ['hello']


class Test_ErgBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.kpert.ErgBuilder
        EXAMPLES_VALID = [{'energies': [consts.string.type.REAL]}, {'energies': [3.1]}, {'energies': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]
