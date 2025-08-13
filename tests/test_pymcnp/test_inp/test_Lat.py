import pymcnp
from ... import consts
from ... import classes


class Test_Lat:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Lat
        EXAMPLES_VALID = [{'type': [consts.string.types.INTEGER]}, {'type': [1]}, {'type': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'type': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Lat
        EXAMPLES_VALID = [consts.string.inp.LAT]
        EXAMPLES_INVALID = ['hello']
