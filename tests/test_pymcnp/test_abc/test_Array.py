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

    @pytest.mark.parametrize(
        'mutate, expected',
        [
            (lambda a: a.__setitem__(slice(0, 1), [7, 8]), 'E0 7 8 2 3'),
            (lambda a: a.__setitem__(slice(0, 2), [9]), 'E0 9 3'),
            (lambda a: a.__setitem__(slice(1, 1), [5]), 'E0 1 5 2 3'),
            (lambda a: a.__setitem__(slice(None), []), 'E0'),
            (lambda a: a.__setitem__(slice(None, None, 2), [8, 9]), 'E0 8 2 9'),
            (lambda a: a.insert(0, 7), 'E0 7 1 2 3'),
            (lambda a: a.insert(10, 7), 'E0 1 2 3 7'),
            (lambda a: a.append(4), 'E0 1 2 3 4'),
            (lambda a: a.extend([4, '5.5']), 'E0 1 2 3 4 5.5'),
            (lambda a: a.__iadd__([4]), 'E0 1 2 3 4'),
            (lambda a: a.__imul__(2), 'E0 1 2 3 1 2 3'),
            (lambda a: a.__delitem__(1), 'E0 1 3'),
            (lambda a: a.__delitem__(-1), 'E0 1 2'),
            (lambda a: a.__delitem__(slice(0, 2)), 'E0 3'),
            (lambda a: a.__delitem__(slice(None, None, 2)), 'E0 2'),
            (lambda a: a.pop(), 'E0 1 2'),
            (lambda a: a.pop(0), 'E0 2 3'),
            (lambda a: a.remove(2), 'E0 1 3'),
            (lambda a: a.clear(), 'E0'),
        ],
    )
    def test_mutators_keep_spaces_in_step(self, mutate, expected) -> None:
        # Each mutator converts its values and keeps one space between items, so the card still round-trips.
        e, _ = pymcnp.inp.card.data.E.from_mcnp('E0 1 2 3')
        mutate(e.e)
        assert len(e.e.spaces) == max(len(e.e) - 1, 0)
        assert all(isinstance(value, pymcnp.inp.literal.Real) for value in e.e)
        assert e.to_mcnp() == expected
        # The text parses back to the same card, also when the array is empty.
        parsed, remainder = pymcnp.inp.card.data.E.from_mcnp(expected)
        assert remainder == ''
        assert parsed.e == e.e and parsed.to_mcnp() == expected
        if len(e.e):
            # An emptied array leaves the unused space after `suffix` stored, so only nonempty cards compare equal.
            assert parsed == e

    def test_empty_array_writes_no_trailing_space(self) -> None:
        # No space follows the last nonempty constituent, as when parsing, so `E0` writes `E0`, not `E0 `.
        card, remainder = pymcnp.inp.card.data.E.from_mcnp('E0')
        assert remainder == '' and card.e == [] and card.to_mcnp() == 'E0'

    def test_mutators_keep_continuation_spaces(self) -> None:
        # Spaces between kept items, e.g., a continuation line, stay where they are.
        e, _ = pymcnp.inp.card.data.E.from_mcnp('E0 1 2 &\n     3 4')
        e.e.insert(0, 0)
        del e.e[1]
        assert e.to_mcnp() == 'E0 0 2 &\n     3 4'

    @pytest.mark.parametrize('mutate', [lambda a: a.append('x'), lambda a: a.insert(0, 'x'), lambda a: a.extend(['x']), lambda a: a.__iadd__(['x'])])
    def test_mutators_reject_invalid_values(self, mutate) -> None:
        e, _ = pymcnp.inp.card.data.E.from_mcnp('E0 1 2 3')
        with pytest.raises(pymcnp.abc.Error):
            mutate(e.e)
        assert e.to_mcnp() == 'E0 1 2 3'

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
