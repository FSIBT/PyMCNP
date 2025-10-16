import pymcnp
from ... import consts
from ... import classes


class Test_Tuple:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Tuple(pymcnp.types.Real)
        EXAMPLES_VALID = [
            {'value': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'value': [None]},
            {'value': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Tuple(pymcnp.types.Real)
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
                element = pymcnp.types.Tuple(pymcnp.types.Real)(**example)
                iter(element)

        def test__getitem__(self):
            for example in self.EXAMPLES:
                element = pymcnp.types.Tuple(pymcnp.types.Real)(**example)
                element[0]

        def test__contains__(self):
            for example in self.EXAMPLES:
                element = pymcnp.types.Tuple(pymcnp.types.Real)(**example)
                'hello' in element
