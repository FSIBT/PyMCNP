import pymcnp
from .... import classes


class Test_Real(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Real
    EXAMPLES_VALID = [
        '1',
        '1E10',
        '3.1',
        '3.',
        '.1',
        '3.1E10',
        '3.E10',
        '.1E10',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]

    def test___hash___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__hash__()

    def test___neg___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__neg__()

    def test___pos___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__pos__()

    def test___abs___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__abs__()

    def test___bool___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__bool__()

    def test___int___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__int__()

    def test___float___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__float__()

    def test___trunc___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__trunc__()

    def test___floor___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__floor__()

    def test___ceil___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__ceil__()

    def test___round___valid(self, real_a: pymcnp.inp.literal.Real) -> None:
        real_a.__round__()
        real_a.__round__(2)

    def test___lt___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real, str_b: str) -> None:
        real_a.__lt__(real_b)
        real_a.__lt__(str_b)

    def test___le___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real, str_b: str) -> None:
        real_a.__le__(real_b)
        real_a.__le__(str_b)

    def test___eq___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real, str_b: str) -> None:
        real_a.__eq__(real_b)
        real_a.__eq__(str_b)

    def test___ne___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real, str_b: str) -> None:
        real_a.__ne__(real_b)
        real_a.__ne__(str_b)

    def test___gt___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real, str_b: str) -> None:
        real_a.__gt__(real_b)
        real_a.__gt__(str_b)

    def test___ge___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real, str_b: str) -> None:
        real_a.__ge__(real_b)
        real_a.__ge__(str_b)

    def test___add___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real, str_b: str) -> None:
        real_a.__add__(real_b)
        real_a.__add__(str_b)

    def test___radd___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__radd__(real_b)

    def test___sub___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__sub__(real_b)

    def test___rsub___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__rsub__(real_b)

    def test___mul___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__mul__(real_b)

    def test___rmul___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__rmul__(real_b)

    def test___mod___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__mod__(real_b)

    def test___rmod___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__rmod__(real_b)

    def test___divmod___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__divmod__(real_b)

    def test___rdivmod___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__rdivmod__(real_b)

    def test___pow___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__pow__(real_b)

    def test___rpow___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__rpow__(real_b)

    def test___floordiv___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__floordiv__(real_b)

    def test___rfloordiv___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__rfloordiv__(real_b)

    def test___truediv___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__truediv__(real_b)

    def test___rtruediv___valid(self, real_a: pymcnp.inp.literal.Real, real_b: pymcnp.inp.literal.Real) -> None:
        real_a.__rtruediv__(real_b)


class Test_Integer(classes.Test_Nonterminal):
    element = pymcnp.inp.literal.Integer
    EXAMPLES_VALID = [
        '1',
        '1E10',
    ]
    EXAMPLES_INVALID = [
        'hello',
    ]

    def test___hash___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__hash__()

    def test___neg___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__neg__()

    def test___pos___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__pos__()

    def test___abs___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__abs__()

    def test___bool___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__bool__()

    def test___int___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__int__()

    def test___float___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__float__()

    def test___trunc___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__trunc__()

    def test___floor___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__floor__()

    def test___ceil___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__ceil__()

    def test___round___valid(self, integer_a: pymcnp.inp.literal.Integer) -> None:
        integer_a.__round__()
        integer_a.__round__(2)

    def test___lt___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer, str_b: str) -> None:
        integer_a.__lt__(integer_b)
        integer_a.__lt__(str_b)

    def test___le___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer, str_b: str) -> None:
        integer_a.__le__(integer_b)
        integer_a.__le__(str_b)

    def test___eq___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer, str_b: str) -> None:
        integer_a.__eq__(integer_b)
        integer_a.__eq__(str_b)

    def test___ne___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer, str_b: str) -> None:
        integer_a.__ne__(integer_b)
        integer_a.__ne__(str_b)

    def test___gt___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer, str_b: str) -> None:
        integer_a.__gt__(integer_b)
        integer_a.__gt__(str_b)

    def test___ge___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer, str_b: str) -> None:
        integer_a.__ge__(integer_b)
        integer_a.__ge__(str_b)

    def test___add___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer, str_b: str) -> None:
        integer_a.__add__(integer_b)
        integer_a.__add__(str_b)

    def test___radd___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__radd__(integer_b)

    def test___sub___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__sub__(integer_b)

    def test___rsub___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__rsub__(integer_b)

    def test___mul___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__mul__(integer_b)

    def test___rmul___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__rmul__(integer_b)

    def test___mod___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__mod__(integer_b)

    def test___rmod___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__rmod__(integer_b)

    def test___divmod___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__divmod__(integer_b)

    def test___rdivmod___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__rdivmod__(integer_b)

    def test___pow___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__pow__(integer_b)

    def test___rpow___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__rpow__(integer_b)

    def test___floordiv___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__floordiv__(integer_b)

    def test___rfloordiv___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__rfloordiv__(integer_b)

    def test___truediv___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__truediv__(integer_b)

    def test___rtruediv___valid(self, integer_a: pymcnp.inp.literal.Integer, integer_b: pymcnp.inp.literal.Integer) -> None:
        integer_a.__rtruediv__(integer_b)
