import pymcnp
from .... import consts
from .... import classes


class Test_File:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.File
        EXAMPLES_VALID = [{'setting': 'asc'}, {'setting': pymcnp.types.String('asc')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.File
        EXAMPLES_VALID = [consts.string.inp.ptrac.FILE]
        EXAMPLES_INVALID = ['hello']
