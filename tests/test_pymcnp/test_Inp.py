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

    def test_no_newline_after_last_line(self) -> None:
        inp, remainder = pymcnp.Inp.from_mcnp(self.HEAD + 'nps 10\nc end of file')
        assert remainder == ''
        assert inp.nps == 10

    def test_no_newline_after_last_card(self) -> None:
        inp, remainder = pymcnp.Inp.from_mcnp(self.HEAD + 'nps 10')
        assert remainder == ''
        assert inp.nps == 10


class Test_Inp_Wrapping:
    HEAD = 'Hello\n1 0 -1\n\n1 SO 1\n\n'
    LONG = 'si1 ' + ' '.join(str(10 * n) for n in range(1, 40))

    def test_long_card_is_wrapped_at_80_columns(self) -> None:
        inp, remainder = pymcnp.Inp.from_mcnp(self.HEAD + self.LONG + '\nnps 10\n')
        lines = inp.to_mcnp().splitlines()
        assert remainder == ''
        assert max(len(line) for line in lines) <= 80
        first = next(i for i, line in enumerate(lines) if line.endswith(' &'))
        assert lines[first + 1].startswith(' ' * 5)

    def test_wrapped_card_keeps_its_values(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp(self.HEAD + self.LONG + '\nnps 10\n')
        again, remainder = pymcnp.Inp.from_mcnp(inp.to_mcnp())
        assert remainder == ''
        assert again.to_mcnp() == inp.to_mcnp()
        wrapped = inp.to_mcnp().split('\n\n')[2].split('\nnps')[0]
        assert wrapped.replace('&', '').split() == self.LONG.split()

    def test_trailing_comment_stays_on_last_line(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp(self.HEAD + self.LONG + ' $ bins\nnps 10\n')
        lines = inp.to_mcnp().splitlines()
        assert max(len(line) for line in lines if '$' not in line) <= 80
        assert any(line.endswith('$ bins') for line in lines)

    def test_text_and_comment_cards_are_not_wrapped(self) -> None:
        text = 'fc1 ' + ' '.join(['word'] * 30)
        comment = 'c ' + ' '.join(['word'] * 30)
        inp, remainder = pymcnp.Inp.from_mcnp(self.HEAD + text + '\n' + comment + '\nnps 10\n')
        assert remainder == ''
        assert text in inp.to_mcnp().splitlines()
        assert comment in inp.to_mcnp().splitlines()

    def test_short_input_is_unchanged(self) -> None:
        source = self.HEAD + 'si1 0 10 20\nnps 10\n'
        inp, _ = pymcnp.Inp.from_mcnp(source)
        assert inp.to_mcnp() == source
