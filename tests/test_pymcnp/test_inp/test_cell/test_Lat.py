import pymcnp
from .... import consts
from .... import classes


class Test_Lat:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Lat
        EXAMPLES_VALID = [{'shape': consts.string.types.INTEGER}, {'shape': 1}, {'shape': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'shape': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Lat
        EXAMPLES_VALID = [consts.string.inp.cell.LAT]
        EXAMPLES_INVALID = ['hello']
