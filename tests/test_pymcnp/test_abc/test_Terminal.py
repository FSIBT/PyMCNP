import re

import pytest

import pymcnp


class Test_Terminal:
    def test___new___invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.abc.Terminal[r'']('hello')

    def test___init_subclass___invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):

            class Terminal0(pymcnp.abc.Terminal):
                _pattern = re.compile(r'(Hi)([\s\S]*)')
                _default = 'Hello'
