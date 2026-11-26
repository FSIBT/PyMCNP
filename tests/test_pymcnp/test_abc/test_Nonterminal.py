import re
import typing

import numpy
import pytest

import pymcnp


class Nonterminal0(pymcnp.abc.Nonterminal):
    constituent0: typing.Annotated[pymcnp.abc.Array, pymcnp.inp.card.Cell, None] | typing.Annotated[pymcnp.abc.Array, pymcnp.inp.card.Surface, None]


class Test_Nonterminal:
    def test___new___valid(self) -> None:
        cell = pymcnp.inp.card.Cell_1(j='1', m=0, geom='+2.3')  # type:ignore
        assert cell.to_mcnp() == '1 0 +2.3'
        cell = pymcnp.inp.card.Cell_1(j='1', m=0, geom='+2.3', spaces={'j': pymcnp.inp.CardSpace('  '), 'm': pymcnp.inp.CardSpace('  ')})  # type:ignore
        assert cell.to_mcnp() == '1  0  +2.3'
        nonterminal = Nonterminal0(constituent0=pymcnp.abc.Array[pymcnp.inp.card.Surface, None](pymcnp.inp.card.Surface.from_mcnp('1 SO 1')[0], pymcnp.inp.card.Surface.from_mcnp('2 SO 2')[0]))
        assert nonterminal.to_mcnp() == '1 SO 1 2 SO 2'

    def test___new___invalid(self) -> None:
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.inp.card.Cell_1(j='A', m=0, geom='+2.3')  # type:ignore
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.inp.card.data.Vol(x=[3.1, 'J', 'A'])  # type:ignore
        with pytest.raises(pymcnp.abc.Error):
            pymcnp.inp.option.cell.Imp.from_mcnp('imp :@')

    def test_setter_valid(self) -> None:
        vol, _ = pymcnp.inp.card.data.Vol.from_mcnp('VOL 3.1 3.1')
        assert vol.to_mcnp() == 'VOL 3.1 3.1'
        vol.no = 'no'  # type:ignore
        assert vol.to_mcnp() == 'VOL no 3.1 3.1'
        vol.no = ''  # type:ignore
        assert vol.to_mcnp() == 'VOL 3.1 3.1'

    def test_setter_numpy_scalars(self) -> None:
        # NumPy scalars, e.g., from ``numpy.arange`` in a scan, are numbers like ``int`` and ``float``.
        nps, _ = pymcnp.inp.card.data.Nps.from_mcnp('NPS 10')
        nps.npp = numpy.int64(20)  # type:ignore
        e, _ = pymcnp.inp.card.data.E.from_mcnp('E0 1 2')
        e.e[1] = numpy.float64(2.5)
        e.e += list(numpy.arange(3, 5))
        assert nps.to_mcnp() == 'NPS 20'
        assert e.to_mcnp() == 'E0 1 2.5 3 4'

    @pytest.mark.parametrize('value', [None, object(), {'a': 1}])
    def test_setter_invalid_value_raises_error(self, value) -> None:
        nps, _ = pymcnp.inp.card.data.Nps.from_mcnp('NPS 10')
        with pytest.raises(pymcnp.abc.Error, match='Invalid value'):
            nps.npp = value  # type:ignore
        e, _ = pymcnp.inp.card.data.E.from_mcnp('E0 1 2')
        with pytest.raises(pymcnp.abc.Error, match='Invalid value'):
            e.e[0] = value

    @pytest.mark.parametrize('value', ['7 8', '7 $ comment', '7\nnps 1'])
    def test_setter_value_with_text_left_over_raises_error(self, value) -> None:
        # A value is stored whole or not at all: ``r = '7 8'`` does not store ``7`` and drop `` 8``.
        so, _ = pymcnp.inp.card.Surface.from_mcnp('1 SO 10')
        with pytest.raises(pymcnp.abc.Error, match='left over'):
            so.r = value  # type:ignore
        assert so.to_mcnp() == '1 SO 10'
        with pytest.raises(pymcnp.abc.Error, match='left over'):
            pymcnp.inp.card.surface.So(j=1, r=value)  # type:ignore

    def test_setter_title_with_a_second_line_raises_error(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp('title\n1 0 -1\n\n1 so 1\n\nnps 5\n')
        with pytest.raises(pymcnp.abc.Error, match='left over'):
            inp.title = 'A\nB'
        assert inp.title == 'title\n'

    def test_setting_an_empty_name_raises_attribute_error(self) -> None:
        rpp, _ = pymcnp.inp.card.Surface.from_mcnp('1 rpp -1 1 -1 1 -1 1')
        with pytest.raises(AttributeError, match="has no field ''"):
            setattr(rpp, '', 1)

    def test_setting_an_unknown_attribute_raises(self) -> None:
        # A name that is not a field, e.g., a typo or the radius of a box, is not silently stored.
        rpp, _ = pymcnp.inp.card.Surface.from_mcnp('1 rpp -1 1 -1 1 -1 1')
        with pytest.raises(AttributeError, match="Rpp has no field 'r'.*xmin"):
            rpp.r = 5  # type:ignore
        with pytest.raises(AttributeError, match="'x_min'"):
            setattr(rpp, 'x_min', 5)
        assert 'r' not in vars(rpp) and rpp.to_mcnp() == '1 rpp -1 1 -1 1 -1 1'
        # Methods are not fields either.
        with pytest.raises(AttributeError, match="'to_mcnp'"):
            rpp.to_mcnp = None  # type:ignore
        # Fields, ``spaces``, settable properties and private names may be set.
        rpp.xmin = -2  # type:ignore
        rpp.spaces = dict(rpp.spaces)
        rpp._note = 'private'
        assert rpp.to_mcnp() == '1 rpp -2 1 -1 1 -1 1'
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 -1\n\n1 SO 1\n\nnps 10\n')
        inp.nps = 20
        assert inp.nps == 20
        with pytest.raises(AttributeError):
            inp.npss = 20  # type:ignore
        # ``scan_with`` with a wrong name fails instead of making identical copies.
        with pytest.raises(AttributeError):
            next(inp.scan_with([1], lambda copy, r: setattr(copy.surface_cards(1)[0], 'radius', r)))

    def test_subclass_property_with_setter_may_be_set(self) -> None:
        # A subclass's own settable properties are found when the class is created; other names still raise.
        class Labelled(pymcnp.inp.card.surface.So):
            @property
            def label(self) -> str:
                return self._label

            @label.setter
            def label(self, value: str) -> None:
                self._label = value

        so = Labelled(j=1, r=2.0)
        so.label = 'ball'
        so.r = 3.0
        assert so.label == 'ball' and so.to_mcnp() == '1 SO 3.0'
        with pytest.raises(AttributeError, match="Labelled has no field 'labl'"):
            so.labl = 'x'  # type:ignore

    def test___class_getitem___valid(self) -> None:
        assert pymcnp.inp.card.Cell[0] == pymcnp.inp.card.Cell_0
        assert pymcnp.inp.card.Cell[1] == pymcnp.inp.card.Cell_1

    def test_scan_valid(self) -> None:
        vol, _ = pymcnp.inp.card.data.Vol.from_mcnp('VOL 3.1 3.1')
        assert tuple(map(str, vol.scan(no=('', 'no')))) == ('VOL 3.1 3.1', 'VOL no 3.1 3.1')

    def test_scan_invalid(self) -> None:
        vol, _ = pymcnp.inp.card.data.Vol.from_mcnp('VOL 3.1 3.1')
        with pytest.raises(pymcnp.abc.Error):
            next(vol.scan(hello=('', 'no')))
        with pytest.raises(pymcnp.abc.Error):
            next(vol.scan())

    def test_scan_with(self) -> None:
        inp, _ = pymcnp.Inp.from_mcnp('Hello\n1 0 -1\n\n1 SO 1\n\nnps 10\n')
        copies = list(inp.scan_with([1, 2], lambda i, v: setattr(i, 'nps', v)))
        assert [c.nps for c in copies] == [1, 2]
        assert inp.nps == 10


CALLS: list[tuple[str, str]] = []


class Space(pymcnp.abc.Terminal):
    _pattern = re.compile(r'( +)')
    _default = ' '


class Nonterminal1(pymcnp.abc.Nonterminal):
    _space: typing.ClassVar = (Space,)

    a: typing.Annotated[pymcnp.abc.Terminal, r'[a-z]+']
    b: typing.Annotated[pymcnp.abc.Terminal, r'[a-z]+']

    def __post_init__(self) -> None:
        CALLS.append((self.a, self.b))

        if self.b == 'bad':
            raise pymcnp.abc.Error('Invalid value.', f'{self.b=}')


class Nonterminal2(pymcnp.abc.Nonterminal):
    _space: typing.ClassVar = (Space,)

    a: typing.Annotated[pymcnp.abc.Terminal, r'[a-z]+']
    b: typing.Annotated[pymcnp.abc.Terminal, r'[a-z]+'] = pymcnp.abc.Terminal[r'[a-z]+']('z')

    def __post_init__(self) -> None:
        CALLS.append((self.a, self.b))

        if self.a == 'x' and self.b == 'z':
            raise pymcnp.abc.Error('Invalid value.', f'{self.a=} {self.b=}')


class Test_Nonterminal_build:
    def test_build_validates_once(self) -> None:
        CALLS.clear()
        nonterminal, remainder = Nonterminal1.from_mcnp('ab  cd')
        assert CALLS == [('ab', 'cd')]
        assert remainder == ''
        assert nonterminal == Nonterminal1(a='ab', b='cd', spaces={'a': Space('  ')})
        assert nonterminal.spaces == {'a': '  '}
        assert nonterminal.to_mcnp() == 'ab  cd'
        assert vars(nonterminal) == vars(Nonterminal1(a='ab', b='cd', spaces={'a': Space('  ')}))

        # Setters still validate.
        CALLS.clear()
        nonterminal.b = 'ef'  # type: ignore
        assert CALLS == [('ab', 'ef')]
        with pytest.raises(pymcnp.abc.Error):
            nonterminal.b = '12'  # type: ignore
        with pytest.raises(pymcnp.abc.Error, match='Invalid value'):
            nonterminal.b = 'bad'  # type: ignore

    def test_build_invalid_still_raises(self) -> None:
        with pytest.raises(pymcnp.abc.Error) as err:
            Nonterminal1.from_mcnp('ab bad')
        assert str(err.value) == "Invalid value.\n self.b='bad'"

    def test_build_default_after_last_required(self) -> None:
        # Fields with defaults after the last required one: the setters validate with the defaults first.
        CALLS.clear()
        nonterminal, _ = Nonterminal2.from_mcnp('ab cd')
        assert CALLS == [('ab', 'z'), ('ab', 'cd')]
        assert nonterminal.to_mcnp() == 'ab cd'

        with pytest.raises(pymcnp.abc.Error) as err:
            Nonterminal2.from_mcnp('x cd')
        assert str(err.value) == "Invalid value.\n self.a='x' self.b='z'"
