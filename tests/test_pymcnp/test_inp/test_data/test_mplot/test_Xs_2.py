import pymcnp
from ..... import consts
from ..... import classes


class Test_Xs_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Xs_2
        EXAMPLES_VALID = [{'m': '?'}, {'m': pymcnp.types.String('?')}]
        EXAMPLES_INVALID = [{'m': None}, {'m': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Xs_2
        EXAMPLES_VALID = [consts.string.inp.data.mplot.XS_2]
        EXAMPLES_INVALID = ['hello']
