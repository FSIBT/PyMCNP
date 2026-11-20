import pathlib

import pytest

import pymcnp


PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp'


class Test_Check:
    def test_check_valid(self) -> None:
        checker = pymcnp.Check()

        problems = checker.check(PATH / 'invalid_00.inp')
        assert problems == (
            pymcnp.abc.Error(title="Expected Terminal[r'(.+\\n)']", body="source[:200]='hello'", stack=[pymcnp.abc.Error(title='Expected ``Inp.title``.', body="source='hello'", stack=[])]),
        )

        problems = checker.check(PATH / 'warning_00.inp')
        assert problems == (pymcnp.abc.Warning(title='Line exceeds 80 characters maximum length', body='c ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'),)

    def test_check_invalid(self) -> None:
        checker = pymcnp.Check()

        with pytest.raises(pymcnp.abc.Error):
            checker.check(PATH / 'hello')

    # def test_fix_valid(self) -> None:
    # pymcnp.Check.fix(PATH / 'invalid_00.inp')
