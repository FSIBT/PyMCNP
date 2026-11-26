import copy

import pytest

import pymcnp


class Test_Array:
    def test___init___valid(self) -> None:
        array = pymcnp.abc.Array[pymcnp.inp.literal.Integer, None](pymcnp.inp.literal.Integer('1'), pymcnp.inp.literal.Integer('2'))

        assert list(array) == ['1', '2']
        assert array.to_mcnp() == '1 2'

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
                _space = (pymcnp.inp.Card,)  # type:ignore
                _kind = ()

    def test_mcnp_valid(self) -> None:
        parse = pymcnp.abc.Array[pymcnp.inp.card.surface.X, None].from_mcnp('1 x 1 1 1 1')
        assert parse[0].to_mcnp() == '1 x 1 1 1 1'
        assert parse[1] == ''

    def test___deepcopy__(self) -> None:
        array = pymcnp.abc.Array[pymcnp.inp.literal.Integer, None](pymcnp.inp.literal.Integer('1'), pymcnp.inp.literal.Integer('2'))
        clone = copy.deepcopy(array)
        assert clone == array
        assert len(clone.spaces) == len(array.spaces) == 1
        assert clone.to_mcnp() == array.to_mcnp()

    def test___setitem___converts_values(self) -> None:
        # Items are converted like field values, so the array still writes MCNP text.
        e, _ = pymcnp.inp.card.data.E.from_mcnp('E0 1 2 3')
        e.e[0] = 5
        e.e[1:3] = [6.5, '7']
        assert [type(value) for value in e.e] == [pymcnp.inp.literal.Real] * 3
        assert e.e == [5, 6.5, 7]
        assert e.to_mcnp() == 'E0 5 6.5 7'
        with pytest.raises(pymcnp.abc.Error):
            e.e[0] = 'x'

    def test_filter(self) -> None:
        array, _ = pymcnp.abc.Array[pymcnp.inp.card.Surface, None].from_mcnp('1 x 1 1 1 1\n2 so 1')
        assert array.filter(pymcnp.inp.card.surface.X) == [pymcnp.inp.card.surface.X.from_mcnp('1 x 1 1 1 1')[0]]
        assert array.filter(j=3) == []
        assert array.filter(hello=2) == []

    def test_filter_skips_items_without_field(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 -1\n\n1 SO 1\n\nc a comment\nnps 10\n')
        found = inp.data.filter(npp=10)
        assert len(found) == 1
        assert found[0].to_mcnp() == 'nps 10'

    def test_filter_rejects_code_in_path(self) -> None:
        array, _ = pymcnp.abc.Array[pymcnp.inp.card.Surface, None].from_mcnp('1 x 1 1 1 1\n2 so 1')
        assert array.filter(**{'__class__.__init__.__globals__': 1}) == []
        assert array.filter(**{'j; import os': 1}) == []
        assert array.filter(**{'': 1}) == []
        assert array.filter(**{'j[': 1}) == []
        assert array.filter(**{'[0]': 1}) == []
        assert array.filter(**{'': 1, '..': 1}) == []

    def test_filter_path_syntax(self) -> None:
        array, _ = pymcnp.abc.Array[pymcnp.inp.card.Surface, None].from_mcnp('1 x 1 1 1 1\n2 so 1')
        assert len(array.filter(**{'j': 1})) == 1
        assert len(array.filter(**{'[5]': 1})) == 0
