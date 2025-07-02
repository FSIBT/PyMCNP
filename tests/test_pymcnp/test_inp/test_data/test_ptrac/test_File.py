import pymcnp
from ..... import consts
from ..... import classes


class Test_File:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.File
        EXAMPLES_VALID = [{'setting': pymcnp.types.String('asc')}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.File
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.FILE]
        EXAMPLES_INVALID = ['hello']


class Test_FileBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ptrac.FileBuilder
        EXAMPLES_VALID = [{'setting': 'asc'}, {'setting': pymcnp.types.String('asc')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]
