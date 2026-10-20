import copy
import pathlib

import pytest

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


class Test_Inp_Continuation:
    HEAD = 'Hello\n1 0 -1\n\n1 SO 1\n\n'

    def test_unindented_line_after_ampersand(self) -> None:
        source = self.HEAD + 'm1 92235.80c 5 &\n92238.80c 95\nnps 10\n'
        inp, remainder = pymcnp.Inp.from_mcnp(source)
        assert remainder == ''
        assert inp.to_mcnp() == source
        assert inp.nps == 10


class Test_Inp_Issue_7:
    SOURCE = """MCNP Test Model for MOAA
C cells
1 1 20
         -1000  $ dollar comment
        imp:n,p=1 U=350 trcl=5
99 0
      1010
     imp:n,p=0

C surfaces
1000 SO 1
1010 SO 3

C data
C UO2 5 atpt enriched
m1        92235.80c           5 &
92238.80c          95
C Iron
m2        26054.80c        5.85
          plib= 80p
          26056           91.75
          26057        2.12 $ trailing comment
          26058.80c        0.28
C water
m3        1001.80c           2
           8016.80c           1
           plib=84p
MT3 lwtr.23t h-zr.20t h/zr.28t
mode n p
"""

    def test_library_keyword_between_substances_parses(self) -> None:
        inp, remainder = pymcnp.Inp.from_mcnp(self.SOURCE)
        assert remainder == ''
        assert 'plib= 80p' in inp.to_mcnp()
        assert 'plib=84p' in inp.to_mcnp()

    def test_written_issue_input_is_stable(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp(self.SOURCE)
        again, remainder = pymcnp.Inp.from_mcnp(inp.to_mcnp())
        assert remainder == ''
        assert again.to_mcnp() == inp.to_mcnp()


class Test_Inp_Horizontal_Format:
    HEAD = 'Hello\n1 0 -1\n\n1 SO 1\n\n'

    def _values(self, card: str) -> list[float]:
        inp, remainder = pymcnp.Inp.from_mcnp(self.HEAD + card + '\nnps 10\n')
        assert remainder == ''
        return [float(value) for value in inp.data[0].to_mcnp().split()[1:]]

    def test_repeat(self) -> None:
        assert self._values('si1 1 2r 5') == [1, 1, 1, 5]

    def test_insert_adds_values_between_the_endpoints(self) -> None:
        assert self._values('si1 0 2i 3 10') == [0, 1, 2, 3, 10]

    def test_insert_log_adds_values_between_the_endpoints(self) -> None:
        values = self._values('si1 1 2ilog 100 1000')
        assert values == pytest.approx([1, 100 ** (1 / 3), 100 ** (2 / 3), 100, 1000])

    def test_jump(self) -> None:
        inp, remainder = pymcnp.Inp.from_mcnp(self.HEAD + 'imp:n 1 2j 1\nnps 10\n')
        assert remainder == ''
        assert inp.data[0].to_mcnp().lower().split() == ['imp:n', '1', 'j', 'j', '1']


class Test_Inp_Copy:
    def test_deepcopy_keeps_blocks_separated_by_one_blank_line(self) -> None:
        surface = pymcnp.inp.card.surface.So(j=1, r=1)
        cell = pymcnp.inp.card.Cell_1(j=1, m=0, geom=-surface, options=['imp:n=1'])
        inp = pymcnp.Inp(title='t\n', cells=[cell], surfaces=[surface], data=[])

        assert copy.deepcopy(inp).to_mcnp() == inp.to_mcnp()

    def test_deepcopy_of_parsed_file_roundtrips(self) -> None:
        source = (pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_11.inp').read_text()
        inp, remainder = pymcnp.Inp.from_mcnp(source)

        assert remainder == ''
        assert copy.deepcopy(inp).to_mcnp() == inp.to_mcnp()
