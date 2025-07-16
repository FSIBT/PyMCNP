import pymcnp
from ..... import consts
from ..... import classes


class Test_Cel:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssw.Cel
        EXAMPLES_VALID = [{'cfs': [consts.string.types.INTEGER]}, {'cfs': [1]}, {'cfs': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'cfs': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssw.Cel
        EXAMPLES_VALID = [consts.string.inp.data.ssw.CEL]
        EXAMPLES_INVALID = ['hello']
