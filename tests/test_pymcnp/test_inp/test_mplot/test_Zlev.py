import pymcnp
from .... import consts
from .... import classes


class Test_Zlev:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Zlev
        EXAMPLES_VALID = [{'n': [consts.string.types.STRING]}, {'n': [consts.ast.types.STRING]}]
        EXAMPLES_INVALID = [{'n': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Zlev
        EXAMPLES_VALID = [consts.string.inp.mplot.ZLEV]
        EXAMPLES_INVALID = ['hello']
