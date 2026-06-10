import pytest

import pymcnp


class Test_Check:
    def test___init___invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Check('hello.hi')

    def test_check_valid(self, check: pymcnp.Check) -> None:
        check.check()

    def test_fix_valid(self, check: pymcnp.Check) -> None:
        check.fix()
