import pymcnp
from ... import consts
from ... import classes


class Test_String:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.String
        EXAMPLES_VALID = [
            {'value': consts.string.types.STRING},
        ]
        EXAMPLES_INVALID = [
            {'value': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.String
        EXAMPLES_VALID = [
            consts.string.types.STRING,
        ]
        EXAMPLES_INVALID = []

    class Test_Dunder:
        EXAMPLES = [
            (consts.ast.types.STRING, consts.ast.types.STRING),
            (consts.ast.types.STRING, 'none'),
        ]

        def test__hash__(self):
            for a, b in self.EXAMPLES:
                a.__hash__()

        def test__iter__(self):
            for a, b in self.EXAMPLES:
                a.__iter__()

        def test__len__(self):
            for a, b in self.EXAMPLES:
                a.__len__()

        def test__getitem__(self):
            for a, b in self.EXAMPLES:
                a.__getitem__(0)
                a.__getitem__(consts.ast.types.INTEGER)

        def test__contains__(self):
            for a, b in self.EXAMPLES:
                a.__contains__(b)

        def test__format__(self):
            for a, b in self.EXAMPLES:
                f'{a}'

        def test__lt__(self):
            for a, b in self.EXAMPLES:
                a.__lt__(b)

        def test__le__(self):
            for a, b in self.EXAMPLES:
                a.__le__(b)

        def test__eq__(self):
            for a, b in self.EXAMPLES:
                a.__eq__(b)

        def test__ne__(self):
            for a, b in self.EXAMPLES:
                a.__ne__(b)

        def test__gt__(self):
            for a, b in self.EXAMPLES:
                a.__gt__(b)

        def test__ge__(self):
            for a, b in self.EXAMPLES:
                a.__ge__(b)

        # def test__mod__(self):
        # for a, b in self.EXAMPLES:
        # a.__mod__(b)

        # def test__rmod__(self):
        # for a, b in self.EXAMPLES:
        # a.__rmod__(b)

        def test__add__(self):
            for a, b in self.EXAMPLES:
                a.__add__(b)

        def test__mul__(self):
            for a, b in self.EXAMPLES:
                a.__mul__(1)
                a.__mul__(consts.ast.types.INTEGER)

        def test__rmul__(self):
            for a, b in self.EXAMPLES:
                a.__rmul__(1)
                a.__rmul__(consts.ast.types.INTEGER)
