import pymcnp
from ... import consts
from ... import classes


class Test_Designator:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Designator
        EXAMPLES_VALID = [
            {'particles': pymcnp.types.String('n,p,@')},
            {'particles': 'n,p,@'},
        ]
        EXAMPLES_INVALID = [
            {'particles': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Designator
        EXAMPLES_VALID = [
            consts.string.types.DESIGNATOR,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]
