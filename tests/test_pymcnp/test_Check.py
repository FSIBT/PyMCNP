import pathlib

import pytest

import pymcnp
from .. import classes


class Test_Check:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Check
        EXAMPLES_VALID = [{'path': pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'}]
        EXAMPLES_INVALID = [
            {'path': None},
        ]

    class Test_Methods:
        element = pymcnp.Check
        EXAMPLES = [{'path': pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'}]

        def test_check(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.check()

        def test_fix(self):
            for example in self.EXAMPLES:
                element = self.element(**example)
                element.check()


VALID = pathlib.Path(__file__).parents[2] / 'files' / 'inp' / 'valid_00.inp'
SOURCE = 'Title\n1 0 -1 imp:n=1\n2 0 1 imp:n=0\n\n1 so 5\n\nnps 10\n\n'


class Test_Check_Problems:
    def test_valid_has_no_problems(self):
        assert pymcnp.Check(VALID).problems() == []

    def test_wide_line_is_an_error(self, tmp_path):
        path = tmp_path / 'wide.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10 $ ' + 'x' * 80))

        problems = pymcnp.Check(path).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(7, 'error')]
        assert '89 columns' in problems[0].message

    def test_line_of_exactly_80_columns_is_fine(self, tmp_path):
        path = tmp_path / 'edge.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10 $ ' + 'x' * 71))

        assert pymcnp.Check(path).problems() == []

    def test_unknown_card_is_a_warning_at_its_line(self, tmp_path):
        path = tmp_path / 'unknown.inp'
        path.write_text(SOURCE.replace('1 so 5', '1 so 5\n2 zzz 5'))

        problems = pymcnp.Check(path).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(6, 'warning')]
        assert 'run the check again' in problems[0].message

    def test_unknown_data_card_line_with_continuation(self, tmp_path):
        path = tmp_path / 'continued.inp'
        path.write_text(SOURCE.replace('nps 10', 'nps 10\nfoo 1 2 &\n    3'))

        problems = pymcnp.Check(path).problems()

        assert [(problem.line, problem.kind) for problem in problems] == [(8, 'warning')]

    def test_missing_file(self, tmp_path):
        with pytest.raises(pymcnp.errors.CliError):
            pymcnp.Check(tmp_path / 'missing.inp').problems()
