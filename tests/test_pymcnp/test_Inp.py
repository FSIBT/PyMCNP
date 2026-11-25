import pathlib
import re

import pytest

import pymcnp
from .. import classes


PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp'


class Test_Inp(classes.Test_FromFile):
    element = pymcnp.Inp

    EXAMPLES_FROM_FILE_VALID = [
        PATH / 'valid_11.inp',
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

        # Testing non-inverible files.

        # Testing vertical format.
        inp, source = pymcnp.Inp.from_file(PATH / 'valid_42.inp')
        assert source == ''

        # Testing issue #7.
        inp, source = pymcnp.Inp.from_file(PATH / 'valid_34.inp')
        assert source == ''

    def test_cell_cards(self) -> None:
        """
        Tests `cell_cards` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            inp, _ = pymcnp.Inp.from_mcnp(example)
            _ = inp.cell_cards()
            _ = inp.cell_cards(number=10, material=20, density=2.0)

    def test_surface_cards(self) -> None:
        """
        Tests `surface_cards` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            inp, _ = pymcnp.Inp.from_mcnp(example)
            _ = inp.surface_cards()
            _ = inp.surface_cards(number=10)

    def test_data_cards(self) -> None:
        """
        Tests `data_cards` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            inp, _ = pymcnp.Inp.from_mcnp(example)
            _ = inp.data_cards()

    def test_comment_cards(self) -> None:
        """
        Tests `comment_cards` on `EXAMPLES_FROM_MCNP_VALID`.
        """

        for example in self.EXAMPLES_FROM_MCNP_VALID:
            inp, _ = pymcnp.Inp.from_mcnp(example)
            _, _, _ = inp.comment_cards()

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


EXAMPLES_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'examples'
EXAMPLE_INPS = sorted(EXAMPLES_DIR.glob('example_*.inp'))
EXAMPLE_INPS_NO_RAND = [p for p in EXAMPLE_INPS if not re.search(r'^\s*rand\b', p.read_text(), re.I | re.M)]


@pytest.mark.parametrize('path', EXAMPLE_INPS, ids=lambda p: p.name)
def test_surface_cards_all(path: pathlib.Path) -> None:
    inp_obj, _ = pymcnp.Inp.from_file(path)
    cards = inp_obj.surface_cards()
    assert len(cards) > 0
    assert len(cards) == len(inp_obj.surfaces.filter(pymcnp.inp.card.Surface))


@pytest.mark.parametrize('path', EXAMPLE_INPS, ids=lambda p: p.name)
def test_data_cards_all(path: pathlib.Path) -> None:
    inp_obj, _ = pymcnp.Inp.from_file(path)
    assert len(inp_obj.data_cards()) == len(inp_obj.data.filter(pymcnp.inp.card.Data))


def test_surface_cards_kind() -> None:
    inp_obj, _ = pymcnp.Inp.from_file(EXAMPLES_DIR / 'example_02.inp')
    kind = pymcnp.inp.card.surface.So
    cards = inp_obj.surface_cards(kind=kind)
    assert len(cards) > 0
    assert all(isinstance(c, kind) for c in cards)


@pytest.mark.parametrize('path', EXAMPLE_INPS_NO_RAND, ids=lambda p: p.name)
def test_seed_added_when_no_rand(path: pathlib.Path) -> None:
    inp_obj, _ = pymcnp.Inp.from_file(path)
    inp_obj.seed = 12345
    again, _ = pymcnp.Inp.from_mcnp(inp_obj.to_mcnp())
    assert again.seed == pymcnp.inp.literal.Integer('12345')
