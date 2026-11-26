import pathlib


import pymcnp
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
    ]
    EXAMPLES_FROM_MCNP_INVALID = [
        'Hello\n1 0 -1\n\n1 SO 1\n1 SO 2\n\nnps 10\n',
        'Vol Test\n1 0 2\n\n2 SO 1\n\nVOL 3.1 3.1\n',
        'Vol Test\n1 0 2\n1 0 3\n\n2 SO 1\n\nVOL 3.1 3.1\n',
        'Vol Test\n1 0 2\n2 like 3 but imp:n=2\n\n2 SO 1\n\nVOL 3.1 3.1\n',
        'Area Test\n1 0 2\n\n2 SO 1\n\nAREA 3.1 3.1\n',
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
