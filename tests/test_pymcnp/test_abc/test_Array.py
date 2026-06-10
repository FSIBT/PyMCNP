import pymcnp

import pytest


class Test_Array:
    def test___init___valid(self) -> None:
        pymcnp.abc.Array[pymcnp.inp.literal.Integer, None](pymcnp.inp.literal.Integer('1'))

    def test___init___invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.abc.Array(spaces=(pymcnp.abc.Array._space[0](' '),))

    def test___post_init___invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):

            class Array0(pymcnp.abc.Array):
                _space = tuple()
                _kind = (pymcnp.inp.Card,)

        with pytest.raises(pymcnp.abc.Error):

            class Array1(pymcnp.abc.Array):
                _space = (pymcnp.inp.Card,)
                _kind = tuple()

    def test_mcnp_valid(self) -> None:
        parse = pymcnp.abc.Array[pymcnp.inp.card.surface.X_0 | pymcnp.inp.card.surface.X_1, None].from_mcnp('1 x 1 1 1 1')
        assert parse[0].to_mcnp() == '1 x 1 1 1 1'
        assert parse[1] == ''
