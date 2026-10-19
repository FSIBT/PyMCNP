import pathlib

import pymcnp
from .. import classes


class Test_Inp(classes.Test_Nonterminal):
    element = pymcnp.Inp
    EXAMPLES_VALID = [
        (pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_11.inp').read_text(),
    ]
    EXAMPLES_INVALID = [
        'Vol Test\n1 0 2\n\n2 SO 1\n\nVOL 3.1 3.1\n',
        'Area Test\n1 0 2\n\n2 SO 1\n\nAREA 3.1 3.1\n',
        'hello',
    ]

    def test_nps_valid(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\n')
        assert inp.nps is None
        inp.nps = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nNPS 10\n'
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nNPS 200\n')
        assert inp.nps
        inp.nps = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nNPS 10\n'

    def test_seed_invalid(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\n')
        assert inp.seed is None
        inp.seed = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND SEED 10\n'
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND\n')
        assert inp.seed is None
        inp.seed = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND SEED 10\n'
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND GEN 1\n')
        assert inp.seed is None
        inp.seed = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND GEN 1 SEED 10\n'
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND GEN 1 SEED 200\n')
        assert inp.seed
        inp.seed = 10
        assert inp.to_mcnp() == 'Hello\n1 0 2\n\n2 SO 1\n\nSDEF\nRAND GEN 1 SEED 10\n'

    def test_vertical_format_valid(self) -> None:
        a, _ = pymcnp.Inp.from_file(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_42.inp')
        b, _ = self.element.from_mcnp(a.to_mcnp())
        assert a.to_mcnp() == b.to_mcnp()


class Test_Inp_Block_Ends:
    HEAD = 'Hello\n1 0 -1\n\n1 SO 1\n\n'

    def test_trailing_spaces_after_last_card(self) -> None:
        inp, remainder = pymcnp.Inp.from_mcnp(self.HEAD + 'nps 10' + ' ' * 40 + '\n')
        assert remainder == ''
        assert inp.nps == 10

    def test_empty_comment_after_card(self) -> None:
        inp, remainder = pymcnp.Inp.from_mcnp(self.HEAD + 'mode n $\nnps 10 $\n')
        assert remainder == ''
        assert inp.nps == 10


class Test_Inp_Trailing_Comments:
    HEAD = 'Hello\n1 0 -1\n\n1 SO 1\n\n'

    def test_comment_after_fm_card(self) -> None:
        source = self.HEAD + 'fm4 1 2 -5 $ multiplier\nnps 1e9 $ histories\n'
        inp, remainder = pymcnp.Inp.from_mcnp(source)
        assert remainder == ''
        assert inp.to_mcnp() == source

    def test_continued_fm_card_with_comment(self) -> None:
        source = self.HEAD + 'fm4 1 2\n     -5 $ multiplier\nnps 1e9\n'
        inp, remainder = pymcnp.Inp.from_mcnp(source)
        assert remainder == ''
        assert inp.to_mcnp() == source
