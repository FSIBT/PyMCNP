import pymcnp
from ... import consts
from ... import classes


class Test_Imp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Lattice
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = [{'ast': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Lattice
        EXAMPLES_VALID = [consts.string.types.LATTICE, '(1)<(2)', '1[1:2 3:4 5:6]' '1<2<3<4<5']
        EXAMPLES_INVALID = ['hello', '', '1[1:4 5:4 6:5', '1[1:4 5:4', '1:', '1[2']
