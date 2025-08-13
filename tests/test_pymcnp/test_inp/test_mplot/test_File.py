import pymcnp
from .... import consts
from .... import classes


class Test_File:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.File
        EXAMPLES_VALID = [{'aa': 'all'}, {'aa': pymcnp.types.String('all')}, {'aa': None}]
        EXAMPLES_INVALID = [{'aa': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.File
        EXAMPLES_VALID = [consts.string.inp.mplot.FILE]
        EXAMPLES_INVALID = ['hello']
