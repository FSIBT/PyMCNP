import pymcnp
from ... import consts
from ... import classes


class Test_Generator:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Generator(pymcnp.types.Real)
        EXAMPLES_VALID = [
            {'value': (_ for _ in [consts.ast.types.REAL])},
        ]
        EXAMPLES_INVALID = [
            {'value': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Generator(pymcnp.types.Real)
        EXAMPLES_VALID = [
            consts.string.types.TUPLE,
        ]
        EXAMPLES_INVALID = []

    class Test_Dunder:
        EXAMPLES = [
            {'value': [consts.ast.types.REAL]},
        ]

        def test__iter__(self):
            for example in self.EXAMPLES:
                element = pymcnp.types.Generator(pymcnp.types.Real)(**example)
                iter(element)
