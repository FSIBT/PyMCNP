import shutil
import pathlib

import pytest

import pymcnp
from pymcnp.Check import Problem


FILES = pathlib.Path(__file__).parents[2] / 'files' / 'inp'
VALID = FILES / 'valid_00.inp'
SOURCE = 'Title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 5\n\nnps 10\n\n'


@pytest.fixture
def check(tmp_path: pathlib.Path) -> pymcnp.Check:
    """
    Check on a copy of a valid file, since ``fix`` writes the file.
    """

    path = tmp_path / 'valid.inp'
    shutil.copy(VALID, path)

    return pymcnp.Check(path)


class Test_Check:
    def test___init___invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Check('hello.hi')

    def test_check_valid(self, check: pymcnp.Check) -> None:
        assert list(check.check()) == []

    def test_check_shows_wrapped_line(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'wide.inp'
        bins = ' '.join(str(10 * n) for n in range(1, 40))
        path.write_text(SOURCE.replace('nps 10', f'si1 {bins}\nnps 10'))

        diff = list(pymcnp.Check(path).check())

        assert f'-si1 {bins}' in diff
        assert any(line.startswith('+si1 10 20') for line in diff)

    def test_fix_valid(self, check: pymcnp.Check) -> None:
        check.fix()

        assert list(check.check()) == []

    def test_fix_wraps_wide_line(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'wide.inp'
        bins = ' '.join(str(10 * n) for n in range(1, 40))
        path.write_text(SOURCE.replace('nps 10', f'si1 {bins}\nnps 10'))
        checker = pymcnp.Check(path)

        checker.fix()

        assert max(len(line) for line in path.read_text().split('\n')) <= 80
        assert pymcnp.Check(path).problems() == []

    @pytest.mark.filterwarnings('ignore:Line exceeds 80 characters:pymcnp.abc.Warning')
    def test_fix_returns_lines_it_cannot_shorten(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'warning.inp'
        shutil.copy(FILES / 'warning_00.inp', path)

        remaining = pymcnp.Check(path).fix()

        assert [(problem.line, problem.kind) for problem in remaining] == [(8, 'error')]
        assert remaining == pymcnp.Check(path).problems()

    def test_fix_returns_nothing_left(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'ok.inp'
        path.write_text(SOURCE)

        assert pymcnp.Check(path).fix() == []


class Test_Check_Problems:
    def test_problems_line_numbers(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'warning.inp'
        shutil.copy(FILES / 'warning_00.inp', path)
        lines = path.read_text().split('\n')
        wide = [n for n, line in enumerate(lines, 1) if len(line) > 80]
        assert wide

        problems = pymcnp.Check(path).problems()

        found = [problem for problem in problems if problem.kind == 'error']
        assert [problem.line for problem in found] == wide
        assert isinstance(found[0], Problem)
        assert 'Line exceeds 80 characters maximum length' in found[0].message

    def test_wide_line_is_an_error(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'wide.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10 $ ' + 'x' * 80))

        problems = pymcnp.Check(path).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(7, 'error')]
        assert '89 columns' in problems[0].message

    def test_line_of_exactly_80_columns_is_fine(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'edge.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10 $ ' + 'x' * 71))

        assert pymcnp.Check(path).problems() == []

    def test_unknown_card_is_a_warning_at_its_line(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'unknown.inp'
        path.write_text(SOURCE.replace('1 so 5', '1 so 5\n2 zzz 5'))

        problems = pymcnp.Check(path).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(6, 'warning')]
        assert 'run the check again' in problems[0].message

    def test_unknown_data_card_line_with_continuation(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'continued.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10\nfoo 1 2 &\n    3'))

        problems = pymcnp.Check(path).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(8, 'warning')]

    def test_missing_file(self, tmp_path: pathlib.Path) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Check(tmp_path / 'missing.inp')

    def test_file_removed_after_init(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'gone.inp'
        path.write_text(SOURCE)
        checker = pymcnp.Check(path)
        path.unlink()

        with pytest.raises(pymcnp.abc.Error):
            checker.problems()

    def test_unknown_card_after_vertical_data_block(self, tmp_path: pathlib.Path) -> None:
        path = tmp_path / 'vertical.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10\n# si1 sp1\n1 0\n2 1\nfoo 1'))

        problems = pymcnp.Check(path).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(11, 'warning')]

    def test_vertical_block_with_short_row(self, tmp_path: pathlib.Path) -> None:
        # A block whose rows do not have one entry per card name is not read, so its `#` line is the problem.
        path = tmp_path / 'vertical.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10\n# si1 sp1\n1 0\n2 1 3\nfoo 1'))

        problems = pymcnp.Check(path).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(8, 'warning')]

    def test_unknown_card_after_comment_cards(self, tmp_path: pathlib.Path) -> None:
        # Comment cards, including indented ones and those in the middle of a card, are not cards to parse.
        path = FILES.parents[1] / 'examples' / 'example_00.inp'
        lines = path.read_text().split('\n')
        index = next(i for i, line in enumerate(lines) if line.lower().startswith('nps'))
        lines.insert(index, 'PRDMP J J -1 bogus=3')
        lines.insert(index, '   c an indented comment card')
        bad = tmp_path / 'commented.inp'
        bad.write_text('\n'.join(lines))

        problems = pymcnp.Check(bad).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(index + 2, 'warning')]
        assert 'cannot parse this card' in problems[0].message

    def test_unknown_card_with_shorthands(self, tmp_path: pathlib.Path) -> None:
        # Cards are checked with their shorthands expanded, as ``Inp`` parses them.
        path = tmp_path / 'shorthand.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10\ne0 1 3r 2m\nfoo 1'))

        problems = pymcnp.Check(path).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(9, 'warning')]

    def test_card_parsed_to_its_end(self) -> None:
        # A card that parses only in part, here up to an indented ``c`` in a continuation line, is the problem.
        problems = pymcnp.Check(FILES / 'valid_39.inp').problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(66, 'warning')]
        assert "Expected end of card at 'c'" in problems[0].message
