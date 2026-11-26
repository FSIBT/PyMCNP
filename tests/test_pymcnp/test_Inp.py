import sys
import pathlib

import numpy
import pytest

import pymcnp
from pymcnp.abc._path import get_path as pymcnp_get_path
from .. import classes


EXAMPLES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'examples'
PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp'


class Test_Inp(classes.Test_FromFile):
    element = pymcnp.Inp

    EXAMPLES_FROM_FILE_VALID = [
        PATH / 'valid_11.inp',
        *sorted(EXAMPLES.glob('example_*.inp')),
    ]
    EXAMPLES_FROM_FILE_INVALID = [
        PATH / 'invalid_00.inp',
    ]

    EXAMPLES_FROM_MCNP_VALID = [
        'Hello\n1 0 -1\n2 like 1 but mat=20 rho=2.0\n\n1 SO 1\n\nnps 10\n',
        # Testing trailing whitespace.
        'Hello\n1 0 -1\n\n1 SO 1\n\nnps 10     \n',
        # Testing empty comment.
        'Hello\n1 0 -1\n\n1 SO 1\n\nmode n $\nnps 10 $\n',
        # Testing comments.
        'Hello\n1 0 -1\n\n1 SO 1\n\nfm4 1 2 -5 $ multiplier\nnps 1e9 $ histories\n',
        # Testing no final newline after other block.
        'Hello\n1 0 -1\n\n1 SO 1\n\nnps 10\nc end of file',
        # Testing no final newline after data card block.
        'Hello\n1 0 -1\n\n1 SO 1\n\nnps 10\nnps 10',
        # Testing continuation.
        'Hello\n1 0 -1\n\n1 SO 1\n\nm1 92235.80c 5 &\n92238.80c 95\nnps 10\n',
        # Testing AREA, which has one entry per surface.
        'Area Test\n1 0 -1\n2 0 1 -2\n3 0 2\n\n1 SO 1\n2 SO 2\n\nAREA 10 20\n',
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'Hello\n1 0 -1\n\n1 SO 1\n1 SO 2\n\nnps 10\n',
        'Vol Test\n1 0 2\n\n2 SO 1\n\nVOL 3.1 3.1\n',
        'Vol Test\n1 0 2\n1 0 3\n\n2 SO 1\n\nVOL 3.1 3.1\n',
        'Vol Test\n1 0 2\n2 like 3 but imp:n=2\n\n2 SO 1\n\nVOL 3.1 3.1\n',
        'Area Test\n1 0 2\n\n2 SO 1\n\nAREA 3.1 3.1\n',
        'Area Test\n1 0 -1\n2 0 1 -2\n3 0 2\n\n1 SO 1\n2 SO 2\n\nAREA 10 20 30\n',
        'hello',
    ]

    def test_from_mcnp_valid(self) -> None:
        super().test_from_mcnp_valid()

        # Testing horizontal format.

        # Testing jump horizontal format preprocessing.
        inp, source = pymcnp.Inp.from_mcnp('Hello\n1 0 -1\n\n1 SO 1\n\nimp:n 1 2j 1\nnps 10\n')
        assert inp.data[0].to_mcnp() == 'imp:n 1 j j 1'

        # Testing repeat horizontal format preprocessing.
        inp, source = pymcnp.Inp.from_mcnp('Hello\n1 0 -1\n\n1 SO 1\n\nsi1 1 2r 5\nnps 10\n')
        assert inp.data[0].to_mcnp() == 'si1 1 1 1 5'

        # Testing insert horizontal format preprocessing.
        inp, source = pymcnp.Inp.from_mcnp('Hello\n1 0 -1\n\n1 SO 1\n\nsi1 0 2i 3\nnps 10\n')
        assert inp.data[0].to_mcnp() == 'si1 0.0 1.0 2.0 3.0'

        # Testing logarithmic insert horizontal format preprocessing.
        inp, source = pymcnp.Inp.from_mcnp('Hello\n1 0 -1\n\n1 SO 1\n\nsi1 1 2ilog 100\nnps 10\n')
        assert inp.data[0].to_mcnp() == 'si1 1.0 4.641588833612778 21.544346900318832 100.0'

    @pytest.mark.parametrize(
        'card, expanded',
        [
            ('e1 1 2m 3', 'e1 1 2.0 3'),
            ('si1 1 2m 2m', 'si1 1 2.0 4.0'),
            ('si1 2 1.5M 1e1m', 'si1 2 3.0 30.0'),
            ('si1 1 2m 2r', 'si1 1 2.0 2.0 2.0'),
            ('si1 1 2r 2m', 'si1 1 1 1 2.0'),
            ('si1 1 2r 2m 2r', 'si1 1 1 1 2.0 2.0 2.0'),
            ('si1 1 0.5m 2i 2', 'si1 1 0.5 1.0 1.5 2.0'),
            ('si1 1 2r 2m 1i 6', 'si1 1 1 1 2.0 4.0 6.0'),
        ],
    )
    def test_from_mcnp_expands_multiply(self, card, expanded) -> None:
        # `xM` is the previous entry times `x`.
        inp, remainder = pymcnp.Inp.from_mcnp(f'Hello\n1 0 -1\n\n1 SO 1\n\n{card}\nm1 1001 2\nnps 10\n')
        assert remainder == ''
        assert [card.to_mcnp() for card in inp.data[:2]] == [expanded, 'm1 1001 2']

    SCAN = 'Hello\nc cells\n1 0 -1\nc void\n2 0 1\n\nc surfaces\n1 SO 1\nc outer\n2 SO 2\n\nc data\nE0 1 14\nnps 10\n'

    def test_scan_cells_and_surfaces_by_number(self) -> None:
        # In scan paths, `cells[n]` and `surfaces[n]` select the card with number n; comment cards have none.
        inp, _ = pymcnp.Inp.from_mcnp(self.SCAN.replace('2 0 1', '20 0 1').replace('2 SO 2', '7 SO 2'))
        copies = list(inp.scan(**{'surfaces[7].r': [5, 6], 'cells[20].m': [0], 'cells.1.m': [0]}))
        assert [copy.surface_cards(7)[0].r for copy in copies] == [5, 6]
        assert [copy.surface_cards(1)[0].r for copy in copies] == [1, 1]
        assert copies[0].cell_cards(20)[0].to_mcnp() == '20 0 1'
        assert inp.surface_cards(7)[0].r == 2
        # A number no card has raises, naming it, whether or not it would be a valid list position.
        for path, number in (('surfaces[2].r', 'surface 2'), ('surfaces[0].r', 'surface 0'), ('cells[-1].m', 'cell -1'), ('cells[3].m', 'cell 3')):
            with pytest.raises(pymcnp.abc.Error, match=f'No {number}\\.'):
                next(inp.scan(**{path: [5]}))
        # Other paths are left as they are.
        assert [copy.nps for copy in inp.scan(nps=[1])] == [1]

    def test_scan_data_index_is_the_list_index(self) -> None:
        # `data[i]` counts as `inp.data[i]` does, comment cards included.
        inp, _ = pymcnp.Inp.from_mcnp(self.SCAN)
        assert type(inp.data[0]).__name__ == 'Comment'
        copies = list(inp.scan(**{'data[1].e[0]': [2], 'data.1.e[1]': [15]}))
        assert [card.to_mcnp() for card in copies[0].data] == ['c data', 'E0 2 15', 'nps 10']
        assert [copy.nps for copy in inp.scan(**{'data[-1].npp': [5]})] == [5]
        with pytest.raises(pymcnp.abc.Error, match='data\\[3\\]'):
            next(inp.scan(**{'data[3].npp': [5]}))

    def test_scan_title_adds_missing_newline(self) -> None:
        # A scanned title value may leave out the trailing newline; one that has it is kept as it is.
        inp, _ = pymcnp.Inp.from_mcnp(self.SCAN)
        copies = list(inp.scan(title=['Case A', 'Case B\n']))
        assert [copy.title for copy in copies] == ['Case A\n', 'Case B\n']
        for copy in copies:
            assert copy.to_mcnp().startswith(str(copy.title))
            assert pymcnp.Inp.from_mcnp(copy.to_mcnp())[0].to_mcnp() == copy.to_mcnp()
        # The original is unchanged.
        assert inp.title == self.SCAN.partition('\n')[0] + '\n'

    def test_title_adds_missing_newline(self) -> None:
        # The constructor and the setter add the title card's trailing newline as ``scan`` does.
        inp, _ = pymcnp.Inp.from_mcnp(self.SCAN)
        built = pymcnp.Inp(title='Sphere', cells=inp.cells, surfaces=inp.surfaces, data=inp.data)
        assert built.title == 'Sphere\n'
        assert built.to_mcnp().startswith('Sphere\nc cells\n')
        built.title = 'Other'
        assert built.title == 'Other\n'
        built.title = 'Kept\n'
        assert built.title == 'Kept\n'
        assert pymcnp.Inp.from_mcnp(built.to_mcnp())[0].title == 'Kept\n'
        # A symbol is kept as it is.
        built.title = pymcnp.abc.Terminal[r'.+\n']('Symbol\n')
        assert built.title == 'Symbol\n'
        with pytest.raises(pymcnp.abc.Error):
            built.title = ''

    def test_scan_values_keep_their_numeric_type(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp(self.SCAN)
        # Surface 2 is item 3 of ``surfaces``; ``data`` indices are list positions.
        for path, position in (('surfaces[2].r', 'surfaces[3].r'), ('data[1].e[1]', 'data[1].e[1]')):
            copies = list(inp.scan(**{path: [3, 4.5]}))
            values = [pymcnp_get_path(copy, position) for copy in copies]
            assert [type(value) for value in values] == [pymcnp.inp.literal.Real] * 2
            assert values == [3, 4.5] and values[1] + 1 == 5.5
            assert 'E0 1 3' in copies[0].to_mcnp() or '2 SO 3' in copies[0].to_mcnp()

    def test_from_mcnp_keeps_comments_verbatim(self) -> None:
        # Shorthands (`nJ`, `nR`, `nI`, `nLOG`) are expanded in cards only, not in the title, comment cards, `$` comments or
        # the text after the data block.
        source = (
            'Title 2j 3r\n'
            'c cells 2r 1 2i 4\n'
            '1 0 -1 imp:n=1 $ imp 2j 1 3r\n'
            '2 0 1 imp:n=0\n'
            '\n'
            '1 so 5\n'
            '\n'
            'c phys:n 50000 5j 4 100\n'
            '   C 1 2ilog 100\n'
            'imp:n 1 &\n'
            '1j $ 3j\n'
            'si1 1 2r 5\n'
            'nps 10\n'
            '\n'
            'notes 2j 1 3r\n'
        )
        inp, remainder = pymcnp.Inp.from_mcnp(source)
        assert remainder == ''
        assert inp.to_mcnp() == (
            'Title 2j 3r\n'
            'c cells 2r 1 2i 4\n'
            '1 0 -1 imp:n=1 $ imp 2j 1 3r\n'
            '2 0 1 imp:n=0\n'
            '\n'
            '1 so 5\n'
            '\n'
            'c phys:n 50000 5j 4 100\n'
            '   C 1 2ilog 100\n'
            'imp:n 1 &\n'
            'j $ 3j\n'
            'si1 1 1 1 5\n'
            'nps 10\n'
            '\n'
            'notes 2j 1 3r\n'
        )

    def test_cell_cards(self) -> None:
        """
        Tests `cell_cards` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            inp, _ = pymcnp.Inp.from_mcnp(example)

            cards = inp.cell_cards()
            assert cards and len(cards) == len(inp.cells.filter(pymcnp.inp.card.Cell))
            assert inp.cell_cards(number=10, material=20, density=2.0) == ()

        inp, _ = pymcnp.Inp.from_mcnp(self.EXAMPLES_FROM_MCNP_VALID[0])
        assert [card.to_mcnp() for card in inp.cell_cards()] == ['1 0 -1', '2 like 1 but mat=20 rho=2.0']
        assert [card.to_mcnp() for card in inp.cell_cards(number=2, material=20, density=2.0)] == ['2 like 1 but mat=20 rho=2.0']
        assert [card.to_mcnp() for card in inp.cell_cards(material=0)] == ['1 0 -1']
        assert [card.to_mcnp() for card in inp.cell_cards(kind=pymcnp.inp.card.Cell_1)] == ['1 0 -1']

    def test_surface_cards(self) -> None:
        """
        Tests `surface_cards` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            inp, _ = pymcnp.Inp.from_mcnp(example)

            cards = inp.surface_cards()
            assert len(cards) == len(inp.surfaces.filter(pymcnp.inp.card.Surface))

            cards = inp.surface_cards(kind=pymcnp.inp.card.surface.So)
            assert all(isinstance(card, pymcnp.inp.card.surface.So) for card in cards)

            cards = inp.surface_cards(number=10)
            assert all(hasattr(card, 'j') and card.j == 10 for card in cards)

    def test_data_cards(self) -> None:
        """
        Tests `data_cards` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            inp, _ = pymcnp.Inp.from_mcnp(example)

            cards = inp.data_cards()
            assert len(cards) == len(inp.data.filter(pymcnp.inp.card.Data))

    def test_comment_cards(self) -> None:
        """
        Tests `comment_cards` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            inp, _ = pymcnp.Inp.from_mcnp(example)
            cells, surfaces, data = inp.comment_cards()
            assert (cells, surfaces) == ((), ())
            assert [card.to_mcnp() for card in data] == (['c end of file'] if 'c end of file' in example else [])

        inp, _ = pymcnp.Inp.from_mcnp('Hello\nc a\n1 0 -1\n\nc b\nc bb\n1 SO 1\n\nc c\nnps 10\n')
        assert [[card.to_mcnp() for card in cards] for cards in inp.comment_cards()] == [['c a'], ['c b', 'c bb'], ['c c']]

    EXAMPLES_NPS = [
        'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\n',
    ]

    def test_nps(self) -> None:
        """
        Tests `nps` on `EXAMPLES_NPS`.
        """

        for example in self.EXAMPLES_NPS:
            inp, _ = pymcnp.Inp.from_mcnp(example)

            subexample = example
            subinp, _ = pymcnp.Inp.from_mcnp(subexample)
            assert subinp.nps is None
            subinp.nps = 10
            assert subinp.data.filter(pymcnp.inp.card.data.Nps, npp=10)

            subexample = f'{inp.title.to_mcnp()}{inp.cells.to_mcnp()}{inp.blank_0.to_mcnp()}{inp.surfaces.to_mcnp()}{inp.blank_1.to_mcnp()}nps 200\n{inp.data.to_mcnp()}{inp.blank_2.to_mcnp()}{inp.other.to_mcnp()}'
            subinp, _ = pymcnp.Inp.from_mcnp(subexample)
            assert subinp.nps == pymcnp.inp.literal.Integer('200')
            subinp.nps = 10
            assert subinp.data.filter(pymcnp.inp.card.data.Nps, npp=10)

    EXAMPLES_SEED = [
        'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\n',
    ]

    def test_seed(self) -> None:
        """
        Tests `seed` on `EXAMPLES_SEED`.
        """

        for example in self.EXAMPLES_SEED:
            inp, _ = pymcnp.Inp.from_mcnp(example)

            subexample = example
            subinp, _ = pymcnp.Inp.from_mcnp(subexample)
            assert subinp.seed is None
            subinp.seed = 10
            assert tuple(rand.options.filter(pymcnp.inp.option.data.rand.Seed, value=10) for rand in subinp.data.filter(pymcnp.inp.card.data.Rand))

            subexample = f'{inp.title.to_mcnp()}{inp.cells.to_mcnp()}{inp.blank_0.to_mcnp()}{inp.surfaces.to_mcnp()}{inp.blank_1.to_mcnp()}rand\n{inp.data.to_mcnp()}{inp.blank_2.to_mcnp()}{inp.other.to_mcnp()}'
            subinp, _ = pymcnp.Inp.from_mcnp(subexample)
            assert subinp.seed is None
            subinp.seed = 10
            assert tuple(rand.options.filter(pymcnp.inp.option.data.rand.Seed, value=10) for rand in subinp.data.filter(pymcnp.inp.card.data.Rand))

            subexample = f'{inp.title.to_mcnp()}{inp.cells.to_mcnp()}{inp.blank_0.to_mcnp()}{inp.surfaces.to_mcnp()}{inp.blank_1.to_mcnp()}rand gen 1\n{inp.data.to_mcnp()}{inp.blank_2.to_mcnp()}{inp.other.to_mcnp()}'
            subinp, _ = pymcnp.Inp.from_mcnp(subexample)
            assert subinp.seed is None
            subinp.seed = 10
            assert tuple(rand.options.filter(pymcnp.inp.option.data.rand.Seed, value=10) for rand in subinp.data.filter(pymcnp.inp.card.data.Rand))

            subexample = f'{inp.title.to_mcnp()}{inp.cells.to_mcnp()}{inp.blank_0.to_mcnp()}{inp.surfaces.to_mcnp()}{inp.blank_1.to_mcnp()}rand gen 1 seed 200\n{inp.data.to_mcnp()}{inp.blank_2.to_mcnp()}{inp.other.to_mcnp()}'
            subinp, _ = pymcnp.Inp.from_mcnp(subexample)
            assert subinp.seed == pymcnp.inp.literal.Integer('200')
            subinp.seed = 10
            assert tuple(rand.options.filter(pymcnp.inp.option.data.rand.Seed, value=10) for rand in subinp.data.filter(pymcnp.inp.card.data.Rand))


class Test_VerticalFormat:
    """
    Tests the vertical data format (``#`` blocks).
    """

    BASE = 'title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 1\n\n'

    @pytest.mark.parametrize('name', ['valid_36.inp', 'valid_37.inp'])
    def test_adjacent_blocks_keep_every_card(self, name) -> None:
        inp, remainder = pymcnp.Inp.from_file(PATH / name)
        assert remainder == ''
        cards = [card.to_mcnp() for card in inp.data_cards()]
        start = cards.index('SI1 0 1000 20000')
        assert cards[start : start + 6] == [
            'SI1 0 1000 20000',
            'SP1 0 1 0',
            'SI2 0 20000',
            'SP2 0 1',
            'F4:n 200',
            'T4 ' + ' '.join(str(value) for value in numpy.linspace(0, 20000, 101)),
        ]
        assert cards[start + 6 :] == ([] if name == 'valid_36.inp' else ['E4 0 5 14'])
        assert str(inp.other).strip() == ''
        again, remainder = pymcnp.Inp.from_mcnp(inp.to_mcnp())
        assert remainder == ''
        assert [' '.join(card.to_mcnp().replace('&', '').split()) for card in again.data_cards()] == [' '.join(card.split()) for card in cards]

    def test_indented_rows(self) -> None:
        source = self.BASE + 'sdef erg=d1\n# si1 sp1\n   1  0\n   2  1\n   3  2\nnps 10\n'
        inp, remainder = pymcnp.Inp.from_mcnp(source)
        assert remainder == ''
        assert [card.to_mcnp() for card in inp.data_cards()] == ['sdef erg=d1', 'si1 1 2 3', 'sp1 0 1 2', 'nps 10']

    def test_single_column_and_signed_values(self) -> None:
        source = self.BASE + '#  si1\n  -1\n  .5\n  2\n#  sp1  imp:n\n 0 j\n 1 1\nnps 10\n'
        inp, remainder = pymcnp.Inp.from_mcnp(source)
        assert remainder == ''
        assert [card.to_mcnp() for card in inp.data_cards()] == ['si1 -1 .5 2', 'sp1 0 1', 'imp:n j 1', 'nps 10']

    @pytest.mark.parametrize(
        'block',
        [
            # A row with fewer entries than card names.
            '# si1 sp1\n1 0\n2\n3 2\n',
            # A row with more entries than card names.
            '# si1 sp1\n1 0\n2 1 5\n',
            # A row with a `$` comment.
            '# si1 sp1\n1 0 $ first\n2 1\n',
            # Rows with shorthands: `2j` would be one entry of one card instead of a jump over two cards.
            '# si1 sp1\n1 2j\n2 1\n',
            '# si1 sp1\n1 0\n2 1r\n',
            '# si1 sp1\n1 0\n2 2m\n',
            '# si1 sp1\n1 0\n2 1i\n',
            '# si1 sp1\n1 0\n2 2log\n',
        ],
    )
    def test_unsupported_block_is_left_as_remainder(self, block) -> None:
        # A block PyMCNP cannot read is not dropped: it and every card after it are the remainder.
        inp, remainder = pymcnp.Inp.from_mcnp(self.BASE + 'sdef erg=d1\n' + block + 'nps 10\n')
        assert remainder.startswith('# si1 sp1\n')
        assert remainder.endswith('nps 10\n')
        assert [card.to_mcnp() for card in inp.data_cards()] == ['sdef erg=d1']

    def test_comment_card_ends_block(self) -> None:
        # A comment card between rows ends the block: the rows before it are read, and the rows after it, which do not
        # start a card, are the remainder.
        inp, remainder = pymcnp.Inp.from_mcnp(self.BASE + '# si1 sp1\n1 0\nc mid\n2 1\nnps 10\n')
        assert [card.to_mcnp() for card in inp.data_cards()] == ['si1 1', 'sp1 0']
        assert remainder == '2 1\nnps 10\n'

    def test_block_after_data_block_is_verbatim(self) -> None:
        source = self.BASE + 'nps 10\n\n# si1 sp1\n1 0\n2 1\n'
        inp, remainder = pymcnp.Inp.from_mcnp(source)
        assert remainder == ''
        assert inp.to_mcnp() == source


def _words(card) -> str:
    """Card text without `$` comments and `&`, with single spaces."""

    return ' '.join(' '.join(line.partition('$')[0].replace('&', ' ') for line in card.to_mcnp().split('\n')).split())


@pytest.mark.parametrize(
    'cell, data, cards',
    [
        ('1 1 -2.7 -1 & $ geometry\n     imp:n=1', 'm1 1001 2 & $ hydrogen\n8016 1', ['m1 1001 2 8016 1']),
        ('1 1 -2.7 -1 &$ geometry\nimp:n=1', 'si1 1 2 &  $\n     3 4\nsp1 0 1 1 1', ['si1 1 2 3 4', 'sp1 0 1 1 1']),
    ],
)
def test_continuation_after_dollar_comment(cell, data, cards) -> None:
    # `&` may be followed by a `$` comment; the next line still continues the card.
    inp, remainder = pymcnp.Inp.from_mcnp(f'title\n{cell}\n2 0 1 imp:n=0\n\n1 so 1\n\n{data}\nnps 10\n')
    assert remainder == ''
    assert [_words(card) for card in inp.cell_cards()] == ['1 1 -2.7 -1 imp:n=1', '2 0 1 imp:n=0']
    assert [_words(card) for card in inp.data_cards()] == [*cards, 'nps 10']
    assert pymcnp.Inp.from_mcnp(inp.to_mcnp()) == (inp, '')


_BASE = 'title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 5\n\n'


@pytest.mark.parametrize('card', ['f4:n 1 [1]', 'df4 iu=1 ic=10', 'zzz 10', 'f4:p (11<16[-10:10 -10:10 -10:10]<17)'])
def test_data_card_that_does_not_parse_is_the_remainder(card) -> None:
    # A data card PyMCNP cannot parse, even one that parses in part, ends parsing: it and every card after it are the remainder.
    inp, remainder = pymcnp.Inp.from_mcnp(_BASE + 'mode n\n' + card + '\nnps 10\n')
    assert remainder == card + '\nnps 10\n'
    assert [_words(item) for item in inp.data_cards()] == ['mode n']


def test_data_card_that_does_not_parse_first() -> None:
    inp, remainder = pymcnp.Inp.from_mcnp(_BASE + 'f4:n 1 [1]\nnps 10\n')
    assert remainder == 'f4:n 1 [1]\nnps 10\n'
    assert inp.data_cards() == ()


def test_valid_07_leaves_its_tally_as_the_remainder() -> None:
    inp, remainder = pymcnp.Inp.from_file(PATH / 'valid_07.inp')
    assert remainder.startswith('f4:p (11<16[-10:10 -10:10 -10:10]<17)\n')
    assert inp.nps == 10000


@pytest.mark.parametrize('cards', ['1 0 -1 imp:n=1 foo=3\n2 0 1 imp:n=0\n\n1 so 5\n\n', '1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 5 7 8 9 9 9\n\n'])
def test_cell_or_surface_card_that_does_not_parse_raises(cards) -> None:
    # Cells and surfaces cannot be cut short: the blocks after them would be missing.
    with pytest.raises(pymcnp.abc.Error):
        pymcnp.Inp.from_mcnp('title\n' + cards + 'nps 10\n')


@pytest.mark.parametrize('found', [None, (2, pymcnp.abc.Error('x', 'y'))])
def test_data_block_error_is_raised_if_no_card_can_be_cut(monkeypatch, found) -> None:
    # If the card cannot be found, or parsing up to it fails as well, the original error stands.
    monkeypatch.setattr(sys.modules['pymcnp.Inp'], '_unparseable_card', lambda lines: found)
    with pytest.raises(pymcnp.abc.Error, match='Inp.blank_2'):
        pymcnp.Inp.from_mcnp(_BASE + 'f4:n 1 [1]\nnps 10\n')
