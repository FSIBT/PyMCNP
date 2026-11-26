import decimal

import pytest

import pymcnp
from .... import classes


Real = pymcnp.inp.literal.Real
Integer = pymcnp.inp.literal.Integer


class Test_Real(classes.Test_FromMcnp):
    element = Real
    EXAMPLES_FROM_MCNP_VALID = [
        '1',
        '1E10',
        '3.1',
        '3.',
        '.1',
        '3.1E10',
        '3.E10',
        '.1E10',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]


class Test_Integer(classes.Test_FromMcnp):
    element = Integer
    EXAMPLES_FROM_MCNP_VALID = [
        '1',
        '1E10',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'hello',
    ]


# (dunder, self, arguments, expected): ``Real`` and ``Integer`` keep their own type, except where noted.
DUNDERS = [
    # Unary.
    ('neg', Real('1.1'), (), Real('-1.1')),
    ('pos', Real('1.1'), (), Real('1.1')),
    ('abs', Real('-1.1'), (), Real('1.1')),
    ('bool', Real('1.1'), (), True),
    ('bool', Real('0.0'), (), False),
    ('int', Real('1.1'), (), 1),
    ('float', Real('1.1'), (), 1.1),
    ('trunc', Real('-1.1'), (), -1),
    ('floor', Real('-1.1'), (), -2),
    ('ceil', Real('1.1'), (), 2),
    ('round', Real('1.6'), (), Real('2')),
    ('round', Real('1.1'), (2,), Real('1.10')),
    ('hash', Real('1.1'), (), hash(decimal.Decimal('1.1'))),
    ('neg', Integer('1'), (), Integer('-1')),
    ('pos', Integer('1'), (), Integer('1')),
    ('abs', Integer('-1'), (), Integer('1')),
    ('bool', Integer('1'), (), True),
    ('bool', Integer('0'), (), False),
    ('int', Integer('1E2'), (), 100),
    ('float', Integer('1'), (), 1.0),
    ('trunc', Integer('1'), (), 1),
    ('floor', Integer('1'), (), 1),
    ('ceil', Integer('1'), (), 1),
    ('round', Integer('1'), (), Real('1')),
    ('round', Integer('1'), (2,), Real('1.00')),
    ('hash', Integer('1'), (), hash(1)),
    # Comparisons by value with numbers, and as strings otherwise.
    ('lt', Real('1.1'), (Real('2.1'),), True),
    ('lt', Real('2.1'), (Real('1.1'),), False),
    ('le', Real('1.1'), (Real('1.10'),), True),
    ('le', Real('2.1'), (Real('1.1'),), False),
    ('eq', Real('1.1'), (Real('1.10'),), True),
    ('eq', Real('1.1'), (Real('2.1'),), False),
    ('ne', Real('1.1'), (Real('2.1'),), True),
    ('ne', Real('1.1'), (Real('1.10'),), False),
    ('gt', Real('2.1'), (Real('1.1'),), True),
    ('gt', Real('1.1'), (Real('2.1'),), False),
    ('ge', Real('1.1'), (Real('1.10'),), True),
    ('ge', Real('1.1'), (Real('2.1'),), False),
    ('lt', Real('1.1'), ('a',), True),
    ('le', Real('1.1'), ('a',), True),
    ('eq', Real('1.1'), ('1.10',), False),
    ('ne', Real('1.1'), ('1.10',), True),
    ('gt', Real('1.1'), ('a',), False),
    ('ge', Real('1.1'), ('a',), False),
    ('lt', Integer('1'), (Integer('2'),), True),
    ('le', Integer('2'), (Integer('1'),), False),
    ('eq', Integer('1'), (Real('1.0'),), True),
    ('ne', Integer('1'), (1,), False),
    ('gt', Integer('2'), (Integer('1'),), True),
    ('ge', Integer('1'), (Integer('2'),), False),
    ('lt', Integer('1'), ('a',), True),
    ('le', Integer('1'), ('a',), True),
    ('eq', Integer('1'), ('1',), True),
    ('ne', Integer('1'), ('1',), False),
    ('gt', Integer('1'), ('a',), False),
    ('ge', Integer('1'), ('a',), False),
    # Arithmetic.
    ('add', Real('1.1'), (Real('2.1'),), Real('3.2')),
    ('add', Real('1.1'), ('a',), '1.1a'),
    ('radd', Real('1.1'), (Real('2.1'),), Real('3.2')),
    ('sub', Real('1.1'), (Real('2.1'),), Real('-1.0')),
    ('rsub', Real('1.1'), (Real('2.1'),), Real('1.0')),
    ('mul', Real('1.1'), (Real('2.1'),), Real('2.31')),
    ('rmul', Real('1.1'), (Real('2.1'),), Real('2.31')),
    ('mod', Real('1.1'), (Real('2.1'),), Real('1.1')),
    ('rmod', Real('1.1'), (Real('2.1'),), Real('1.0')),
    ('divmod', Real('1.1'), (Real('2.1'),), (Real('0'), Real('1.1'))),
    ('rdivmod', Real('1.1'), (Real('2.1'),), (Real('1'), Real('1.0'))),
    ('pow', Real('1.1'), (Real('2.1'),), Real('1.221587665160033301118458843')),
    ('rpow', Real('1.1'), (Real('2.1'),), Real('2.261732424639162721756443140')),
    ('floordiv', Real('1.1'), (Real('2.1'),), Real('0')),
    ('rfloordiv', Real('1.1'), (Real('2.1'),), Real('1')),
    ('truediv', Real('1.1'), (Real('2.1'),), Real('0.5238095238095238095238095238')),
    ('rtruediv', Real('1.1'), (Real('2.1'),), Real('1.909090909090909090909090909')),
    ('add', Integer('1'), (Integer('2'),), Integer('3')),
    ('add', Integer('1'), ('a',), '1a'),
    ('radd', Integer('1'), (Integer('2'),), Integer('3')),
    ('sub', Integer('1'), (Integer('2'),), Integer('-1')),
    ('rsub', Integer('1'), (Integer('2'),), Integer('1')),
    ('mul', Integer('3'), (Integer('2'),), Integer('6')),
    ('rmul', Integer('3'), (Integer('2'),), Integer('6')),
    ('mod', Integer('5'), (Integer('3'),), Integer('2')),
    ('rmod', Integer('3'), (Integer('5'),), Integer('2')),
    ('divmod', Integer('5'), (Integer('3'),), (Integer('1'), Integer('2'))),
    ('rdivmod', Integer('3'), (Integer('5'),), (Integer('1'), Integer('2'))),
    ('pow', Integer('2'), (Integer('3'),), Integer('8')),
    ('rpow', Integer('2'), (Integer('3'),), Integer('9')),
    ('floordiv', Integer('5'), (Integer('2'),), Integer('2')),
    ('rfloordiv', Integer('2'), (Integer('5'),), Integer('2')),
    ('truediv', Integer('1'), (Integer('2'),), Real('0.5')),
    ('rtruediv', Integer('1'), (Integer('2'),), Real('2')),
]


def _same(result: object, expected: object) -> bool:
    """
    Checks type and exact value; ``Real`` and ``Integer`` by their text, since ``==`` compares them by value.
    """

    if isinstance(expected, tuple):
        return type(result) is tuple and len(result) == len(expected) and all(_same(r, e) for r, e in zip(result, expected))
    return type(result) is type(expected) and (str.__eq__(result, expected) if isinstance(expected, str) else result == expected)


@pytest.mark.parametrize(('dunder', 'number', 'arguments', 'expected'), DUNDERS, ids=lambda value: value if isinstance(value, str) else None)
def test_dunder(dunder: str, number: pymcnp.inp.literal.Real, arguments: tuple, expected: object) -> None:
    result = getattr(number, f'__{dunder}__')(*arguments)

    assert _same(result, expected), f'{type(number).__name__}({number!r}).__{dunder}__{arguments} = {type(result).__name__}({result!r})'


def test_dunders_cover_both_types() -> None:
    names = {name.strip('_') for name, value in vars(Real).items() if name.startswith('__') and callable(value)}

    for kind in (Real, Integer):
        assert names <= {dunder for dunder, number, _, _ in DUNDERS if type(number) is kind}, kind
