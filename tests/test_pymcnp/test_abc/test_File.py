import pymcnp

import pytest


class Test_File:
    def test_file_invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.Inp.from_file('hello.hi')
