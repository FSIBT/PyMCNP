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


@pytest.mark.parametrize(
    'source',
    [
        'sc1 source 2r here',
        'SC12 1 2i 4 3m',
        'fc4 detector 1 2j 3',
        'fc4 detector 1 2j 3\n     more 2r',
    ],
)
def test_card_from_mcnp_leaves_text_cards(source) -> None:
    # `fc` and `sc` cards hold free text, so `2r` or `2j` in it are words, not shorthands.
    card, remainder = pymcnp.inp.card.Data.from_mcnp(source)

    assert remainder == ''
    assert card.to_mcnp() == source


def test_inp_leaves_text_cards() -> None:
    # `Inp` leaves the text of `fc` and `sc` cards, with their continuation lines, as it is, and still expands the next card.
    text = 'sc1 source 2r here\nfc4 detector 1 2j 3\n     more 2r\nc 2r\nsi1 1 2r'
    inp, remainder = pymcnp.Inp.from_mcnp(f'title\n1 0 -1\n\n1 so 1\n\n{text}\n')

    assert remainder == ''
    assert [card.to_mcnp() for card in inp.data] == [
        'sc1 source 2r here',
        'fc4 detector 1 2j 3\n     more 2r',
        'c 2r',
        'si1 1 1 1',
    ]


def test_check_leaves_text_cards(tmp_path) -> None:
    # `Check` reads a text card as `Inp` does, so the file has no problems.
    path = tmp_path / 'text.inp'
    path.write_text('title\n1 0 -1\n\n1 so 1\n\nfc4 detector 1 2j 3\n     more 2r\nnps 1\n')

    assert pymcnp.Check(path).problems() == []


def test_expand_card_leaves_text_card_continued_with_ampersand() -> None:
    # A line after a text card line ending in `&` is still text; the card after it is expanded.
    source = 'fc5 a 2r & $ 2r\nb 2r\nc 2r\n     d 2r\nsi1 1 2r'

    assert pymcnp.inp._shorthand._expand_card(source) == 'fc5 a 2r & $ 2r\nb 2r\nc 2r\n     d 2r\nsi1 1 1 1'
