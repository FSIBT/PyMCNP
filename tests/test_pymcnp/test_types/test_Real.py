import decimal

import pymcnp
from ... import consts
from ... import classes


class Test_Real:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Real
        EXAMPLES_VALID = [
            {'value': 0.5},
        ]
        EXAMPLES_INVALID = [
            {'value': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Real
        EXAMPLES_VALID = [
            consts.string.types.REAL,
            '10r',
            '10i',
            '10j',
            '10m',
            '10log',
            '10ilog',
            'e2',
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]

    class Test_Dunder:
        EXAMPLES = [
            (consts.ast.types.REAL, consts.ast.types.REAL),
            (consts.ast.types.REAL, decimal.Decimal('0.5')),
            (consts.ast.types.REAL, 0.5),
        ]

        def test__hash__(self):
            for a, b in self.EXAMPLES:
                a.__hash__()

        def test__neg__(self):
            for a, b in self.EXAMPLES:
                a.__neg__()

        def test__pos__(self):
            for a, b in self.EXAMPLES:
                a.__pos__()

        def test__abs__(self):
            for a, b in self.EXAMPLES:
                a.__abs__()

        def test__bool__(self):
            for a, b in self.EXAMPLES:
                a.__bool__()

        def test__int__(self):
            for a, b in self.EXAMPLES:
                a.__int__()

        def test__float__(self):
            for a, b in self.EXAMPLES:
                a.__float__()

        def test__trunc__(self):
            for a, b in self.EXAMPLES:
                a.__trunc__()

        def test__floor__(self):
            for a, b in self.EXAMPLES:
                a.__floor__()

        def test__ceil__(self):
            for a, b in self.EXAMPLES:
                a.__ceil__()

        def test__round__(self):
            for a, b in self.EXAMPLES:
                a.__round__()

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

        def test__add__(self):
            for a, b in self.EXAMPLES:
                a.__add__(b)

        def test__radd__(self):
            for a, b in self.EXAMPLES:
                a.__radd__(b)

        def test__sub__(self):
            for a, b in self.EXAMPLES:
                a.__sub__(b)

        def test__rsub__(self):
            for a, b in self.EXAMPLES:
                a.__rsub__(b)

        def test__mul__(self):
            for a, b in self.EXAMPLES:
                a.__mul__(b)

        def test__rmul__(self):
            for a, b in self.EXAMPLES:
                a.__rmul__(b)

        def test__mod__(self):
            for a, b in self.EXAMPLES:
                a.__mod__(b)

        def test__rmod__(self):
            for a, b in self.EXAMPLES:
                a.__rmod__(b)

        def test__divmod__(self):
            for a, b in self.EXAMPLES:
                a.__divmod__(b)

        def test__rdivmod__(self):
            for a, b in self.EXAMPLES:
                a.__rdivmod__(b)

        def test__pow__(self):
            for a, b in self.EXAMPLES:
                a.__pow__(b)

        def test__rpow__(self):
            for a, b in self.EXAMPLES:
                a.__rpow__(b)

        def test__floordiv__(self):
            for a, b in self.EXAMPLES:
                a.__floordiv__(b)

        def test__rfloordiv__(self):
            for a, b in self.EXAMPLES:
                a.__rfloordiv__(b)

        def test__truediv__(self):
            for a, b in self.EXAMPLES:
                a.__truediv__(b)

        def test__rtruediv__(self):
            for a, b in self.EXAMPLES:
                a.__rtruediv__(b)
