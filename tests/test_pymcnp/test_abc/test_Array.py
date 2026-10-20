import copy

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
                _space = ()
                _kind = (pymcnp.inp.Card,)

        with pytest.raises(pymcnp.abc.Error):

            class Array1(pymcnp.abc.Array):
                _space = (pymcnp.inp.Card,)
                _kind = ()

    def test_mcnp_valid(self) -> None:
        parse = pymcnp.abc.Array[pymcnp.inp.card.surface.X_0 | pymcnp.inp.card.surface.X_1, None].from_mcnp('1 x 1 1 1 1')
        assert parse[0].to_mcnp() == '1 x 1 1 1 1'
        assert parse[1] == ''

    def test_deepcopy_keeps_spaces(self) -> None:
        array = pymcnp.abc.Array[pymcnp.inp.literal.Integer, None](pymcnp.inp.literal.Integer('1'), pymcnp.inp.literal.Integer('2'))
        clone = copy.deepcopy(array)

        assert clone == array
        assert len(clone.spaces) == len(array.spaces) == 1
        assert clone.to_mcnp() == array.to_mcnp()

    def test_deepcopy_empty_and_single(self) -> None:
        kind = pymcnp.abc.Array[pymcnp.inp.literal.Integer, None]

        assert copy.deepcopy(kind()).spaces == []
        assert copy.deepcopy(kind(pymcnp.inp.literal.Integer('1'))).spaces == []

    def test_append_adds_a_space_only_between_items(self) -> None:
        array = pymcnp.abc.Array[pymcnp.inp.literal.Integer, None]()

        array.append(pymcnp.inp.literal.Integer('1'))
        assert array.spaces == []

        array.append(pymcnp.inp.literal.Integer('2'))
        assert len(array.spaces) == 1

        assert copy.deepcopy(array).to_mcnp() == array.to_mcnp()
