import pymcnp
from .... import consts
from .... import classes


class Test_Filter:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.Filter
        EXAMPLES_VALID = [{'variables': [consts.string.inp.ptrac.filter.ENTRY]}, {'variables': [consts.ast.inp.ptrac.filter.ENTRY]}]
        EXAMPLES_INVALID = [{'variables': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.Filter
        EXAMPLES_VALID = [consts.string.inp.ptrac.FILTER]
        EXAMPLES_INVALID = ['hello']
