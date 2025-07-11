import pymcnp
from ..... import consts
from ..... import classes


class Test_Zlev:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Zlev
        EXAMPLES_VALID = [{'n': [consts.string.type.STRING]}, {'n': [consts.ast.type.STRING]}]
        EXAMPLES_INVALID = [{'n': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Zlev
        EXAMPLES_VALID = [consts.string.inp.data.mplot.ZLEV]
        EXAMPLES_INVALID = ['hello']
