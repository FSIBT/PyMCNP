import numpy
import pytest

import pymcnp


@pytest.mark.parametrize(
    'kind, source, expected',
    [
        (pymcnp.inp.card.data.E, 'E14 0.1 3i 10', 'E14 0.1 2.575 5.05 7.525 10.0'),
        (pymcnp.inp.card.Data, 'si1 1 2r 5', 'si1 1 1 1 5'),
        (pymcnp.inp.card.Data, 'imp:n 1 2j 1', 'imp:n 1 j j 1'),
        (pymcnp.inp.card.Data, 'si1 1 2ilog 100 $ 2j\n     200 2r', 'si1 1.0 4.641588833612778 21.544346900318832 100.0 $ 2j\n     200 200 200'),
        (pymcnp.inp.card.Data, 'e1 1 2m 3', 'e1 1 2.0 3'),
        (pymcnp.inp.card.Cell, '1 0 -1 $ 2j\n     imp:n=1', '1 0 -1 $ 2j\n     imp:n=1'),
        (pymcnp.inp.card.Comment, 'c phys:n 2j 3r', 'c phys:n 2j 3r'),
    ],
)
def test_card_from_mcnp_expands_shorthands(kind, source, expected) -> None:
    # A single card expands `nR`, `nI`, `nJ`, `nLOG` and `xM` as `Inp` does, so it is not cut short at the shorthand.
    card, remainder = kind.from_mcnp(source)

    assert remainder == ''
    assert card.to_mcnp() == expected


def test_card_from_mcnp_expands_long_insert() -> None:
    card, remainder = pymcnp.inp.card.data.E.from_mcnp('E14 0.1 100i 10')

    assert remainder == ''
    assert [float(value) for value in card.e] == pytest.approx(numpy.linspace(0.1, 10, 102))
